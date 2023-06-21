# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Page.ui'
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


class Ui_PageMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AuthorNametextEdit = QTextEdit(self.centralwidget)
        self.AuthorNametextEdit.setReadOnly(True)
        self.AuthorNametextEdit.setObjectName("AuthorNametextEdit")
        self.AuthorNametextEdit.setGeometry(QRect(0, 10, 631, 31))
        self.AuthorNametextEdit.setStyleSheet(
            " border: none;\n background-color: #f5e6c6; font-size: 12px\n"
        )

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QRect(60, 60, 651, 431))
        self.textEdit.setStyleSheet(
            " border: none;\n"
            "    box-shadow: none; background-color: #faf5ea;\n;  padding: 15px; "
        )
        self.textEdit.setFontPointSize(12)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(60, 510, 651, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.nextPageButton = QPushButton(self.frame_2)
        self.nextPageButton.setObjectName("nextPage")
        self.nextPageButton.setGeometry(QRect(610, 10, 41, 24))
        self.nextPageButton.setStyleSheet(" border: none;\n" "    box-shadow: none;")

        self.addQuoteButton = QPushButton(self.centralwidget)
        self.addQuoteButton.setObjectName("previous page")
        self.addQuoteButton.setGeometry(QRect(380, 10, 75, 31))  #275, 495, 181, 24
        self.addQuoteButton.setStyleSheet(" \n" "    box-shadow: none;")

        self.translateButton = QPushButton(self.centralwidget)
        self.translateButton.setObjectName("previous page")
        self.translateButton.setGeometry(QRect(470, 10, 75, 31))  # 275, 495, 181, 24
        self.translateButton.setStyleSheet(" \n" "    box-shadow: none;")

        self.wikipediaButton = QPushButton(self.centralwidget)
        self.wikipediaButton.setObjectName("previous page")
        self.wikipediaButton.setGeometry(QRect(560, 10, 75, 31))  # 275, 495, 181, 24
        self.wikipediaButton.setStyleSheet(" \n" "    box-shadow: none;")

        icon1 = QIcon()
        iconThemeName = "go-next"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(
                "../Python/Projects/venv/Lib/site-packages/PySide6",
                QSize(),
                QIcon.Normal,
                QIcon.Off,
            )

        self.nextPageButton.setIcon(icon1)
        self.prevPageButton = QPushButton(self.frame_2)
        self.prevPageButton.setObjectName("previous page")
        self.prevPageButton.setGeometry(QRect(0, 10, 41, 24))
        self.prevPageButton.setStyleSheet(" border: none;\n" "    box-shadow: none;")
        icon2 = QIcon()
        iconThemeName = "go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(
                "../Python/Projects/venv/Lib/site-packages/PySide6",
                QSize(),
                QIcon.Normal,
                QIcon.Off,
            )

        self.prevPageButton.setIcon(icon2)
        self.PageslineEdit = QLineEdit(self.frame_2)
        self.PageslineEdit.setObjectName("PageslineEdit")
        self.PageslineEdit.setGeometry(QRect(250, 15, 113, 21))
        self.PageslineEdit.setAlignment(Qt.AlignCenter)
        self.PageslineEdit.setStyleSheet(
            " border: none;\n" "    box-shadow: none; background-color: #faf5ea;\n"
        )
        self.questionsButton = QPushButton(self.centralwidget)
        self.questionsButton.setObjectName("pushButton_3")
        self.questionsButton.setGeometry(QRect(275, 495, 181, 24))
        # self.questionsButton.set
        self.questionsButton.setStyleSheet(
            "font-style: italic;" "    box-shadow: none;  font-size: 14px; "
        )

        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setGeometry(QRect(650, 10, 75, 31))
        self.closeButton.setStyleSheet(
            "font-style: italic;" "    box-shadow: none;  font-size: 14px; "
        )
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Reading", None)
        )
        self.AuthorNametextEdit.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )

        self.nextPageButton.setText(
            QCoreApplication.translate("MainWindow", "->", None)
        )
        self.prevPageButton.setText(
            QCoreApplication.translate("MainWindow", "<-", None)
        )
        self.PageslineEdit.setText(
            QCoreApplication.translate("MainWindow", "page/page", None)
        )
        self.questionsButton.setText(
            QCoreApplication.translate("MainWindow", "Check understanding", None)
        )
        self.closeButton.setText("Close")
        self.addQuoteButton.setText("Add quote")
        self.translateButton.setText("Translate")
        self.wikipediaButton.setText("Wiki")

    # retranslateUi
