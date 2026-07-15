"""
ui/pool.py

Pool monitoring page.

Displays:
- Pool address
- Pool IP
- Algorithm
- Difficulty
- Ping
- Accepted shares
- Rejected shares
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QFormLayout,
)


from PySide6.QtCore import Qt



class PoolPage(QWidget):


    def __init__(
        self,
        updater,
        parent=None
    ):

        super().__init__(parent)


        self.updater = updater


        self.setup_ui()


        self.connect_signals()



    # =================================================
    # UI
    # =================================================


    def setup_ui(self):


        layout = QVBoxLayout()



        title = QLabel(
            "Pool Information"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            title
        )



        pool_box = QGroupBox(
            "Current Pool"
        )


        form = QFormLayout()



        self.pool_label = QLabel(
            "-"
        )


        self.ip_label = QLabel(
            "-"
        )


        self.algorithm_label = QLabel(
            "-"
        )


        self.diff_label = QLabel(
            "-"
        )


        self.ping_label = QLabel(
            "-"
        )


        self.accepted_label = QLabel(
            "-"
        )


        self.rejected_label = QLabel(
            "-"
        )


        self.uptime_label = QLabel(
            "-"
        )



        form.addRow(
            "Pool:",
            self.pool_label
        )


        form.addRow(
            "IP:",
            self.ip_label
        )


        form.addRow(
            "Algorithm:",
            self.algorithm_label
        )


        form.addRow(
            "Difficulty:",
            self.diff_label
        )


        form.addRow(
            "Ping:",
            self.ping_label
        )


        form.addRow(
            "Accepted:",
            self.accepted_label
        )


        form.addRow(
            "Rejected:",
            self.rejected_label
        )


        form.addRow(
            "Connection Uptime:",
            self.uptime_label
        )



        pool_box.setLayout(
            form
        )


        layout.addWidget(
            pool_box
        )


        layout.addStretch()



        self.setLayout(
            layout
        )



    # =================================================
    # Signals
    # =================================================


    def connect_signals(self):


        self.updater.pool_updated.connect(
            self.update_pool
        )



    # =================================================
    # Update Data
    # =================================================


    def update_pool(
        self,
        data
    ):


        if not data:

            return



        self.pool_label.setText(

            str(
                data.get(
                    "pool",
                    "-"
                )
            )

        )



        self.ip_label.setText(

            str(
                data.get(
                    "ip",
                    "-"
                )
            )

        )



        self.algorithm_label.setText(

            str(
                data.get(
                    "algo",
                    "-"
                )
            )

        )



        self.diff_label.setText(

            str(
                data.get(
                    "diff",
                    "-"
                )
            )

        )



        ping = data.get(
            "ping",
            0
        )


        self.ping_label.setText(

            f"{ping} ms"

        )



        self.accepted_label.setText(

            str(
                data.get(
                    "accepted",
                    0
                )
            )

        )



        self.rejected_label.setText(

            str(
                data.get(
                    "rejected",
                    0
                )
            )

        )



        uptime = data.get(
            "uptime",
            0
        )


        self.uptime_label.setText(

            self.format_time(
                uptime
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
