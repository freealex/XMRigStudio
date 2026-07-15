"""
ui/cpu.py

CPU monitoring page.

Displays:
- CPU backend
- Threads
- Hashrate per thread
- Memory usage
- Huge pages status
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QFormLayout,
    QTableWidget,
    QTableWidgetItem,
)


from PySide6.QtCore import Qt



class CPUPage(QWidget):


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



        # CPU information


        info_box = QGroupBox(
            "CPU Information"
        )


        form = QFormLayout()



        self.backend_label = QLabel(
            "-"
        )


        self.memory_label = QLabel(
            "-"
        )


        self.hugepages_label = QLabel(
            "-"
        )



        form.addRow(
            "Backend:",
            self.backend_label
        )


        form.addRow(
            "Memory:",
            self.memory_label
        )


        form.addRow(
            "Huge Pages:",
            self.hugepages_label
        )



        info_box.setLayout(
            form
        )


        layout.addWidget(
            info_box
        )



        # Thread table


        self.thread_table = QTableWidget()


        self.thread_table.setColumnCount(
            3
        )


        self.thread_table.setHorizontalHeaderLabels(
            [
                "Thread",
                "Affinity",
                "Hashrate"
            ]
        )


        layout.addWidget(
            self.thread_table
        )


        self.setLayout(
            layout
        )



    # =================================================
    # Signals
    # =================================================


    def connect_signals(self):


        self.updater.cpu_updated.connect(
            self.update_cpu
        )



    # =================================================
    # Update
    # =================================================


    def update_cpu(
        self,
        data
    ):


        if not data:

            return



        backends = data.get(
            "backends",
            []
        )


        if not backends:

            return



        cpu = None


        for backend in backends:

            if backend.get(
                "type"
            ) == "cpu":

                cpu = backend

                break



        if not cpu:

            return



        self.backend_label.setText(
            cpu.get(
                "type",
                "-"
            )
        )



        self.memory_label.setText(

            str(
                cpu.get(
                    "memory",
                    "-"
                )
            )

            +
            " bytes"

        )



        huge = cpu.get(
            "hugepages",
            []
        )


        self.hugepages_label.setText(
            str(huge)
        )



        threads = cpu.get(
            "threads",
            []
        )


        self.thread_table.setRowCount(
            len(threads)
        )



        for index, thread in enumerate(threads):


            self.thread_table.setItem(

                index,
                0,

                QTableWidgetItem(
                    str(index)
                )

            )


            self.thread_table.setItem(

                index,
                1,

                QTableWidgetItem(

                    str(
                        thread.get(
                            "affinity",
                            "-"
                        )
                    )

                )

            )


            rate = thread.get(
                "hashrate",
                [0]
            )[0]


            self.thread_table.setItem(

                index,
                2,

                QTableWidgetItem(

                    f"{rate:.2f} H/s"

                )

            )
