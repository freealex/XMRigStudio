"""
core/api.py

Production XMRig API client.

Handles:
- XMRig HTTP API communication
- Authentication
- API version detection
- Retry handling
- Connection tracking
- Miner data retrieval
"""

from __future__ import annotations

import time
from typing import Any, Dict, Optional

import requests

from core.config import ConfigManager
from core.exceptions import (
    APIAuthenticationError,
)


class MinerAPI:


    def __init__(
        self,
        config: ConfigManager | None = None
    ):

        # IMPORTANT:
        # Do not name this "config"
        # because it conflicts with miner_config()
        self.config_manager = (
            config or ConfigManager()
        )


        api_settings = (
            self.config_manager.api_settings()
        )


        self.host = api_settings["host"]

        self.port = api_settings["port"]

        self.token = api_settings["token"]


        self.base_url = (
            f"http://{self.host}:{self.port}"
        )


        self.session = requests.Session()


        self.session.headers.update(
            {
                "Authorization":
                    f"Bearer {self.token}",

                "Accept":
                    "application/json",

                "User-Agent":
                    "XMRig-Manager"
            }
        )


        self.timeout = 5


        self.api_version = None

        self.connected = False


        self.detect_version()



    # =================================================
    # API Detection
    # =================================================


    def detect_version(self):

        """
        Detect available XMRig API version.
        """

        for version in ("2", "1"):

            try:

                result = self._request(
                    f"/{version}/summary",
                    retries=1
                )


                if result:

                    self.api_version = version

                    self.connected = True

                    return True


            except Exception:

                continue



        self.connected = False

        return False



    # =================================================
    # HTTP Requests
    # =================================================


    def _request(
        self,
        endpoint: str | None,
        retries: int = 3
    ) -> Optional[Dict[str, Any]]:


        if not endpoint:

            return None



        url = (
            self.base_url
            +
            endpoint
        )


        delay = 1



        for attempt in range(retries):

            try:

                response = self.session.get(
                    url,
                    timeout=self.timeout
                )



                if response.status_code == 401:

                    raise APIAuthenticationError(
                        "Invalid XMRig API token"
                    )



                response.raise_for_status()



                self.connected = True


                return response.json()



            except requests.exceptions.ConnectionError:

                self.connected = False



            except requests.exceptions.Timeout:

                self.connected = False



            if attempt < retries - 1:

                time.sleep(delay)

                delay *= 2



        return None



    # =================================================
    # Endpoint Builder
    # =================================================


    def endpoint(
        self,
        path: str
    ):


        if not self.api_version:

            self.detect_version()



        if not self.api_version:

            return None



        return (
            f"/{self.api_version}{path}"
        )



    # =================================================
    # Miner Data
    # =================================================


    def summary(self):

        return self._request(
            self.endpoint(
                "/summary"
            )
        )



    def backends(self):

        return self._request(
            self.endpoint(
                "/backends"
            )
        )



    def miner_config(self):

        """
        Retrieve running XMRig configuration.
        """

        return self._request(
            self.endpoint(
                "/config"
            )
        )



    # =================================================
    # Miner Controls
    # =================================================


    def pause(self):

        return self._request(
            self.endpoint(
                "/pause"
            )
        )



    def resume(self):

        return self._request(
            self.endpoint(
                "/resume"
            )
        )



    # =================================================
    # Convenience Functions
    # =================================================


    def is_connected(self):

        return self.connected



    def hashrate(self):

        data = self.summary()


        if not data:

            return 0



        return (
            data
            .get(
                "hashrate",
                {}
            )
            .get(
                "total",
                [0]
            )[0]
        )



    def pool(self):

        data = self.summary()


        if not data:

            return {}



        return data.get(
            "connection",
            {}
        )
