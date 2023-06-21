import sys
from functools import partial

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, \
    QListWidgetItem, QMessageBox, QListView, QMenu
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
from PySide6.QtGui import QStandardItem, QStandardItemModel, QContextMenuEvent, QAction, Qt
from services.book_session import BookSession
from modules import question_generator, wikipedia_search,fancy_words_generator,phrase_translation


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
        self.books=[]

        self.ui_loged=Ui_LogedQMainWindow()
        self.ui_notloged=Ui_NotLogedMainWindow()
        self.ui_logPage=Ui_LoginPageMainWindow()
        self.ui_register=Ui_RegisterQMainWindow()

        self.ui_log=self.ui_notloged

        self.account_buttons()
        self.ui.tabWidget.currentChanged.connect(self.open_tab)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui_page.setupUi(self)

        self.ui_page.textEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui_page.textEdit.customContextMenuRequested.connect(self.open_context_menu)

    def open_tab(self, index):
        if self.ui_log == self.ui_logPage or self.ui_log == self.ui_register:
            if index not in [0, 1]:
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
            self.load_users_things()
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
            self.ui.tabWidget.setCurrentIndex(0)

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
        if self.user!=None:
            self.load_users_things()
            for index in range(self.ui.tabWidget.count(),5,-1):
                self.ui.tabWidget.removeTab(index-1)
            self.books=[]
            self.user=None
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
        library_model = self.ui.FoundBookslistView.model()
        selected_indexes = self.ui.MyBookslistView.selectedIndexes()
        if not selected_indexes:
            return
        my_books_model = self.ui.MyBookslistView.model()
        book_item = self.ui.MyBookslistView.model().itemFromIndex(selected_indexes[0])
        book_name = book_item.text().split(" - ")
        book_name[0] = book_name[0].replace('"', '')
        book_name[1] = book_name[1]
        print(book_name)
        page_widget = QWidget()
        self.ui_page.setupUi(page_widget)
        self.ui.tabWidget.addTab(page_widget, book_item.text())

        book = None
        for b in self.user.get_user_books():
            if b.title == book_name[0] and b.author == book_name[1]:
                book = BookSession(self.session,b.id,self.user.user_id)
                break
        if book != None:
            self.books.append(b)
            self.ui_page.AuthorNametextEdit.setText(f"{b.title} - {b.author}")
        else:
            QMessageBox.warning(self, "Oops..", "Something went wrong :(")

        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.count()-1)

        self.ui_page.textEdit.setText(book.book_pages[book.page_number])
        self.ui_page.PageslineEdit.setText(str(book.page_number))
        self.ui_page.closeButton.clicked.connect(self.close_book)

        self.ui_page.nextPageButton.clicked.connect(lambda : self.next_page(book))
        self.ui_page.prevPageButton.clicked.connect(lambda : self.prev_page(book))

    def next_page(self,book):
        if book.page_number<book.book_pages.__len__()-1:
            book.page_number+=1
            book.update_page_number(book.page_number)
            self.ui_page.textEdit.setText(book.book_pages[book.page_number])
            self.ui_page.PageslineEdit.setText(str(book.page_number))

    def prev_page(self,book):
        if book.page_number>0:
            book.page_number-=1
            book.update_page_number(book.page_number)
            self.ui_page.textEdit.setText(book.book_pages[book.page_number])
            self.ui_page.PageslineEdit.setText(str(book.page_number))


    def close_book(self):
        book_name = self.ui_page.AuthorNametextEdit.toPlainText().split(" - ")
        book_name[0] = book_name[0].replace('"', '')
        book_name[1] = book_name[1]
        for book in self.books:
            if book.title == book_name[0] and book.author == book_name[1]:
                self.books.remove(book)
                break
        current_index = self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.removeTab(current_index)



    def load_users_things(self):
        library_model=QStandardItemModel()
        for book in self.user.get_other_books(): ##?
            item=QStandardItem(f"\"{book.title}\" - {book.author}")
            library_model.appendRow(item)
        self.ui.FoundBookslistView.setModel(library_model)
        self.ui.FoundBookslistView.setSelectionMode(QListView.ExtendedSelection)

        mybooks_model = QStandardItemModel()
        for book in self.user.get_user_books():  ##?
            item = QStandardItem(f"\"{book.title}\" - {book.author}")
            mybooks_model.appendRow(item)
        self.ui.MyBookslistView.setModel(mybooks_model)
        self.ui.MyBookslistView.setSelectionMode(QListView.ExtendedSelection)

        quotes_model = QStandardItemModel()
        for quote in self.user.get_user_quotes():  ##?
            item = QStandardItem(f"\"{quote.quote}\"")
            quotes_model.appendRow(item)
        self.ui.FavoritelistView.setModel(quotes_model)
        self.ui.FavoritelistView.setSelectionMode(QListView.ExtendedSelection)

        #buttons
        self.ui.addBookButton.clicked.connect(self.add_book)
        self.ui.delMyBookButton.clicked.connect(self.delete_book)
        self.ui.readMyBookButton.clicked.connect(self.open_book)


    def delete_book(self):
        library_model = self.ui.FoundBookslistView.model()
        selected_indexes = self.ui.MyBookslistView.selectedIndexes()
        if not selected_indexes:
            return
        my_books_model = self.ui.MyBookslistView.model()
        book_item = self.ui.MyBookslistView.model().itemFromIndex(selected_indexes[0])
        book_name = book_item.text().split(" - ")
        book_name[0] = book_name[0].replace('"', '')
        book_name[1] = book_name[1]
        print(book_name)

        """
        тут будет бред коня, поиск по не своим книгам
        """
        book = None
        for b in self.user.get_user_books():
            if b.title == book_name[0] and b.author == book_name[1]:
                book = b
                break
        if book != None:
            for connection in b.connections:
                if connection.book_id==b.id and self.user.user_id==connection.user_id:
                    self.user.remove_connection(book.id)
                    library_model.appendRow(book_item.clone())
                    my_books_model.removeRow(selected_indexes[0].row())
                    break
        else:
            QMessageBox.warning(self, "Oops..", "Something went wrong :(")

        self.ui.MyBookslistView.setModel(my_books_model)
        self.ui.FoundBookslistView.setModel(library_model)
    def add_book(self):
        library_model=self.ui.FoundBookslistView.model()
        selected_indexes = self.ui.FoundBookslistView.selectedIndexes()
        if not selected_indexes:
            return
        my_books_model = self.ui.MyBookslistView.model()
        book_item = self.ui.FoundBookslistView.model().itemFromIndex(selected_indexes[0])
        book_name=book_item.text().split(" - ")
        book_name[0]=book_name[0].replace('"','')
        book_name[1]=book_name[1]
        print(book_name)

        """
        тут будет бред коня, поиск по не своим книгам
        """
        book=None
        for b in self.user.get_other_books():
            if b.title==book_name[0] and b.author==book_name[1]:
                book=b
                break
        if book!=None:
            self.user.add_connection(book.id)
            book_session = BookSession(self.session, book.id,self.user.user_id)

            book_item = QStandardItem(f"\"{book.title}\" - {book.author}")
            my_books_model.appendRow(book_item)
            library_model.removeRow(selected_indexes[0].row())
        else:
            QMessageBox.warning(self, "Oops..", "Something went wrong :(")

        self.ui.MyBookslistView.setModel(my_books_model)
        self.ui.FoundBookslistView.setModel(library_model)

    def open_context_menu(self,pos):
        copy_action = QAction("Copy", self)
        translate_action = QAction("Translate", self)
        wikipedia_action = QAction("Wikipedia", self)

        # Connect the actions to their respective slots/methods
        copy_action.triggered.connect(self.copy_text)
        translate_action.triggered.connect(self.translate_text)
        wikipedia_action.triggered.connect(self.open_wikipedia)

        # Create the context menu
        context_menu = QMenu(self)
        context_menu.addAction(copy_action)
        context_menu.addAction(translate_action)
        context_menu.addAction(wikipedia_action)

        # Show the context menu at the requested position
        context_menu.exec_(self.ui_page.textEdit.mapToGlobal(pos))

    def copy_text(self):
        selected_text = self.ui_page.textEdit.textCursor().selectedText()

    def translate_text(self):
        selected_text = self.ui_page.textEdit.textCursor().selectedText()

    def open_wikipedia(self):
        selected_text = self.ui_page.textEdit.textCursor().selectedText()


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