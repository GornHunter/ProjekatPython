import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


from key_notifier import KeyNotifier


class SimMoveDemo(QWidget):

    def __init__(self):
       super().__init__()

        self.pix1 = QPixmap('airplane2.png')
        self.pix2 = QPixmap('airplane3.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)

        self.setWindowState(Qt.WindowMaximized)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self):
        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(1800, 900, 50, 50)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(50, 900, 50, 50)

        self.setWindowTitle('1942')

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1 = self.label1.geometry()
        rec2 = self.label2.geometry()

        if key == Qt.Key_Right:
            self.label1.setGeometry(rec1.x() + 13, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            self.label1.setGeometry(rec1.x(), rec1.y() + 13, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            self.label1.setGeometry(rec1.x(), rec1.y() - 13, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            self.label1.setGeometry(rec1.x() - 13, rec1.y(), rec1.width(), rec1.height())

        if key == Qt.Key_D:
            self.label2.setGeometry(rec2.x() + 13, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_S:
            self.label2.setGeometry(rec2.x(), rec2.y() + 13, rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            self.label2.setGeometry(rec2.x(), rec2.y() - 13, rec2.width(), rec2.height())
        elif key == Qt.Key_A:
            self.label2.setGeometry(rec2.x() - 13, rec2.y(), rec2.width(), rec2.height())

        if key == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.key_notifier.die()

    def paintEvent(self, event):
         p = QPainter(self)

         p.fillRect(event.rect(), QBrush(Qt.black))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())