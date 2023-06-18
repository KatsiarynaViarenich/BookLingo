from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, \
    QListWidgetItem
from Main import Ui_StartMainWindow
from Favourite import Ui_FavouriteMainWindow



class StartMainWindow(QMainWindow):
    def __init__(self):
        super(StartMainWindow, self).__init__()
        self.ui=Ui_StartMainWindow()
        self.ui.setupUi(self)
        self.ui_fav=FavouriteMainWindow()
        self.buttons()

    def buttons(self):
        self.ui.FavoriteButton.clicked.connect(self.ui_fav.show)


class FavouriteMainWindow(QMainWindow):
    def __init__(self):
        super(FavouriteMainWindow, self).__init__()
        self.ui = Ui_FavouriteMainWindow()
        self.ui.setupUi(self)
        #self.buttons()


if __name__ == "__main__":
    app = QApplication()
    window = StartMainWindow()
    window.show()
    exit(app.exec())