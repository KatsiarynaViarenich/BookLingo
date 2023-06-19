# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_vision.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QListView, QMainWindow, QPlainTextEdit,
    QSizePolicy, QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 598)
        MainWindow.setStyleSheet(u"background: #f5e6c6 \n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 789, 599))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"background: #f5e6c6 \n"
"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(30, 30))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"home")
        self.HelloQText = QTextEdit(self.tab_home)
        self.HelloQText.setReadOnly(True)
        self.HelloQText.setObjectName(u"HelloQText")
        self.HelloQText.setGeometry(QRect(110, 100, 571, 341))
        self.HelloQText.setAutoFillBackground(False)
        self.HelloQText.setStyleSheet(u"")
        self.tabWidget.addTab(self.tab_home, "")
        self.tab_account = QWidget()
        self.tab_account.setObjectName(u"account page")
        self.tabWidget.addTab(self.tab_account, "")
        self.tab_fav = QWidget()
        self.tab_fav.setObjectName(u"favourites")
        self.findFavoriteplainTextEdit = QPlainTextEdit(self.tab_fav)
        self.findFavoriteplainTextEdit.setObjectName(u"findFavoriteplainTextEdit")
        self.findFavoriteplainTextEdit.setGeometry(QRect(70, 60, 651, 31))
        self.findFavoriteplainTextEdit.setStyleSheet(u"background: #faf5ea;\n"
"  box-shadow: none;")
        self.FavoritelistView = QListView(self.tab_fav)
        self.FavoritelistView.setObjectName(u"FavoritelistView")
        self.FavoritelistView.setGeometry(QRect(70, 100, 651, 431))
        self.FavoritelistView.setStyleSheet(u"background: #faf5ea;\n"
" border: none;\n"
"    box-shadow: none;")
        self.FavoritetextEdit = QTextEdit(self.tab_fav)
        self.FavoritetextEdit.setReadOnly(True)
        self.FavoritetextEdit.setObjectName(u"FavoritetextEdit")
        self.FavoritetextEdit.setGeometry(QRect(50, 10, 671, 41))
        self.FavoritetextEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.tabWidget.addTab(self.tab_fav, "")
        self.tab_mybooks = QWidget()
        self.tab_mybooks.setObjectName(u"my books")
        self.MyBookslistView = QListView(self.tab_mybooks)
        self.MyBookslistView.setObjectName(u"MyBookslistView")
        self.MyBookslistView.setGeometry(QRect(70, 100, 651, 431))
        self.MyBookslistView.setStyleSheet(u"background: #faf5ea;\n"
" border: none;\n"
"    box-shadow: none;")
        self.findMyBookplainTextEdit = QPlainTextEdit(self.tab_mybooks)
        self.findMyBookplainTextEdit.setObjectName(u"findMyBookplainTextEdit")
        self.findMyBookplainTextEdit.setGeometry(QRect(70, 60, 651, 31))
        self.findMyBookplainTextEdit.setStyleSheet(u"background: #faf5ea;\n"
"    box-shadow: none;")
        self.MyBookstextEdit = QTextEdit(self.tab_mybooks)
        self.MyBookstextEdit.setReadOnly(True)
        self.MyBookstextEdit.setObjectName(u"MyBookstextEdit")
        self.MyBookstextEdit.setGeometry(QRect(50, 10, 671, 41))
        self.MyBookstextEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.tabWidget.addTab(self.tab_mybooks, "")
        self.tab_find = QWidget()
        self.tab_find.setObjectName(u"home")
        self.FoundBookslistView = QListView(self.tab_find)
        self.FoundBookslistView.setObjectName(u"FoundBookslistView")
        self.FoundBookslistView.setGeometry(QRect(70, 100, 651, 431))
        self.FoundBookslistView.setStyleSheet(u"background: #faf5ea;\n"
" border: none;\n"
"    box-shadow: none;")
        self.FindBookstextEdit = QTextEdit(self.tab_find)
        self.FindBookstextEdit.setReadOnly(True)
        self.FindBookstextEdit.setObjectName(u"FindBookstextEdit")
        self.FindBookstextEdit.setGeometry(QRect(50, 10, 671, 41))
        self.FindBookstextEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.findFindBooksplainTextEdit = QPlainTextEdit(self.tab_find)
        self.findFindBooksplainTextEdit.setObjectName(u"findFindBooksplainTextEdit")
        self.findFindBooksplainTextEdit.setGeometry(QRect(70, 60, 651, 31))
        self.findFindBooksplainTextEdit.setStyleSheet(u"background: #faf5ea;\n"
" border: none;")
        self.tabWidget.addTab(self.tab_find, "")

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HelloQText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">Welcome to BookLingo!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Dive into a world of books, literature, and the art of words. Discover a vast library of captivating novels, non-fiction, and classics. Engage in discussions, share reviews, and join our friendly community of book lovers. Start your literary adventure with BookLingo today!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p"
                        ">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">by Katsiaryna Viaernich and Vera Goriukhina</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_account), QCoreApplication.translate("MainWindow", u"Account", None))
        self.FavoritetextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Favourite</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fav), QCoreApplication.translate("MainWindow", u"Favourites", None))
        self.MyBookstextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">My Books</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mybooks), QCoreApplication.translate("MainWindow", u"My Books", None))
        self.FindBookstextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Library</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_find), QCoreApplication.translate("MainWindow", u"Find", None))
    # retranslateUi

