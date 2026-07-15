"""
core/config.py

Production configuration manager for XMRig Manager.

Responsibilities:
- Load/save application settings
- Create default configuration
- Repair missing settings
- Provide typed accessors
"""

from __future__ import annotations

import json
import shutil
import tempfile

from pathlib import Path
from typing import Any, Dict


from core.constants import (
    SETTINGS_FILE,
    DEFAULT_API_HOST,
    DEFAULT_API_PORT,
    DEFAULT_API_TOKEN,
    DEFAULT_XMRIG_BINARY,
    DEFAULT_UPDATE_INTERVAL,
)

from core.exceptions import ConfigurationError



class ConfigManager:
    """
    Production configuration manager.
    """


    def __init__(self):

        self.path = Path(SETTINGS_FILE)

        self.settings: Dict[str, Any] = {}

        self.defaults = {

            "application": {

                "name": "XMRig Manager",

                "version": "1.0.0"
            },


            "xmrig": {

                "binary": DEFAULT_XMRIG_BINARY,

                "config": "",

                "auto_start": False
            },


            "api": {

                "host": DEFAULT_API_HOST,

                "port": DEFAULT_API_PORT,

                "token": DEFAULT_API_TOKEN,

                "version": None
            },


            "gui": {

                "theme": "dark",

                "refresh_interval": DEFAULT_UPDATE_INTERVAL
            },


            "logging": {

                "level": "INFO",

                "save_logs": True
            }

        }


        self.load()



    # =================================================
    # Load / Save
    # =================================================


    def load(self):

        """
        Load configuration.

        If missing:
            create defaults

        If incomplete:
            repair missing keys

        If corrupt:
            backup and restore defaults
        """

        try:

            self.path.parent.mkdir(
                parents=True,
                exist_ok=True
            )


            if not self.path.exists():

                self.settings = self._copy_defaults()

                self.save()

                return



            try:

                with open(
                    self.path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.settings = json.load(file)


            except json.JSONDecodeError:

                backup = self.path.with_suffix(
                    ".broken.json"
                )

                shutil.move(
                    self.path,
                    backup
                )

                self.settings = self._copy_defaults()

                self.save()

                return



            changed = self.merge_defaults()


            if changed:

                self.save()



        except Exception as exc:

            raise ConfigurationError(
                f"Configuration load failed: {exc}"
            )



    def save(self):

        """
        Atomic save.

        Writes temporary file first,
        then replaces original.
        """

        try:

            self.path.parent.mkdir(
                parents=True,
                exist_ok=True
            )


            fd, temp_path = tempfile.mkstemp(
                dir=self.path.parent,
                prefix="settings_",
                suffix=".tmp"
            )


            with open(
                fd,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.settings,
                    file,
                    indent=4
                )


            shutil.move(
                temp_path,
                self.path
            )


        except Exception as exc:

            raise ConfigurationError(
                f"Configuration save failed: {exc}"
            )



    # =================================================
    # Default Handling
    # =================================================


    def _copy_defaults(self):

        return json.loads(
            json.dumps(
                self.defaults
            )
        )



    def merge_defaults(self):

        """
        Add missing configuration keys.
        """

        changed = False


        for section, values in self.defaults.items():

            if section not in self.settings:

                self.settings[section] = values

                changed = True

                continue



            for key, value in values.items():

                if key not in self.settings[section]:

                    self.settings[section][key] = value

                    changed = True



        return changed



    # =================================================
    # Generic Access
    # =================================================


    def get(
        self,
        section: str,
        key: str,
        default=None
    ):

        return (

            self.settings
            .get(section, {})
            .get(key, default)

        )



    def set(
        self,
        section: str,
        key: str,
        value: Any
    ):


        if section not in self.settings:

            self.settings[section] = {}


        self.settings[section][key] = value


        self.save()



    def all(self):

        return self.settings



    # =================================================
    # API Settings
    # =================================================


    def api_settings(self):

        return {

            "host":
                self.get(
                    "api",
                    "host",
                    DEFAULT_API_HOST
                ),


            "port":
                self.get(
                    "api",
                    "port",
                    DEFAULT_API_PORT
                ),


            "token":
                self.get(
                    "api",
                    "token",
                    DEFAULT_API_TOKEN
                )

        }



    # =================================================
    # XMRig Settings
    # =================================================


    def xmrig_binary(self):

        return self.get(
            "xmrig",
            "binary",
            DEFAULT_XMRIG_BINARY
        )



    def xmrig_config(self):

        return self.get(
            "xmrig",
            "config",
            ""
        )



    def auto_start(self):

        return self.get(
            "xmrig",
            "auto_start",
            False
        )



    # =================================================
    # GUI Settings
    # =================================================


    def refresh_interval(self):

        return self.get(
            "gui",
            "refresh_interval",
            DEFAULT_UPDATE_INTERVAL
        )



    def theme(self):

        return self.get(
            "gui",
            "theme",
            "dark"
        )



    # =================================================
    # Logging Settings
    # =================================================


    def log_level(self):

        return self.get(
            "logging",
            "level",
            "INFO"
        )
