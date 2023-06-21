# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyBooks.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QListView, QMainWindow,
                               QPlainTextEdit, QPushButton, QSizePolicy,
                               QTextEdit, QWidget)


class Ui_MyBooksMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #faf5ea;\n" "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MyBookslistView = QListView(self.centralwidget)
        self.MyBookslistView.setObjectName("MyBookslistView")
        self.MyBookslistView.setGeometry(QRect(100, 100, 651, 471))
        self.MyBookslistView.setStyleSheet(" border: none;\n" "    box-shadow: none;")
        self.MyBookstextEdit = QTextEdit(self.centralwidget)
        self.MyBookstextEdit.setObjectName("MyBookstextEdit")
        self.MyBookstextEdit.setGeometry(QRect(80, 0, 671, 51))
        self.MyBookstextEdit.setStyleSheet(" border: none;\n" "    box-shadow: none;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 0, 71, 601))
        self.frame.setStyleSheet("background-color: #f5e6c6;\n" "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.KontoButton_3 = QPushButton(self.frame)
        self.KontoButton_3.setObjectName("KontoButton_3")
        self.KontoButton_3.setGeometry(QRect(0, 0, 71, 71))
        self.KontoButton_3.setStyleSheet("    border: none;\n" "    box-shadow: none;")
        icon = QIcon()
        iconThemeName = "user-desktop"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(
                "../Python/Projects/venv/Lib/site-packages/PySide6",
                QSize(),
                QIcon.Normal,
                QIcon.Off,
            )

        self.KontoButton_3.setIcon(icon)
        self.MyBooksButton_3 = QPushButton(self.frame)
        self.MyBooksButton_3.setObjectName("MyBooksButton_3")
        self.MyBooksButton_3.setGeometry(QRect(0, 140, 71, 71))
        self.MyBooksButton_3.setStyleSheet(
            "    border: none;\n" "    box-shadow: none;"
        )
        self.FindButton_3 = QPushButton(self.frame)
        self.FindButton_3.setObjectName("FindButton_3")
        self.FindButton_3.setGeometry(QRect(0, 210, 71, 71))
        self.FindButton_3.setStyleSheet("    border: none;\n" "    box-shadow: none;")
        self.FavoriteButton_3 = QPushButton(self.frame)
        self.FavoriteButton_3.setObjectName("FavoriteButton_3")
        self.FavoriteButton_3.setGeometry(QRect(0, 70, 71, 71))
        self.FavoriteButton_3.setStyleSheet(
            "    border: none;\n" "    box-shadow: none;"
        )
        self.ExitButton_3 = QPushButton(self.frame)
        self.ExitButton_3.setObjectName("ExitButton_3")
        self.ExitButton_3.setGeometry(QRect(0, 530, 71, 71))
        self.ExitButton_3.setStyleSheet("    border: none;\n" "    box-shadow: none;")
        self.HelpButton_3 = QPushButton(self.frame)
        self.HelpButton_3.setObjectName("HelpButton_3")
        self.HelpButton_3.setGeometry(QRect(0, 460, 71, 71))
        self.HelpButton_3.setStyleSheet("    border: none;\n" "    box-shadow: none;")
        self.findMyBookplainTextEdit = QPlainTextEdit(self.centralwidget)
        self.findMyBookplainTextEdit.setObjectName("findMyBookplainTextEdit")
        self.findMyBookplainTextEdit.setGeometry(QRect(100, 60, 651, 31))
        self.findMyBookplainTextEdit.setStyleSheet("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "My Books", None)
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
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt; font-weight:700; font-style:italic;">My Books</span></p></body></html>',
                None,
            )
        )
        self.KontoButton_3.setText(QCoreApplication.translate("MainWindow", "L", None))
        self.MyBooksButton_3.setText(
            QCoreApplication.translate("MainWindow", "MyBooks", None)
        )
        self.FindButton_3.setText(
            QCoreApplication.translate("MainWindow", "Find", None)
        )
        self.FavoriteButton_3.setText(
            QCoreApplication.translate("MainWindow", "Fav", None)
        )
        self.ExitButton_3.setText(
            QCoreApplication.translate("MainWindow", "Exit", None)
        )
        self.HelpButton_3.setText(
            QCoreApplication.translate("MainWindow", "Help", None)
        )

    # retranslateUi
