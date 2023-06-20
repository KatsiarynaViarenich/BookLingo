import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, \
    QListWidgetItem, QMessageBox, QListView
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Page import Ui_PageMainWindow
from Loged import Ui_LogedQMainWindow
from NotLoged import Ui_NotLogedMainWindow
from new_vision import Ui_MainWindow
from LoginWindow import Ui_LoginPageMainWindow
from RegisterWindow import Ui_RegisterQMainWindow
from services.authorizing_process import AuthorizingProcess
from services.user_session import UserSession
from scripts.run_setup import User,Book,Quote,Base
from PySide6.QtGui import QStandardItem, QStandardItemModel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.user = None
        """
        Is session must be inside? 
        """
        engine = create_engine('sqlite:///../data/app.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.ap=AuthorizingProcess(self.session)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_page=Ui_PageMainWindow()
        self.open_book() #wkinut w funkcyu



        self.ui_loged=Ui_LogedQMainWindow()
        self.ui_notloged=Ui_NotLogedMainWindow()
        self.ui_logPage=Ui_LoginPageMainWindow()
        self.ui_register=Ui_RegisterQMainWindow()

        self.ui_log=self.ui_notloged

        self.account_buttons()
        self.ui.tabWidget.currentChanged.connect(self.open_tab)
        self.ui.tabWidget.setCurrentIndex(0)

    def open_tab(self, index):
        if self.ui_log == self.ui_logPage or self.ui_log == self.ui_register:
            if index!=1:
                QMessageBox.warning(self, "Oops...", "You're not logged.\nGo to Accounts.")
                self.logOut()
                self.ui.tabWidget.setCurrentIndex(0)
        elif self.ui_log==self.ui_notloged:
            if index not in [0, 1]:
                QMessageBox.warning(self, "Oops...", "You're not logged.\nGo to Accounts.")
                self.ui.tabWidget.setCurrentIndex(0)
            else:
                self.ui.tabWidget.setCurrentIndex(index)

    def account_buttons(self):
        if self.ui_log == self.ui_loged:
            self.logIn()
        else:
            self.logOut()

    def logInPage(self):
        tab_index = 1
        self.ui.tabWidget.removeTab(tab_index)
        self.ui.tab_account=QWidget()
        self.ui.tabWidget.insertTab(tab_index,self.ui.tab_account,"Login")
        self.ui_log=self.ui_logPage

        self.ui_log.setupUi(self.ui.tab_account)
        self.ui_log.LogInButton.clicked.connect(self.authorization_login)
        self.ui_log.RegisterButton.clicked.connect(self.registerPage)

        self.ui.tabWidget.setCurrentIndex(tab_index)

    def authorization_login(self):
        #you're in loginpage
        username=self.ui_log.loginLine.text()
        password=self.ui_log.passLine.text()
        message=self.ap.log_in(username,password)

        if message!="Login successful":
            self.logInPage()
            QMessageBox.warning(self, "Authorizing", message)
        else:
            self.user = UserSession(self.session, self.session.query(User).filter_by(name=username).first().id)
            self.books_tab()
            print(f"{username},{password}")
            self.logIn()


    def authorization_create_acc(self):
        username=self.ui_log.loginLine.text()
        password=self.ui_log.passLine.text()
        message=self.ap.create_new_account(username,password)

        if message!="Account created successfully":
            QMessageBox.warning(self, "Authorizing", message)
            self.registerPage()
        else:
            print(f"{username},{password}")
            self.logIn()

    def registerPage(self):
        tab_index = 1
        self.ui.tabWidget.removeTab(tab_index)
        self.ui.tab_account = QWidget()
        self.ui.tabWidget.insertTab(tab_index, self.ui.tab_account, "Register")
        self.ui_log = self.ui_register

        self.ui_log.setupUi(self.ui.tab_account)
        self.ui_log.RegisterButton.clicked.connect(self.authorization_create_acc)

        self.ui.tabWidget.setCurrentIndex(tab_index)


    def logIn(self):

            tab_index = 1
            self.ui.tabWidget.removeTab(tab_index)
            self.ui.tab_account = QWidget()
            self.ui.tabWidget.insertTab(tab_index, self.ui.tab_account, "Account")
            self.ui_log = self.ui_loged
            self.ui_log.setupUi(self.ui.tab_account)
            self.ui_log.LogOutButton.clicked.connect(self.logOut)


            html_text=QCoreApplication.translate("","<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">"
"p, li { white-space: pre-wrap; }"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Dear </span><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">User</span><span style=\" font-size:14pt; font-weight:600;\">,</span></p>"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Feel free to browse through our library, add books to your library or favorite quotes. We hope you have a delightful reading experience with BookLingo.</span></p></body></html>")
            html_text=html_text.replace(
                "<span style=\" font-size:14pt; font-weight:600; font-style:italic;\">User</span>",
                f"<span style=\" font-size:14pt; font-weight:600; font-style:italic;\">{self.session.query(User).filter_by(id=self.user.user_id).first().name}</span>")

            self.ui_log.HelloUserQTextEdit.setHtml(html_text)
            self.ui.tabWidget.setCurrentIndex(tab_index)

    def logOut(self):
        tab_index=1
        self.ui.tabWidget.removeTab(tab_index)
        self.ui.tab_account=QWidget()
        self.ui.tabWidget.insertTab(tab_index,self.ui.tab_account,"Account")
        self.ui_log = self.ui_notloged
        self.ui_log.setupUi(self.ui.tab_account)
        self.ui_log.LogInButton.clicked.connect(self.logInPage)
        self.ui_log.RegisterButton.clicked.connect(self.registerPage)
        self.ui.tabWidget.setCurrentIndex(tab_index)

        self.ui.tabWidget.setCurrentIndex(tab_index)



    def open_book(self):
        page_widget = QWidget()
        self.ui_page.setupUi(page_widget)
        self.ui.tabWidget.addTab(page_widget, "Book's name")

    def books_tab(self):
        model=QStandardItemModel()
        for book in self.user.get_other_books(): ##?
            item=QStandardItem(f"\"{book.title}\" - {book.author} ")
            model.appendRow(item)
        self.ui.FoundBookslistView.setModel(model)
        self.ui.FoundBookslistView.setSelectionMode(QListView.ExtendedSelection)



if __name__ == "__main__":
    print()
    app = QApplication()
    window = MainWindow()
    layout = QVBoxLayout()
    layout.addWidget(window.ui.tabWidget)
    central_widget = QWidget()
    central_widget.setLayout(layout)

    window.setCentralWidget(central_widget)
    window.show()
    sys.exit(app.exec())