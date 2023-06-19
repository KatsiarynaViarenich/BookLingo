import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, \
    QListWidgetItem
from Page import Ui_PageMainWindow
from new_vision import Ui_MainWindow




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_main=Ui_MainWindow()
        self.open_book()

    def open_book(self):
        page_widget = QWidget()
        page_ui = Ui_PageMainWindow()
        page_ui.setupUi(page_widget)
        self.ui.tabWidget.addTab(page_widget, "New Tab")



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    layout = QVBoxLayout()
    layout.addWidget(window.ui.tabWidget)
    central_widget = QWidget()
    central_widget.setLayout(layout)

    window.setCentralWidget(central_widget)
    window.show()
    sys.exit(app.exec())