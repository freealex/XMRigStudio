"""
core/updater.py

Background XMRig updater thread.

Collects:
- miner summary
- CPU backend stats
- pool information
- miner configuration
- connection status

and pushes updates to the PySide6 GUI.
"""


from __future__ import annotations


import time
import traceback


from PySide6.QtCore import (
    QThread,
    Signal
)


from core.api import MinerAPI



class MinerUpdater(QThread):
    """
    Background worker for live miner updates.
    """


    # =================================================
    # Signals
    # =================================================

    summary_updated = Signal(dict)

    cpu_updated = Signal(dict)

    pool_updated = Signal(dict)

    config_updated = Signal(dict)

    log_updated = Signal(str)

    connection_changed = Signal(bool)

    error = Signal(str)



    # =================================================
    # Init
    # =================================================


    def __init__(
        self,
        api: MinerAPI,
        interval: int = 5,
        parent=None
    ):

        super().__init__(parent)


        self.api = api

        self.interval = interval


        self.running = False


        self.last_connection_state = None



    # =================================================
    # Thread Control
    # =================================================


    def start_updater(self):

        """
        Start updater thread safely.
        """

        if self.running:

            return



        self.running = True


        self.start()



    def stop(self):

        """
        Stop thread cleanly.
        """

        self.running = False



        if self.isRunning():

            self.wait(3000)



    # =================================================
    # Thread Loop
    # =================================================


    def run(self):

        self.log_updated.emit(
            "Miner updater started"
        )



        while self.running:


            try:

                self.update_data()



            except Exception as exc:


                message = (
                    f"Updater exception: {exc}"
                )


                self.error.emit(
                    message
                )


                self.log_updated.emit(
                    message
                )


                traceback.print_exc()



            time.sleep(
                self.interval
            )



        self.log_updated.emit(
            "Miner updater stopped"
        )



    # =================================================
    # Data Collection
    # =================================================


    def update_data(self):


        summary = (
            self.api.summary()
        )



        connected = (
            summary is not None
        )



        # Connection state change

        if connected != self.last_connection_state:


            self.connection_changed.emit(
                connected
            )


            self.last_connection_state = connected



            if connected:

                self.log_updated.emit(
                    "XMRig connected"
                )

            else:

                self.log_updated.emit(
                    "XMRig disconnected"
                )



        if not connected:

            return



        # ---------------------------------------------
        # Summary
        # ---------------------------------------------


        self.summary_updated.emit(
            summary
        )



        # ---------------------------------------------
        # CPU / Backend
        # ---------------------------------------------


        backends = (
            self.api.backends()
        )


        if backends:


            cpu_data = {

                "backends":
                    backends

            }


            self.cpu_updated.emit(
                cpu_data
            )



        # ---------------------------------------------
        # Pool
        # ---------------------------------------------


        pool = summary.get(
            "connection",
            {}
        )


        self.pool_updated.emit(
            pool
        )



        # ---------------------------------------------
        # Config
        # ---------------------------------------------


        config = (
            self.api.miner_config()
        )


        if config:

            self.config_updated.emit(
                config
            )



        # ---------------------------------------------
        # Logging
        # ---------------------------------------------


        hashrate = (

            summary
            .get(
                "hashrate",
                {}
            )
            .get(
                "total",
                [0]
            )[0]

        )


        shares = (

            summary
            .get(
                "results",
                {}
            )
            .get(
                "shares_good",
                0
            )

        )


        self.log_updated.emit(

            f"Hashrate: {hashrate:.2f} H/s | "
            f"Shares: {shares}"

        )
