"""
ui/main_window.py

Main XMRig Manager application window.

Creates:
- Dashboard
- CPU
- Pool
- Config
- Logs

and connects them to the shared MinerUpdater.
"""


from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTabWidget,
)

from PySide6.QtCore import Qt


from ui.dashboard import Dashboard
from ui.cpu import CPUPage
from ui.pool import PoolPage
from ui.config_page import ConfigPage
from ui.logs import LogsPage



class MainWindow(QMainWindow):


    def __init__(
        self,
        updater,
        parent=None
    ):

        super().__init__(parent)


        self.updater = updater


        self.setup_window()

        self.setup_ui()



    # =================================================
    # Window Setup
    # =================================================


    def setup_window(self):


        self.setWindowTitle(
            "XMRig Manager"
        )


        self.resize(
            1200,
            700
        )



    # =================================================
    # UI Construction
    # =================================================


    def setup_ui(self):


        central = QWidget()


        self.setCentralWidget(
            central
        )


        layout = QVBoxLayout()


        central.setLayout(
            layout
        )



        # Title

        title = QLabel(
            "XMRig Manager"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            title
        )



        # Tabs

        self.tabs = QTabWidget()


        layout.addWidget(
            self.tabs
        )



        self.create_pages()



    # =================================================
    # Pages
    # =================================================


    def create_pages(self):


        self.dashboard_page = Dashboard(
            self.updater
        )


        self.cpu_page = CPUPage(
            self.updater
        )


        self.pool_page = PoolPage(
            self.updater
        )


        self.config_page = ConfigPage(
            self.updater
        )


        self.logs_page = LogsPage(
            self.updater
        )



        self.tabs.addTab(
            self.dashboard_page,
            "Dashboard"
        )


        self.tabs.addTab(
            self.cpu_page,
            "CPU"
        )


        self.tabs.addTab(
            self.pool_page,
            "Pool"
        )


        self.tabs.addTab(
            self.config_page,
            "Config"
        )


        self.tabs.addTab(
            self.logs_page,
            "Logs"
        )



    # =================================================
    # Shutdown Handling
    # =================================================


    def closeEvent(
        self,
        event
    ):


        if self.updater:


            self.updater.stop()



        event.accept()
