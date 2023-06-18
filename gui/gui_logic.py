from PySide6.QtWidgets import QMainWindow

import Main


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui= Main.Ui_StartMainWindow()
        self.ui.setupUi(self)
        self.ui.current_index=0
        #Path
        self.ui.OpenPathButt.setCheckable(True)
        self.ui.OpenPathButt.clicked.connect(self.read_path)
        #next and prev
        self.ui.list_widget.currentRowChanged.connect(self.show_log_details)
        self.ui.NextButt.clicked.connect(self.go_next)
        self.ui.PreviousButt.clicked.connect(self.go_back)