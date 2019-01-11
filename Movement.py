import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout, QAction, QMainWindow

from key_notifier import KeyNotifier


class Movement(QMainWindow):

    def __init__(self):
        super().__init__()

        #self.setWindowState(Qt.WindowMaximized)
        self.setGeometry(600, 300, 800, 600)
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("sea.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.pix1 = QPixmap('player1.png')
        self.pix2 = QPixmap('player2.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)

        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self):

        exitAct = QAction(QIcon('skull.png'), 'Exit 1942', self)
        exitAct.setShortcut('Ctrl+Q')
        #exitAct.setStatusTip('Exit')
        exitAct.triggered.connect(self.close)

        #self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Game')
        fileMenu.addAction(exitAct)

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(100, 40, 120, 95)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(50, 40, 112, 96)

        self.setWindowTitle('1942')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1 = self.label1.geometry()
        rec2 = self.label2.geometry()

        if key == Qt.Key_Right:
            self.label1.setGeometry(rec1.x() + 5, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            self.label1.setGeometry(rec1.x(), rec1.y() + 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            self.label1.setGeometry(rec1.x(), rec1.y() - 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            self.label1.setGeometry(rec1.x() - 5, rec1.y(), rec1.width(), rec1.height())

        if key == Qt.Key_D:
            self.label2.setGeometry(rec2.x() + 5, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_S:
            self.label2.setGeometry(rec2.x(), rec2.y() + 5, rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            self.label2.setGeometry(rec2.x(), rec2.y() - 5, rec2.width(), rec2.height())
        elif key == Qt.Key_A:
            self.label2.setGeometry(rec2.x() - 5, rec2.y(), rec2.width(), rec2.height())

    def closeEvent(self, event):
        self.key_notifier.die()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Movement()
    sys.exit(app.exec_())
