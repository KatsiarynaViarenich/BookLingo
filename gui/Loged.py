# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Loged.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QWidget,
)


class Ui_LogedQMainWindow(object):
    def setupUi(self, LogedQMainWindow):
        if not LogedQMainWindow.objectName():
            LogedQMainWindow.setObjectName("LogedQMainWindow")
        LogedQMainWindow.resize(800, 601)
        LogedQMainWindow.setStyleSheet("background-color: #faf5ea;\n" "")
        self.centralwidget = QWidget(LogedQMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.HelloUserQTextEdit = QTextEdit(self.centralwidget)
        self.HelloUserQTextEdit.setObjectName("HelloUserQTextEdit")
        self.HelloUserQTextEdit.setGeometry(QRect(120, 100, 551, 171))
        self.HelloUserQTextEdit.setStyleSheet(
            " border: none;\n" "    box-shadow: none;"
        )
        self.LogOutButton = QPushButton(self.centralwidget)
        self.LogOutButton.setObjectName("LogOutButton")
        self.LogOutButton.setGeometry(QRect(250, 480, 291, 41))
        self.LogOutButton.setStyleSheet(
            "    border: none;\n"
            "    box-shadow: none; background-color: #f5e6c6;\n"
            "  font-size: 14px;"
        )

        self.retranslateUi(LogedQMainWindow)

        QMetaObject.connectSlotsByName(LogedQMainWindow)

    # setupUi

    def retranslateUi(self, LogedQMainWindow):
        LogedQMainWindow.setWindowTitle(
            QCoreApplication.translate("LogedQMainWindow", "Login", None)
        )

        self.LogOutButton.setText(
            QCoreApplication.translate("LogedQMainWindow", "Log Out", None)
        )

    # retranslateUi
