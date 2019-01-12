from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from movement import Movement


class Menu(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.logo = QPixmap('images/logo.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.logo)
        self.label.setGeometry(0, 0, 800, 720)

        self.setGeometry(550, 150, 800, 720)
        self.resize(self.logo.width(), self.logo.height())
        self.setMinimumSize(self.logo.width(), self.logo.height())
        self.setMaximumSize(self.logo.width(), self.logo.height())
        self.setWindowTitle('1942')
        self.setWindowIcon(QIcon('images/icon.png'))

        buttonPlay = QPushButton('START GAME', self)
        buttonPlay.clicked.connect(self.gamewindow)
        buttonPlay.resize(320, 40)
        buttonPlay.move(40, 320)

        buttonExit = QPushButton('EXIT', self)
        buttonExit.clicked.connect(self.exit)
        buttonExit.resize(320, 40)
        buttonExit.move(440, 320)

    def gamewindow(self):
        self.game = Movement(self)
        self.game.closed.connect(self.show)
        self.game.show()
        self.hide()

    def exit(self):
        self.close()
