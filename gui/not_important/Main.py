# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
                               QSizePolicy, QTabWidget, QTextEdit, QWidget)


class Ui_StartMainWindow(object):
    def setupUi(self, StartMainWindow):
        if not StartMainWindow.objectName():
            StartMainWindow.setObjectName("StartMainWindow")
        StartMainWindow.resize(800, 600)
        StartMainWindow.setStyleSheet(
            "background-color: #faf5ea;\n" "   border: none;\n  box-shadow: none;"
        )
        self.centralwidget = QTabWidget(StartMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setTabPosition(QTabWidget.West)
        self.helloWidget = QWidget()
        self.HelloQText = QTextEdit(self.helloWidget)
        self.HelloQText.setObjectName("HelloQText")
        self.HelloQText.setGeometry(QRect(110, 100, 571, 341))
        self.HelloQText.setAutoFillBackground(False)
        self.HelloQText.setStyleSheet("")
        self.findWidget = QWidget()
        self.centralwidget.addTab(self.helloWidget, "Home")
        self.centralwidget.addTab(self.findWidget, "find")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 0, 71, 601))
        self.frame.setStyleSheet("background-color: #f5e6c6;\n" "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.KontoButton = QPushButton(self.frame)
        self.KontoButton.setObjectName("KontoButton")
        self.KontoButton.setGeometry(QRect(0, 0, 71, 71))
        self.KontoButton.setStyleSheet("    border: none;\n" "    box-shadow: none;")
        icon = QIcon(QIcon.fromTheme("user-desktop"))
        self.KontoButton.setIcon(icon)
        self.MyBooksButton = QPushButton(self.frame)
        self.MyBooksButton.setObjectName("MyBooksButton")
        self.MyBooksButton.setGeometry(QRect(0, 140, 71, 71))
        self.MyBooksButton.setStyleSheet("    border: none;\n" "    box-shadow: none;")
        self.FindButton = QPushButton(self.frame)
        self.FindButton.setObjectName("FindButton")
        self.FindButton.setGeometry(QRect(0, 210, 71, 71))
        self.FindButton.setStyleSheet("    border: none;\n" "    box-shadow: none;")
        self.FavoriteButton = QPushButton(self.frame)
        self.FavoriteButton.setObjectName("FavoriteButton")
        self.FavoriteButton.setGeometry(QRect(0, 70, 71, 71))
        self.FavoriteButton.setStyleSheet("    border: none;\n" "    box-shadow: none;")
        self.ExitButton = QPushButton(self.frame)
        self.ExitButton.setObjectName("ExitButton")
        self.ExitButton.setGeometry(QRect(0, 530, 71, 71))
        self.HelpButton = QPushButton(self.frame)
        self.HelpButton.setObjectName("HelpButton")
        self.HelpButton.setGeometry(QRect(0, 460, 71, 71))

        StartMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartMainWindow)

        QMetaObject.connectSlotsByName(StartMainWindow)

    # setupUi

    def retranslateUi(self, StartMainWindow):
        StartMainWindow.setWindowTitle(
            QCoreApplication.translate("StartMainWindow", "BookLingo", None)
        )
        self.HelloQText.setHtml(
            QCoreApplication.translate(
                "StartMainWindow",
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
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-style:italic;">by Katsiaryna Viaernich and Vera Goriukhina</span></p></body></html>',
                None,
            )
        )

        self.KontoButton.setText(
            QCoreApplication.translate("StartMainWindow", "L", None)
        )
        self.MyBooksButton.setText(
            QCoreApplication.translate("StartMainWindow", "MyBooks", None)
        )
        self.FindButton.setText(
            QCoreApplication.translate("StartMainWindow", "Find", None)
        )
        self.FavoriteButton.setText(
            QCoreApplication.translate("StartMainWindow", "Fav", None)
        )
        self.ExitButton.setStyleSheet(
            QCoreApplication.translate(
                "StartMainWindow", "    border: none;\n" "    box-shadow: none;", None
            )
        )
        self.ExitButton.setText(
            QCoreApplication.translate("StartMainWindow", "Exit", None)
        )
        self.HelpButton.setStyleSheet(
            QCoreApplication.translate(
                "StartMainWindow", "    border: none;\n" "    box-shadow: none;", None
            )
        )
        self.HelpButton.setText(
            QCoreApplication.translate("StartMainWindow", "Help", None)
        )

    # retranslateUi
