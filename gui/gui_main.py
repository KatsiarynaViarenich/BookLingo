import sys
from functools import partial
from Loged import Ui_LogedQMainWindow
from LoginWindow import Ui_LoginPageMainWindow
from new_vision import Ui_MainWindow
from NotLoged import Ui_NotLogedMainWindow
from Page import Ui_PageMainWindow
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, \
    QListWidgetItem, QMessageBox, QListView, QMenu, QToolTip
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListView,
                               QListWidgetItem, QMainWindow, QMessageBox,
                               QPushButton, QVBoxLayout, QWidget)
from RegisterWindow import Ui_RegisterQMainWindow
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from services.authorizing_process import AuthorizingProcess
from scripts.run_setup import User,Book,Quote,Base
from PySide6.QtGui import QStandardItem, QStandardItemModel, QContextMenuEvent, QAction, Qt, QCursor

from modules.phrase_translation import PhraseTranslation
from services.book_session import BookSession
from services.user_session import UserSession
from modules import fancy_words_generator
from modules import wikipedia_search
from modules.question_generator import QuestionGenerator



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.user = None

        engine = create_engine("sqlite:///../data/app.db")
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.ap = AuthorizingProcess(self.session)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_page=Ui_PageMainWindow()
        self.books=[]
        self.ui_page = Ui_PageMainWindow()

        self.ui_loged = Ui_LogedQMainWindow()
        self.ui_notloged = Ui_NotLogedMainWindow()
        self.ui_logPage = Ui_LoginPageMainWindow()
        self.ui_register = Ui_RegisterQMainWindow()

        self.ui_log = self.ui_notloged

        self.account_buttons()
        self.ui.tabWidget.currentChanged.connect(self.open_tab)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui_page.setupUi(self)

    def open_tab(self, index):
        if self.ui_log == self.ui_logPage or self.ui_log == self.ui_register:
            if index not in [0, 1]:
                self.logOut()
                self.ui.tabWidget.setCurrentIndex(0)
        elif self.ui_log == self.ui_notloged:
            if index not in [0, 1]:
                QMessageBox.warning(
                    self, "Oops...", "You're not logged.\nGo to Accounts."
                )
                self.ui.tabWidget.setCurrentIndex(0)
            else:
                self.ui.tabWidget.setCurrentIndex(index)
        if self.ui.tabWidget.count()==6:
            self.ui.readMyBookButton.setEnabled(False)
        else:
            self.ui.readMyBookButton.setEnabled(True)



    def account_buttons(self):
        if self.ui_log == self.ui_loged:
            self.logIn()
        else:
            self.logOut()

    def logInPage(self):
        tab_index = 1
        self.ui.tabWidget.removeTab(tab_index)
        self.ui.tab_account = QWidget()
        self.ui.tabWidget.insertTab(tab_index, self.ui.tab_account, "Login")
        self.ui_log = self.ui_logPage

        self.ui_log.setupUi(self.ui.tab_account)
        self.ui_log.LogInButton.clicked.connect(self.authorization_login)
        self.ui_log.RegisterButton.clicked.connect(self.registerPage)

        self.ui.tabWidget.setCurrentIndex(tab_index)

    def authorization_login(self):
        # you're in loginpage
        username = self.ui_log.loginLine.text()
        password = self.ui_log.passLine.text()
        message = self.ap.log_in(username, password)

        if message != "Login successful":
            self.logInPage()
            QMessageBox.warning(self, "Authorizing", message)
        else:
            self.user = UserSession(
                self.session,
                self.session.query(User).filter_by(name=username).first().id,
            )
            self.load_users_things()
            print(f"{username},{password}")
            self.logIn()

    def authorization_create_acc(self):
        username = self.ui_log.loginLine.text()
        password = self.ui_log.passLine.text()
        message = self.ap.create_new_account(username, password)

        if message != "Account created successfully":
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

        html_text = QCoreApplication.translate(
            "",
            '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">'
            '<html><head><meta name="qrichtext" content="1" /><style type="text/css">'
            "p, li { white-space: pre-wrap; }"
            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">"
            '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">Dear </span><span style=" font-size:14pt; font-weight:600; font-style:italic;">User</span><span style=" font-size:14pt; font-weight:600;">,</span></p>'
            '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"></p>'
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Feel free to browse through our library, add books to your library or favorite quotes. We hope you have a delightful reading experience with BookLingo.</span></p></body></html>',
        )
        html_text = html_text.replace(
            '<span style=" font-size:14pt; font-weight:600; font-style:italic;">User</span>',
            f'<span style=" font-size:14pt; font-weight:600; font-style:italic;">{self.session.query(User).filter_by(id=self.user.user_id).first().name}</span>',
        )

        self.ui_log.HelloUserQTextEdit.setHtml(html_text)
        self.ui.tabWidget.setCurrentIndex(tab_index)

    def logOut(self):
        if self.user != None:
            self.load_users_things()
            for index in range(self.ui.tabWidget.count(), 5, -1):
                self.ui.tabWidget.removeTab(index - 1)
            self.books = []
            self.user = None
        tab_index = 1
        self.ui.tabWidget.removeTab(tab_index)
        self.ui.tab_account = QWidget()
        self.ui.tabWidget.insertTab(tab_index, self.ui.tab_account, "Account")
        self.ui_log = self.ui_notloged
        self.ui_log.setupUi(self.ui.tab_account)
        self.ui_log.LogInButton.clicked.connect(self.logInPage)
        self.ui_log.RegisterButton.clicked.connect(self.registerPage)
        self.ui.tabWidget.setCurrentIndex(tab_index)

        self.ui.tabWidget.setCurrentIndex(tab_index)

    def open_book(self):
        selected_indexes = self.ui.MyBookslistView.selectedIndexes()
        if not selected_indexes:
            return
        book_session_item = self.ui.MyBookslistView.model().itemFromIndex(selected_indexes[0])
        book_session_obj = book_session_item.data()
        page_widget = QWidget()
        self.ui_page.setupUi(page_widget)
        self.ui.tabWidget.addTab(page_widget, book_session_item.text())

        self.books.append(book_session_item)
        self.ui_page.AuthorNametextEdit.setText(book_session_item.text())
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.count() - 1)

        self.ui_page.textEdit.setText(book_session_obj.book_pages[book_session_obj.page_number])
        self.ui_page.PageslineEdit.setText(str(book_session_obj.page_number))
        self.ui_page.closeButton.clicked.connect(self.close_book)

        self.ui_page.nextPageButton.clicked.connect(lambda : self.next_page(book_session_obj))
        self.ui_page.prevPageButton.clicked.connect(lambda : self.prev_page(book_session_obj))
        self.ui_page.questionsButton.clicked.connect(self.check_understanding)
        self.ui_page.addQuoteButton.clicked.connect(lambda :self.add_quote(book_session_obj))
        self.ui.delMyQuoteButton.clicked.connect(self.delete_quote)
        self.ui_page.translateButton.clicked.connect(self.translate_text)
        self.ui_page.wikipediaButton.clicked.connect(self.open_wikipedia)

    def next_page(self,book):
        if book.page_number<book.book_pages.__len__()-1:
            print(str(book.page_number))
            book.page_number= book.page_number+1
            self.ui_page.textEdit.setText(book.book_pages[book.page_number])
            self.ui_page.PageslineEdit.setText(str(book.page_number))
            print(book.page_number)


    def prev_page(self,book):
        if book.page_number>0:
            book.page_number=book.page_number-1
            book.update_page_number(book.page_number)
            self.ui_page.textEdit.setText(book.book_pages[book.page_number])
            self.ui_page.PageslineEdit.setText(str(book.page_number))


    def next_page(self, book):
        book_name = self.ui_page.AuthorNametextEdit.toPlainText()
        for book in self.books:
            if book_name == book.text():
                book=book.data()
                book.page_number+=1
                book.update_page_number(book.page_number)
                self.ui_page.textEdit.setText(book.book_pages[book.page_number])
                self.ui_page.PageslineEdit.setText(book.page_number)

    def prev_page(self, book):
        book_name = self.ui_page.AuthorNametextEdit.toPlainText()
        for book in self.books:
            if book_name==book.text():
                book=book.data()
                book.page_number-=1
                self.ui_page.textEdit.setText(book.book_pages[book.page_number])
                self.ui_page.PageslineEdit.setText(str(book.page_number))

    def close_book(self):
        book_name = self.ui_page.AuthorNametextEdit.toPlainText()
        for book in self.books:
            if book.text() == book_name:
                book.update_page_number(book.page_number)
                self.books.remove(book)
                break
        current_index = self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.removeTab(current_index)

    def load_users_things(self):
        library_model = QStandardItemModel()
        for book in self.user.get_other_books():  ##?
            item = QStandardItem()
            item.setData(book)
            item.setText(f"\'{book.title}\' - {book.author}")
            library_model.appendRow(item)
        self.ui.FoundBookslistView.setModel(library_model)
        self.ui.FoundBookslistView.setSelectionMode(QListView.ExtendedSelection)

        mybooks_model = QStandardItemModel()
        for book in self.user.get_user_books():
            book_session=BookSession(self.session,book.id,self.user.user_id)
            item = QStandardItem()
            item.setData(book_session)
            item.setText(f'"{book.title}" - {book.author}')
            mybooks_model.appendRow(item)
        self.ui.MyBookslistView.setModel(mybooks_model)
        self.ui.MyBookslistView.setSelectionMode(QListView.ExtendedSelection)

        quotes_model = QStandardItemModel()
        for quote in self.user.get_user_quotes():  ##?
            item = QStandardItem()
            item.setData(quote)
            item.setText(f"\'{quote[2]}\' - {quote[1]}, {quote[0]}")
            quotes_model.appendRow(item)
        self.ui.FavoritelistView.setModel(quotes_model)
        self.ui.FavoritelistView.setSelectionMode(QListView.ExtendedSelection)

        # buttons
        self.ui.addBookButton.clicked.connect(self.add_book)
        self.ui.delMyBookButton.clicked.connect(self.delete_book)
        self.ui.readMyBookButton.clicked.connect(self.open_book)
        self.ui.delMyQuoteButton.clicked.connect(self.delete_quote)

    def delete_book(self):
        library_model = self.ui.FoundBookslistView.model()
        selected_indexes = self.ui.MyBookslistView.selectedIndexes()
        if not selected_indexes:
            return
        my_books_model = self.ui.MyBookslistView.model()
        book_session_item = self.ui.MyBookslistView.model().itemFromIndex(selected_indexes[0]).data()
        self.user.remove_connection(book_session_item.book_id)

        books = self.user.get_user_books()
        for book in books:
            if book.id==book_session_item.book_id:
                book_item=QStandardItem()
                book_item.setData(book)
                book_item.setText(f"\'{book.title}\' - {book.author}")
                self.user.remove_connection(book.id)
                library_model.appendRow(book_item)
                break

        my_books_model.removeRow(selected_indexes[0].row())

        self.ui.MyBookslistView.setModel(my_books_model)
        self.ui.FoundBookslistView.setModel(library_model)

    def add_book(self):
        library_model = self.ui.FoundBookslistView.model()
        selected_indexes = self.ui.FoundBookslistView.selectedIndexes()
        if not selected_indexes:
            return
        my_books_model = self.ui.MyBookslistView.model()
        book_item = self.ui.FoundBookslistView.model().itemFromIndex(selected_indexes[0]).data()

        self.user.add_connection(book_item.id)
        book_session = BookSession(self.session, book_item.id, self.user.user_id)
        book_session_item = QStandardItem()
        book_session_item.setData(book_session)
        book_session_item.setText(f"\'{book_item.title}\' - {book_item.author}")
        my_books_model.appendRow(book_session_item)
        library_model.removeRow(selected_indexes[0].row())
        self.ui.MyBookslistView.setModel(my_books_model)
        self.ui.FoundBookslistView.setModel(library_model)


    def translate_text(self):
        selected_text = self.ui_page.textEdit.textCursor().selectedText()
        from modules.phrase_translation import PhraseTranslation
        PhraseTranslation_obj = PhraseTranslation()
        translation = PhraseTranslation_obj.get_translation(selected_text)
        QMessageBox.warning(self,"Translation",f"{selected_text} - {translation}")

    def open_wikipedia(self):
        selected_text = self.ui_page.textEdit.textCursor().selectedText()
        result=wikipedia_search.search_wikipedia(selected_text)
        QMessageBox.warning(self,"Wikipedia",f"{result}")


    def add_quote(self,book):
        selected_text = self.ui_page.textEdit.textCursor().selectedText()
        book.add_quote(selected_text)

        quote_model = self.ui.FavoritelistView.model()

        item = QStandardItem(selected_text)
        quote_model.appendRow(item)

        self.ui.FavoritelistView.setModel(quote_model)
        self.ui.FavoritelistView.setSelectionMode(QListView.ExtendedSelection)

    def delete_quote(self):
        quote_model = self.ui.FavoritelistView.model()
        selected_indexes = self.ui.MyBookslistView.selectedIndexes()
        if not selected_indexes:
            return
        quote_model.removeRow(selected_indexes[0].row())
        self.user.remove_quotes()
        self.ui.FavoritelistView.setModel(quote_model)


    def check_understanding(self):
        selected_text = self.ui_page.textEdit.toPlainText()
        print(selected_text)
        QMessageBox.information(self, "Hey", f"Questions:\n{QuestionGenerator.generate_questions(selected_text)}\nFancy words:\n {(fancy_words_generator.get_fancy_words(selected_text))}")


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
