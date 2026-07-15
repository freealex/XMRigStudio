"""
ui/config_page.py

Live XMRig configuration viewer.

Uses:
    updater.config_updated
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QFormLayout,
    QTextEdit,
)

from PySide6.QtCore import Qt

import json



class ConfigPage(QWidget):


    def __init__(
        self,
        updater,
        parent=None
    ):

        super().__init__(parent)

        self.updater = updater

        self.setup_ui()

        self.connect_signals()



    # ==========================================
    # UI
    # ==========================================


    def setup_ui(self):


        layout = QVBoxLayout()



        title = QLabel(
            "XMRig Configuration"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            title
        )



        # Basic config


        info_box = QGroupBox(
            "Miner Settings"
        )


        form = QFormLayout()



        self.worker_label = QLabel(
            "-"
        )


        self.api_label = QLabel(
            "-"
        )


        self.pool_label = QLabel(
            "-"
        )


        self.donate_label = QLabel(
            "-"
        )


        form.addRow(
            "Worker ID:",
            self.worker_label
        )


        form.addRow(
            "API:",
            self.api_label
        )


        form.addRow(
            "Pool:",
            self.pool_label
        )


        form.addRow(
            "Donate Level:",
            self.donate_label
        )



        info_box.setLayout(
            form
        )


        layout.addWidget(
            info_box
        )



        # Raw JSON viewer


        json_box = QGroupBox(
            "Raw Configuration"
        )


        json_layout = QVBoxLayout()



        self.json_view = QTextEdit()


        self.json_view.setReadOnly(
            True
        )


        json_layout.addWidget(
            self.json_view
        )


        json_box.setLayout(
            json_layout
        )


        layout.addWidget(
            json_box
        )


        self.setLayout(
            layout
        )



    # ==========================================
    # Signals
    # ==========================================


    def connect_signals(self):


        self.updater.config_updated.connect(
            self.update_config
        )



    # ==========================================
    # Update
    # ==========================================


    def update_config(
        self,
        data
    ):


        if not data:

            return



        api = data.get(
            "api",
            {}
        )


        pools = data.get(
            "pools",
            []
        )


        pool = "-"


        if pools:

            pool = pools[0].get(
                "url",
                "-"
            )



        self.worker_label.setText(

            str(
                api.get(
                    "worker-id",
                    "-"
                )
            )

        )


        self.api_label.setText(

            f"{data.get('http', {}).get('host', '-')}:"
            f"{data.get('http', {}).get('port', '-')}"

        )


        self.pool_label.setText(
            pool
        )


        self.donate_label.setText(

            str(
                data.get(
                    "donate-level",
                    "-"
                )
            )

        )



        self.json_view.setText(

            json.dumps(
                data,
                indent=4
            )

        )
