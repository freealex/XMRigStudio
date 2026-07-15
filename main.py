"""
main.py

XMRig Manager application entry point.
"""


from __future__ import annotations


import sys
import traceback


from PySide6.QtWidgets import QApplication


from core.api import MinerAPI
from core.updater import MinerUpdater

from ui.main_window import MainWindow



APP_NAME = "XMRig Manager"



def exception_hook(
    exc_type,
    exc_value,
    exc_traceback
):

    """
    Global exception handler.
    """

    if issubclass(
        exc_type,
        KeyboardInterrupt
    ):

        sys.__excepthook__(
            exc_type,
            exc_value,
            exc_traceback
        )

        return



    print(
        "".join(
            traceback.format_exception(
                exc_type,
                exc_value,
                exc_traceback
            )
        )
    )



sys.excepthook = exception_hook



def main():


    # ---------------------------------
    # Qt Application
    # ---------------------------------

    app = QApplication(
        sys.argv
    )


    app.setApplicationName(
        APP_NAME
    )



    # ---------------------------------
    # XMRig API
    # ---------------------------------

    try:

        api = MinerAPI()


    except Exception as exc:


        print(
            f"Failed creating API client: {exc}"
        )

        return 1



    # ---------------------------------
    # Background updater
    # ---------------------------------

    updater = MinerUpdater(
        api=api,
        interval=5
    )



    # ---------------------------------
    # Main Window
    # ---------------------------------

    window = MainWindow(
        updater
    )


    window.show()



    # ---------------------------------
    # Start live updates
    # ---------------------------------

    updater.start_updater()



    # ---------------------------------
    # Qt Event Loop
    # ---------------------------------

    exit_code = app.exec()



    # ---------------------------------
    # Shutdown
    # ---------------------------------

    updater.stop()



    return exit_code




if __name__ == "__main__":

    sys.exit(
        main()
    )
