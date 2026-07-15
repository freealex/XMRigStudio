"""
ui/dashboard.py

Main dashboard page for XMRig Manager.

Displays:
- Connection status
- Worker ID
- Pool
- Algorithm
- Hashrate
- Shares
- Uptime
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QGroupBox,
    QFormLayout,
    QPushButton,
)


from PySide6.QtCore import Qt



class Dashboard(QWidget):


    def __init__(
        self,
        updater,
        parent=None
    ):

        super().__init__(parent)


        self.updater = updater


        self.build_ui()

        self.connect_signals()



    # =================================================
    # Build Interface
    # =================================================


    def build_ui(self):


        layout = QVBoxLayout()


        # -----------------------------
        # Title
        # -----------------------------

        title = QLabel(
            "Miner Dashboard"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            title
        )



        # -----------------------------
        # Status
        # -----------------------------


        status_group = QGroupBox(
            "Status"
        )


        status_form = QFormLayout()



        self.status_value = QLabel(
            "Waiting..."
        )


        self.worker_value = QLabel(
            "-"
        )


        self.pool_value = QLabel(
            "-"
        )


        self.algorithm_value = QLabel(
            "-"
        )



        status_form.addRow(
            "Connection:",
            self.status_value
        )


        status_form.addRow(
            "Worker:",
            self.worker_value
        )


        status_form.addRow(
            "Pool:",
            self.pool_value
        )


        status_form.addRow(
            "Algorithm:",
            self.algorithm_value
        )



        status_group.setLayout(
            status_form
        )


        layout.addWidget(
            status_group
        )



        # -----------------------------
        # Performance
        # -----------------------------


        performance_group = QGroupBox(
            "Performance"
        )


        performance_form = QFormLayout()



        self.hashrate_value = QLabel(
            "0 H/s"
        )


        self.accepted_value = QLabel(
            "0"
        )


        self.rejected_value = QLabel(
            "0"
        )


        self.uptime_value = QLabel(
            "00:00:00"
        )



        performance_form.addRow(
            "Hashrate:",
            self.hashrate_value
        )


        performance_form.addRow(
            "Accepted Shares:",
            self.accepted_value
        )


        performance_form.addRow(
            "Rejected Shares:",
            self.rejected_value
        )


        performance_form.addRow(
            "Uptime:",
            self.uptime_value
        )



        performance_group.setLayout(
            performance_form
        )


        layout.addWidget(
            performance_group
        )



        # -----------------------------
        # Controls
        # -----------------------------


        button_layout = QHBoxLayout()



        self.start_button = QPushButton(
            "Start"
        )


        self.stop_button = QPushButton(
            "Stop"
        )


        self.stop_button.setEnabled(
            False
        )


        button_layout.addWidget(
            self.start_button
        )


        button_layout.addWidget(
            self.stop_button
        )


        layout.addLayout(
            button_layout
        )



        layout.addStretch()



        self.setLayout(
            layout
        )



    # =================================================
    # Signal Wiring
    # =================================================


    def connect_signals(self):


        self.updater.summary_updated.connect(
            self.update_summary
        )


        self.updater.connection_changed.connect(
            self.update_connection
        )



    # =================================================
    # Update Functions
    # =================================================


    def update_connection(
        self,
        connected
    ):


        if connected:

            self.status_value.setText(
                "Connected"
            )

            self.status_value.setStyleSheet(
                "color: green;"
            )


        else:

            self.status_value.setText(
                "Disconnected"
            )

            self.status_value.setStyleSheet(
                "color: red;"
            )



    def update_summary(
        self,
        data
    ):


        if not data:

            return



        self.worker_value.setText(

            str(
                data.get(
                    "worker_id",
                    "-"
                )
            )

        )



        self.algorithm_value.setText(

            str(
                data.get(
                    "algo",
                    "-"
                )
            )

        )



        connection = data.get(
            "connection",
            {}
        )


        self.pool_value.setText(

            str(
                connection.get(
                    "pool",
                    "-"
                )
            )

        )



        hashrate = (

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


        self.hashrate_value.setText(

            f"{hashrate:.2f} H/s"

        )



        results = data.get(
            "results",
            {}
        )


        accepted = results.get(
            "shares_good",
            0
        )


        total = results.get(
            "shares_total",
            0
        )


        self.accepted_value.setText(
            str(accepted)
        )


        self.rejected_value.setText(

            str(
                total - accepted
            )

        )



        self.uptime_value.setText(

            self.format_time(
                data.get(
                    "uptime",
                    0
                )
            )

        )



    # =================================================
    # Helpers
    # =================================================


    def format_time(
        self,
        seconds
    ):


        hours = seconds // 3600


        minutes = (
            seconds % 3600
        ) // 60


        secs = (
            seconds % 60
        )


        return (
            f"{hours:02}:"
            f"{minutes:02}:"
            f"{secs:02}"
        )
