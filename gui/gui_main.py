import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, \
    QListWidgetItem, QMessageBox
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
        self.ui_log=self.ui_notloged
        self.account_buttons()
        self.ui.tabWidget.currentChanged.connect(self.open_tab)

        self.ui.tabWidget.setCurrentIndex(0)

    def open_tab(self, index):
        if self.ui_log==self.ui_notloged:
            if index not in [0, 1]:  # Индексы вкладок "Home" и "Account"
                QMessageBox.warning(self, "Oops...", "user is not logged.\nGo to Accounts->Log In.")
                self.ui.tabWidget.setCurrentIndex(0)
            else:
                self.ui.tabWidget.setCurrentIndex(index)

    def account_buttons(self):
        if self.ui_log == self.ui_loged:
            self.logIn()
        else:
            self.logOut()

    def logIn(self):
        tab_index = 1  # Индекс целевой закладки
        self.ui.tabWidget.removeTab(tab_index)
        self.ui.tab_account=QWidget()
        self.ui.tabWidget.insertTab(tab_index,self.ui.tab_account,"Account")
        self.ui_log = self.ui_loged
        self.ui_log.setupUi(self.ui.tab_account)
        self.ui_log.LogOutButton.clicked.connect(self.logOut)
        self.ui.tabWidget.setCurrentIndex(tab_index)

    def logOut(self):
        tab_index=1
        self.ui.tabWidget.removeTab(tab_index)
        self.ui.tab_account=QWidget()
        self.ui.tabWidget.insertTab(tab_index,self.ui.tab_account,"Account")
        self.ui_log = self.ui_notloged
        self.ui_log.setupUi(self.ui.tab_account)
        self.ui_log.LogInButton.clicked.connect(self.logIn)
        self.ui_log.RegisterButton.clicked.connect(print("register"))
        self.ui.tabWidget.setCurrentIndex(tab_index)


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