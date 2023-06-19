import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, \
    QListWidgetItem
from Page import Ui_PageMainWindow
from new_vision import Ui_MainWindow
from scripts.run_load_data import main


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_page=Ui_MainWindow()
        self.open_book()

    def open_book(self,book):
        page_widget = QWidget()
        self.ui_page.setupUi(page_widget)
        self.ui.tabWidget.addTab(page_widget, "New Tab")

    def books_tab(self):
        curr_tab=self.ui.tabWidget.currentWidget()




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