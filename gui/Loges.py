# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Loged.ui'
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

class Ui_LogedQMainWindow(object):
    def setupUi(self, LogedQMainWindow):
        if not LogedQMainWindow.objectName():
            LogedQMainWindow.setObjectName(u"LogedQMainWindow")
        LogedQMainWindow.resize(800, 601)
        LogedQMainWindow.setStyleSheet(u"background-color: #faf5ea;\n"
"")
        self.centralwidget = QWidget(LogedQMainWindow)
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
        self.BackButton = QPushButton(self.frame)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(0, 530, 71, 71))
        self.BackButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.HelpButton = QPushButton(self.frame)
        self.HelpButton.setObjectName(u"HelpButton")
        self.HelpButton.setGeometry(QRect(0, 460, 71, 71))
        self.HelpButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none;")
        self.HelloUserQTextEdit = QTextEdit(self.centralwidget)
        self.HelloUserQTextEdit.setObjectName(u"HelloUserQTextEdit")
        self.HelloUserQTextEdit.setGeometry(QRect(140, 100, 551, 71))
        self.HelloUserQTextEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        self.LogOutButton = QPushButton(self.centralwidget)
        self.LogOutButton.setObjectName(u"LogOutButton")
        self.LogOutButton.setGeometry(QRect(260, 533, 291, 41))
        self.LogOutButton.setStyleSheet(u"    border: none;\n"
"    box-shadow: none; background-color: #f5e6c6;\n"
"  font-size: 14px;")
        LogedQMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogedQMainWindow)

        QMetaObject.connectSlotsByName(LogedQMainWindow)
    # setupUi

    def retranslateUi(self, LogedQMainWindow):
        LogedQMainWindow.setWindowTitle(QCoreApplication.translate("LogedQMainWindow", u"Login", None))
        self.KontoButton.setText(QCoreApplication.translate("LogedQMainWindow", u"L", None))
        self.MyBooksButton.setText(QCoreApplication.translate("LogedQMainWindow", u"MyBooks", None))
        self.FindButton.setText(QCoreApplication.translate("LogedQMainWindow", u"Find", None))
        self.FavoriteButton.setText(QCoreApplication.translate("LogedQMainWindow", u"Fav", None))
        self.BackButton.setText(QCoreApplication.translate("LogedQMainWindow", u"Back", None))
        self.HelpButton.setText(QCoreApplication.translate("LogedQMainWindow", u"Help", None))
        self.LogOutButton.setText(QCoreApplication.translate("LogedQMainWindow", u"Log Out", None))
    # retranslateUi

