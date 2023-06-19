# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_PageMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #faf5ea;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.AuthorNametextEdit = QTextEdit(self.centralwidget)
        self.AuthorNametextEdit.setObjectName(u"AuthorNametextEdit")
        self.AuthorNametextEdit.setGeometry(QRect(80, 0, 671, 51))
        self.AuthorNametextEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
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
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 60, 651, 461))
        self.textEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(100, 560, 651, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 10, 41, 24))
        self.pushButton.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        icon1 = QIcon()
        iconThemeName = u"go-next"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../Python/Projects/venv/Lib/site-packages/PySide6", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton.setIcon(icon1)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 10, 41, 24))
        self.pushButton_2.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        icon2 = QIcon()
        iconThemeName = u"go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"../Python/Projects/venv/Lib/site-packages/PySide6", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_2.setIcon(icon2)
        self.PageslineEdit = QLineEdit(self.frame_2)
        self.PageslineEdit.setObjectName(u"PageslineEdit")
        self.PageslineEdit.setGeometry(QRect(270, 10, 113, 21))
        self.PageslineEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(330, 530, 181, 24))
        self.pushButton_3.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reading", None))
        self.AuthorNametextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.KontoButton_3.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.MyBooksButton_3.setText(QCoreApplication.translate("MainWindow", u"MyBooks", None))
        self.FindButton_3.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.FavoriteButton_3.setText(QCoreApplication.translate("MainWindow", u"Fav", None))
        self.ExitButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.HelpButton_3.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.PageslineEdit.setText(QCoreApplication.translate("MainWindow", u"page/page", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Check understanding", None))
    # retranslateUi

