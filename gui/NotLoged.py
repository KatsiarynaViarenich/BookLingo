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
        self.LogInButton = QPushButton(self.frame_2)
        self.LogInButton.setObjectName(u"LogInButton")
        self.LogInButton.setGeometry(QRect(10, 20, 231, 41))
        self.LogInButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none; background-color: #f5e6c6;\n"
" font-size: 14px;")
        self.RegisterButton = QPushButton(self.frame_2)
        self.RegisterButton.setObjectName(u"RegisterButton")
        self.RegisterButton.setGeometry(QRect(330, 20, 231, 41))
        self.RegisterButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none; background-color: #f5e6c6;\n"
" font-size: 14px;")


        self.retranslateUi(NotLogedMainWindow)

        QMetaObject.connectSlotsByName(NotLogedMainWindow)
    # setupUi

    def retranslateUi(self, NotLogedMainWindow):
        NotLogedMainWindow.setWindowTitle(QCoreApplication.translate("NotLogedMainWindow", u"Login", None))

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
        self.LogInButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"Log In", None))
        self.RegisterButton.setText(QCoreApplication.translate("NotLogedMainWindow", u"Register", None))
    # retranslateUi

