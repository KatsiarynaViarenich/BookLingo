# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogInWindow(pass).ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QTextEdit, QWidget)


class Ui_LoginPageMainWindow(object):
    def setupUi(self, NotLogedMainWindow):
        if not NotLogedMainWindow.objectName():
            NotLogedMainWindow.setObjectName("NotLogedMainWindow")
        NotLogedMainWindow.resize(800, 600)
        NotLogedMainWindow.setStyleSheet("background-color: #faf5ea;\n" "")
        self.centralwidget = QWidget(NotLogedMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(120, 420, 541, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.LogInButton = QPushButton(self.frame_2)
        self.LogInButton.setObjectName("LogOutButton")
        self.LogInButton.setGeometry(QRect(30, 20, 211, 41))
        self.LogInButton.setStyleSheet(
            "    border: none;\n"
            "    box-shadow: none; background-color: #f5e6c6;\n"
            " font-size: 14px;"
        )
        self.RegisterButton = QPushButton(self.frame_2)
        self.RegisterButton.setObjectName("LogOutButton_2")
        self.RegisterButton.setGeometry(QRect(290, 20, 211, 41))
        self.RegisterButton.setStyleSheet(
            "    border: none;\n"
            "    box-shadow: none; background-color: #f5e6c6;\n"
            " font-size: 14px;"
        )
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(120, 100, 541, 281))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.loginLine = QLineEdit(self.frame)
        self.loginLine.setObjectName("lineEdit")
        self.loginLine.setGeometry(QRect(150, 140, 371, 31))
        self.passLine = QLineEdit(self.frame)
        self.passLine.setObjectName("lineEdit_2")
        self.passLine.setGeometry(QRect(150, 190, 371, 31))
        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 140, 121, 87))
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setGeometry(QRect(20, 10, 491, 87))

        self.retranslateUi(NotLogedMainWindow)

        QMetaObject.connectSlotsByName(NotLogedMainWindow)

    # setupUi

    def retranslateUi(self, NotLogedMainWindow):
        NotLogedMainWindow.setWindowTitle(
            QCoreApplication.translate("LoginPageMainWindow", "Login", None)
        )
        self.LogInButton.setText(
            QCoreApplication.translate("LoginPageMainWindow", "Log In", None)
        )
        self.RegisterButton.setText(
            QCoreApplication.translate("NotLogedMainWindow", "Register", None)
        )
        self.textEdit_2.setHtml(
            QCoreApplication.translate(
                "NotLogedMainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="right" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">Login</span></p>\n'
                '<p align="right" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;"><br /></p>\n'
                '<p align="right" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">Password</span></p></body></html>',
                None,
            )
        )
        self.textEdit.setHtml(
            QCoreApplication.translate(
                "NotLogedMainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; font-size:12pt; text-indent:0px;">Write your login or e-mail and password or press register, if you have no account.</p></body></html>',
                None,
            )
        )

    # retranslateUi
