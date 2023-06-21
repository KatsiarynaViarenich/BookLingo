# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Favourite.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QListView, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_FavouriteMainWindow(object):
    def setupUi(self, FavoriteMainWindow):
        if not FavoriteMainWindow.objectName():
            FavoriteMainWindow.setObjectName(u"FavoriteMainWindow")
        FavoriteMainWindow.resize(800, 601)
        FavoriteMainWindow.setStyleSheet(u"background-color: #faf5ea;\n"
"  ")
        self.centralwidget = QWidget(FavoriteMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 71, 601))
        self.frame.setStyleSheet(u"background-color: #f5e6c6;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.KontoButton_3 = QPushButton(self.frame)
        self.KontoButton_3.setObjectName(u"KontoButton_3")
        self.KontoButton_3.setGeometry(QRect(0, 0, 71, 71))
        self.KontoButton_3.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        icon = QIcon()
        iconThemeName = u"user-desktop"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../Python/Projects/venv/Lib/site-packages/PySide6", QSize(), QIcon.Normal, QIcon.Off)

        self.KontoButton_3.setIcon(icon)
        self.MyBooksButton_3 = QPushButton(self.frame)
        self.MyBooksButton_3.setObjectName(u"MyBooksButton_3")
        self.MyBooksButton_3.setGeometry(QRect(0, 140, 71, 71))
        self.MyBooksButton_3.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.FindButton_3 = QPushButton(self.frame)
        self.FindButton_3.setObjectName(u"FindButton_3")
        self.FindButton_3.setGeometry(QRect(0, 210, 71, 71))
        self.FindButton_3.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.FavoriteButton_3 = QPushButton(self.frame)
        self.FavoriteButton_3.setObjectName(u"FavoriteButton_3")
        self.FavoriteButton_3.setGeometry(QRect(0, 70, 71, 71))
        self.FavoriteButton_3.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.ExitButton_3 = QPushButton(self.frame)
        self.ExitButton_3.setObjectName(u"ExitButton_3")
        self.ExitButton_3.setGeometry(QRect(0, 530, 71, 71))
        self.ExitButton_3.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.HelpButton_3 = QPushButton(self.frame)
        self.HelpButton_3.setObjectName(u"HelpButton_3")
        self.HelpButton_3.setGeometry(QRect(0, 460, 71, 71))
        self.HelpButton_3.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.FavoritelistView = QListView(self.centralwidget)
        self.FavoritelistView.setObjectName(u"FavoritelistView")
        self.FavoritelistView.setGeometry(QRect(100, 100, 651, 471))
        self.FavoritelistView.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.FavoritetextEdit = QTextEdit(self.centralwidget)
        self.FavoritetextEdit.setObjectName(u"FavoritetextEdit")
        self.FavoritetextEdit.setGeometry(QRect(80, 0, 671, 51))
        self.FavoritetextEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.findFavoriteplainTextEdit = QPlainTextEdit(self.centralwidget)
        self.findFavoriteplainTextEdit.setObjectName(u"findFavoriteplainTextEdit")
        self.findFavoriteplainTextEdit.setGeometry(QRect(100, 60, 651, 31))
        FavoriteMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FavoriteMainWindow)

        QMetaObject.connectSlotsByName(FavoriteMainWindow)
    # setupUi

    def retranslateUi(self, FavoriteMainWindow):
        FavoriteMainWindow.setWindowTitle(QCoreApplication.translate("FavoriteMainWindow", u"Favourite", None))
        self.KontoButton_3.setText(QCoreApplication.translate("FavoriteMainWindow", u"L", None))
        self.MyBooksButton_3.setText(QCoreApplication.translate("FavoriteMainWindow", u"MyBooks", None))
        self.FindButton_3.setText(QCoreApplication.translate("FavoriteMainWindow", u"Find", None))
        self.FavoriteButton_3.setText(QCoreApplication.translate("FavoriteMainWindow", u"Fav", None))
        self.ExitButton_3.setText(QCoreApplication.translate("FavoriteMainWindow", u"Exit", None))
        self.HelpButton_3.setText(QCoreApplication.translate("FavoriteMainWindow", u"Help", None))
        self.FavoritetextEdit.setHtml(QCoreApplication.translate("FavoriteMainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; font-style:italic;\">Favourite</span></p></body></html>", None))
    # retranslateUi

