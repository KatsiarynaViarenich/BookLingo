# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NotLoged.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_NotLogedMainWindow(object):
    def setupUi(self, NotLogedMainWindow):
        if not NotLogedMainWindow.objectName():
            NotLogedMainWindow.setObjectName(u"NotLogedMainWindow")
        NotLogedMainWindow.resize(800, 600)
        NotLogedMainWindow.setStyleSheet(u"background-color: #faf5ea;\n"
"")
        self.centralwidget = QWidget(NotLogedMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 71, 601))
        self.frame.setStyleSheet(u"background-color: #f5e6c6;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.KontoButton = QPushButton(self.frame)
        self.KontoButton.setObjectName(u"KontoButton")
        self.KontoButton.setGeometry(QRect(0, 0, 71, 71))
        self.KontoButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        icon = QIcon()
        iconThemeName = u"user-desktop"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../Python/Projects/venv/Lib/site-packages/PySide6", QSize(), QIcon.Normal, QIcon.Off)

        self.KontoButton.setIcon(icon)
        self.MyBooksButton = QPushButton(self.frame)
        self.MyBooksButton.setObjectName(u"MyBooksButton")
        self.MyBooksButton.setGeometry(QRect(0, 140, 71, 71))
        self.MyBooksButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.FindButton = QPushButton(self.frame)
        self.FindButton.setObjectName(u"FindButton")
        self.FindButton.setGeometry(QRect(0, 210, 71, 71))
        self.FindButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.FavoriteButton = QPushButton(self.frame)
        self.FavoriteButton.setObjectName(u"FavoriteButton")
        self.FavoriteButton.setGeometry(QRect(0, 70, 71, 71))
        self.FavoriteButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.ExitButton = QPushButton(self.frame)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setGeometry(QRect(0, 530, 71, 71))
        self.ExitButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.HelpButton = QPushButton(self.frame)
        self.HelpButton.setObjectName(u"HelpButton")
        self.HelpButton.setGeometry(QRect(0, 460, 71, 71))
        self.HelpButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(140, 200, 571, 71))
        self.textEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(140, 310, 571, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.LogOutButton = QPushButton(self.frame_2)
        self.LogOutButton.setObjectName(u"LogOutButton")
        self.LogOutButton.setGeometry(QRect(10, 20, 231, 41))
        self.LogOutButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none; background-color: #f5e6c6;\n"
" font-size: 14px;")
        self.LogOutButton_2 = QPushButton(self.frame_2)
        self.LogOutButton_2.setObjectName(u"LogOutButton_2")
        self.LogOutButton_2.setGeometry(QRect(330, 20, 231, 41))
        self.LogOutButton_2.setStyleSheet(u"    border: none;\n"
"    box-shadow: none; background-color: #f5e6c6;\n"
" font-size: 14px;")
        NotLogedMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NotLogedMainWindow)

        QMetaObject.connectSlotsByName(NotLogedMainWindow)
    # setupUi

    def retranslateUi(self, NotLogedMainWindow):
        NotLogedMainWindow.setWindowTitle(QCoreApplication.translate("NotLogedMainWindow", u"Login", None))
        self.KontoButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"L", None))
        self.MyBooksButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"MyBooks", None))
        self.FindButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"Find", None))
        self.FavoriteButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"Fav", None))
        self.ExitButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"Exit", None))
        self.HelpButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"Help", None))
        self.textEdit.setHtml(QCoreApplication.translate("NotLogedMainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Until you </span><span style=\" font-size:12pt; color:#000000;\">log in</span><span style=\" font-size:12pt;\">, you won't be able to read our books :( </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Please </span><"
                        "span style=\" font-size:12pt; font-weight:700; font-style:italic;\">log in</span><span style=\" font-size:12pt;\"> or </span><span style=\" font-size:12pt; font-weight:700; font-style:italic; color:#000000;\">register</span><span style=\" font-size:12pt;\"> if you don't have an account.</span></p></body></html>", None))
        self.LogOutButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"Log In", None))
        self.LogOutButton_2.setText(QCoreApplication.translate("NotLogedMainWindow", u"Register", None))
    # retranslateUi

