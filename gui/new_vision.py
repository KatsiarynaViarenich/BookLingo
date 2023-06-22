# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_vision.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QListView, QMainWindow,
                               QPlainTextEdit, QPushButton, QSizePolicy,
                               QTabWidget, QTextEdit, QWidget, QAbstractItemView)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 598)
        MainWindow.setStyleSheet("background: #f5e6c6 \n" "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 789, 599))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet("background: #f5e6c6 \n" "")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(30, 30))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_home = QWidget()
        self.tab_home.setObjectName("home")
        self.HelloQText = QTextEdit(self.tab_home)
        self.HelloQText.setReadOnly(True)
        self.HelloQText.setObjectName("HelloQText")
        self.HelloQText.setGeometry(QRect(100, 100, 571, 341))
        self.HelloQText.setAutoFillBackground(False)
        self.HelloQText.setStyleSheet("")
        self.tabWidget.addTab(self.tab_home, "")
        self.tab_account = QWidget()
        self.tab_account.setObjectName("account page")
        self.tabWidget.addTab(self.tab_account, "")
        self.tab_fav = QWidget()
        self.tab_fav.setObjectName("favourites")
        self.findFavoriteplainTextEdit = QPlainTextEdit(self.tab_fav)
        self.findFavoriteplainTextEdit.setObjectName("findFavoriteplainTextEdit")
        self.findFavoriteplainTextEdit.setGeometry(QRect(70, 60, 551, 31))
        self.findFavoriteplainTextEdit.setStyleSheet(
            "background: #faf5ea;\n" "  box-shadow: none;"
        )

        self.findQuoteButton = QPushButton(self.tab_fav)
        self.findQuoteButton.setObjectName("findBookButton")
        self.findQuoteButton.setGeometry(QRect(640, 60, 70, 31))
        self.findQuoteButton.setStyleSheet(
            "  box-shadow: none; background-color: #f5e6c6;\n"
        )

        self.FavoritelistView = QListView(self.tab_fav)
        self.FavoritelistView.setObjectName("FavoritelistView")
        self.FavoritelistView.setGeometry(QRect(70, 100, 651, 381))
        self.FavoritelistView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.FavoritelistView.setStyleSheet(
            "background: #faf5ea;\n" " border: none;\n" "    box-shadow: none;"
        )
        self.FavoritetextEdit = QTextEdit(self.tab_fav)
        self.FavoritetextEdit.setReadOnly(True)
        self.FavoritetextEdit.setObjectName("FavoritetextEdit")
        self.FavoritetextEdit.setGeometry(QRect(50, 10, 671, 41))
        self.FavoritetextEdit.setStyleSheet(" border: none;\n" "    box-shadow: none;")
        self.delMyQuoteButton = QPushButton(self.tab_fav)
        self.delMyQuoteButton.setObjectName("findMyQuoteButton")
        self.delMyQuoteButton.setGeometry(QRect(640, 500, 80, 31))
        self.delMyQuoteButton.setStyleSheet(
            "  box-shadow: none; background-color: #f5e6c6;\n"
        )
        self.tabWidget.addTab(self.tab_fav, "")
        self.tab_mybooks = QWidget()
        self.tab_mybooks.setObjectName("my books")
        self.MyBookslistView = QListView(self.tab_mybooks)
        self.MyBookslistView.setObjectName("MyBookslistView")
        self.MyBookslistView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.MyBookslistView.setGeometry(QRect(70, 100, 651, 381))
        self.MyBookslistView.setStyleSheet(
            "background: #faf5ea;\n" " border: none;\n" "    box-shadow: none;"
        )
        self.findMyBookplainTextEdit = QPlainTextEdit(self.tab_mybooks)
        self.findMyBookplainTextEdit.setObjectName("findMyBookplainTextEdit")
        self.findMyBookplainTextEdit.setGeometry(QRect(70, 60, 551, 31))
        self.findMyBookplainTextEdit.setStyleSheet(
            "background: #faf5ea;\n" "    box-shadow: none;"
        )
        self.MyBookstextEdit = QTextEdit(self.tab_mybooks)
        self.MyBookstextEdit.setReadOnly(True)
        self.MyBookstextEdit.setObjectName("MyBookstextEdit")
        self.MyBookstextEdit.setGeometry(QRect(50, 10, 671, 41))
        self.MyBookstextEdit.setStyleSheet(" border: none;\n" "    box-shadow: none;")
        self.readMyBookButton = QPushButton(self.tab_mybooks)
        self.readMyBookButton.setObjectName("findBookButton")
        self.readMyBookButton.setGeometry(QRect(640, 500, 80, 31))
        self.readMyBookButton.setStyleSheet(
            "  box-shadow: none; background-color: #f5e6c6;\n"
        )

        self.delMyBookButton = QPushButton(self.tab_mybooks)
        self.delMyBookButton.setObjectName("findBookButton")
        self.delMyBookButton.setGeometry(QRect(70, 500, 80, 31))
        self.delMyBookButton.setStyleSheet(
            "  box-shadow: none; background-color: #f5e6c6;\n"
        )

        self.findMyBookButton = QPushButton(self.tab_mybooks)
        self.findMyBookButton.setObjectName("findMyBookButton")
        self.findMyBookButton.setGeometry(QRect(640, 60, 70, 31))
        self.findMyBookButton.setStyleSheet(
            "  box-shadow: none; background-color: #f5e6c6;\n"
        )
        self.tabWidget.addTab(self.tab_mybooks, "")
        self.tab_find = QWidget()
        self.tab_find.setObjectName("home")
        self.FoundBookslistView = QListView(self.tab_find)
        self.FoundBookslistView.setObjectName("FoundBookslistView")
        self.FoundBookslistView.setGeometry(QRect(70, 100, 651, 381))
        self.FoundBookslistView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.FoundBookslistView.setStyleSheet(
            "background: #faf5ea;\n" " border: none;\n" "    box-shadow: none;"
        )
        self.addBookButton = QPushButton(self.tab_find)
        self.addBookButton.setObjectName("findBookButton")
        self.addBookButton.setGeometry(QRect(640, 500, 80, 31))
        self.addBookButton.setStyleSheet(
            "  box-shadow: none; background-color: #f5e6c6;\n"
        )
        self.FindBookstextEdit = QTextEdit(self.tab_find)
        self.FindBookstextEdit.setReadOnly(True)
        self.FindBookstextEdit.setObjectName("FindBookstextEdit")
        self.FindBookstextEdit.setGeometry(QRect(50, 10, 671, 41))
        self.FindBookstextEdit.setStyleSheet(" border: none;\n" "    box-shadow: none;")
        self.findFindBooksplainTextEdit = QPlainTextEdit(self.tab_find)
        self.findFindBooksplainTextEdit.setObjectName("findFindBooksplainTextEdit")
        self.findFindBooksplainTextEdit.setGeometry(QRect(70, 60, 551, 31))
        self.findFindBooksplainTextEdit.setStyleSheet(
            "background: #faf5ea;\n" " border: none;"
        )
        self.findBookButton = QPushButton(self.tab_find)
        self.findBookButton.setObjectName("findBookButton")
        self.findBookButton.setGeometry(QRect(640, 60, 80, 31))
        self.findBookButton.setStyleSheet(
            "  box-shadow: none; background-color: #f5e6c6;\n"
        )
        self.tabWidget.addTab(self.tab_find, "")

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.HelloQText.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt; font-weight:700;">Welcome to BookLingo!</span></p>\n'
                '<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:700;"><br /></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r'
                'ight:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Dive into a world of books, literature, and the art of words. Discover a vast library of captivating novels, non-fiction, and classics. Engage in discussions, share reviews, and join our friendly community of book lovers. Start your literary adventure with BookLingo today!</span></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;"><br /></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p'
                ">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-style:italic; color:#000000;">by Katsiaryna Viaernich and Vera Goriukhina</span></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_home),
            QCoreApplication.translate("MainWindow", "Home", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_account),
            QCoreApplication.translate("MainWindow", "Account", None),
        )
        self.FavoritetextEdit.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; font-weight:700;">Quotes</span></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_fav),
            QCoreApplication.translate("MainWindow", "Quotes", None),
        )
        self.MyBookstextEdit.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; font-weight:700;">My Books</span></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_mybooks),
            QCoreApplication.translate("MainWindow", "My Books", None),
        )
        self.FindBookstextEdit.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; font-weight:700;">Library</span></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_find),
            QCoreApplication.translate("MainWindow", "Library", None),
        )
        self.findBookButton.setText("Find")
        self.findMyBookButton.setText("Find")
        self.findQuoteButton.setText("Find")
        self.addBookButton.setText(("Add"))
        self.delMyBookButton.setText("Delete")
        self.delMyQuoteButton.setText("Delete")
        self.readMyBookButton.setText("Read")

    # retranslateUi
