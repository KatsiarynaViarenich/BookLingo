import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, \
    QListWidgetItem
from Page import Ui_PageMainWindow
from Loged import Ui_LogedQMainWindow
from NotLoged import Ui_NotLogedMainWindow
from new_vision import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_page=Ui_PageMainWindow()
        self.open_book()

        self.ui_loged=Ui_LogedQMainWindow()
        self.ui_notloged=Ui_NotLogedMainWindow()
        self.ui_log =self.ui_notloged
        self.ui_log.setupUi(self.ui_notloged)
        self.account_buttons()

    def account(self):
        if self.ui_log == self.ui_loged:
            log_widget = QWidget(self.ui.tab_account)
            self.ui_loged.setupUi(log_widget)
        else:
            log_widget = QWidget(self.ui.tab_account)
            self.ui_notloged.setupUi(log_widget)

    def account_buttons(self):
        self.ui_notloged.LogInButton.clicked.connect(self.logIn)
        self.ui_loged.LogOutButton.clicked.connect(self.logOut)

    def logIn(self):
        self.ui_log = self.ui_notloged
        self.ui_log = Ui_NotLogedMainWindow()  # Создаем новый экземпляр Ui_NotLogedMainWindow
        self.ui_log.setupUi(self.ui.tab_account)

    def logOut(self):
        self.ui_log = self.ui_loged
        self.ui_log = Ui_LogedQMainWindow()  # Создаем новый экземпляр Ui_LogedQMainWindow
        self.ui_log.setupUi(self.ui.tab_account)

    def open_book(self):
        page_widget = QWidget()
        self.ui_page.setupUi(page_widget)
        self.ui.tabWidget.addTab(page_widget, "Book's name")

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