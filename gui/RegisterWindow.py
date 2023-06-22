# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterWindow(pass).ui'
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


class Ui_RegisterQMainWindow(object):
    def setupUi(self, RegisterQMainWindow):
        if not RegisterQMainWindow.objectName():
            RegisterQMainWindow.setObjectName("RegisterQMainWindow")
        RegisterQMainWindow.resize(800, 600)
        RegisterQMainWindow.setStyleSheet("background-color: #faf5ea;\n" "")
        self.centralwidget = QWidget(RegisterQMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(120, 420, 541, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.RegisterButton = QPushButton(self.frame_2)
        self.RegisterButton.setObjectName("LogOutButton")
        self.RegisterButton.setGeometry(QRect(130, 20, 261, 41))
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
        self.loginLine.setGeometry(QRect(150, 170, 371, 31))
        self.passLine = QLineEdit(self.frame)
        self.passLine.setObjectName("lineEdit_2")
        self.passLine.setGeometry(QRect(150, 220, 371, 31))
        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 170, 121, 87))
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QRect(20, 10, 501, 131))

        self.retranslateUi(RegisterQMainWindow)

        QMetaObject.connectSlotsByName(RegisterQMainWindow)

    # setupUi

    def retranslateUi(self, RegisterQMainWindow):
        RegisterQMainWindow.setWindowTitle(
            QCoreApplication.translate("RegisterQMainWindow", "Login", None)
        )
        self.RegisterButton.setText(
            QCoreApplication.translate("RegisterQMainWindow", "Register", None)
        )
        self.textEdit_2.setHtml(
            QCoreApplication.translate(
                "RegisterQMainWindow",
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
        self.textEdit_2.setReadOnly(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setHtml(
            QCoreApplication.translate(
                "RegisterQMainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt; font-weight:600;">Welcome</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;"><br />Write your unique login or e-mail and a hard password (min. 8 symbols).</span></p></body></html>',
                None,
            )
        )

    # retranslateUi
