"""
ui/logs.py

Live XMRig Manager log viewer.

Displays messages emitted by:
    MinerUpdater.log_updated
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
    QLabel,
)


from PySide6.QtCore import Qt



class LogsPage(QWidget):


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
            "Miner Logs"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            title
        )



        self.log_view = QTextEdit()


        self.log_view.setReadOnly(
            True
        )


        layout.addWidget(
            self.log_view
        )



        # Buttons


        button_layout = QHBoxLayout()



        self.clear_button = QPushButton(
            "Clear Logs"
        )


        self.save_button = QPushButton(
            "Save Logs"
        )



        button_layout.addWidget(
            self.clear_button
        )


        button_layout.addWidget(
            self.save_button
        )


        layout.addLayout(
            button_layout
        )



        self.setLayout(
            layout
        )



    # =================================================
    # Signals
    # =================================================


    def connect_signals(self):


        self.updater.log_updated.connect(
            self.add_log
        )


        self.clear_button.clicked.connect(
            self.clear_logs
        )


        self.save_button.clicked.connect(
            self.save_logs
        )



    # =================================================
    # Log Handling
    # =================================================


    def add_log(
        self,
        message
    ):


        self.log_view.append(
            str(message)
        )



        scrollbar = (
            self.log_view.verticalScrollBar()
        )


        scrollbar.setValue(
            scrollbar.maximum()
        )



    def clear_logs(self):

        self.log_view.clear()



    def save_logs(self):


        filename = (
            "xmrig-manager.log"
        )


        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:


            file.write(
                self.log_view.toPlainText()
            )
