from PyQt5.QtCore import Qt, QRect, QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon, QPainter
from PyQt5.QtWidgets import QLabel, QMainWindow

from key_notifier import KeyNotifier


class Movement(QMainWindow):

    closed = pyqtSignal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.parent = parent

        self.moveSpeed = 13
        self.bulletCounter1 = 0
        self.bulletCounter2 = 0
        self.bulletList1 = []
        self.bulletList2 = []
        self.seaPos = 0

        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.frame)
        self.timer.start(10)

        self.setGeometry(300, 30, 1024, 768)
        self.setMinimumSize(1024, 768)
        self.setMaximumSize(1024, 768)

        self.pix1 = QPixmap('player1.png')
        self.pix2 = QPixmap('player2.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)

        self.seaTex = QPixmap("sea.png").scaled(70, 77)

        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self):

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(848, 674, 120, 95)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(63, 674, 112, 96)

        self.setWindowTitle('1942')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1: QRect = self.label1.geometry()
        rec2: QRect = self.label2.geometry()

        if key == Qt.Key_Right:
            if rec1.x() + rec1.width() <= 1024:
                self.label1.setGeometry(rec1.x() + self.moveSpeed, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            if rec1.y() + rec1.height() <= 768:
                self.label1.setGeometry(rec1.x(), rec1.y() + self.moveSpeed, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            if rec1.y() > 1:
                self.label1.setGeometry(rec1.x(), rec1.y() - self.moveSpeed, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            if rec1.x() > 0:
                self.label1.setGeometry(rec1.x() - self.moveSpeed, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_M:
            if self.bulletCounter1 == 0:
                self.bulletCounter1 = 20
                temp = QLabel(self)
                temp.setGeometry(rec1.x() + rec1.width() / 2 - 4, rec1.y() - 10, 10, 10)
                temp.setPixmap(QPixmap('bullet1.png'))
                temp.show()
                self.bulletList1.append(temp)

        if key == Qt.Key_D:
            if rec2.x() + rec2.width() <= 1024:
                self.label2.setGeometry(rec2.x() + self.moveSpeed, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_S:
            if rec2.y() + rec2.height() <= 768:
                self.label2.setGeometry(rec2.x(), rec2.y() + self.moveSpeed, rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            if rec2.y() > 1:
                self.label2.setGeometry(rec2.x(), rec2.y() - self.moveSpeed, rec2.width(), rec2.height())
        elif key == Qt.Key_A:
            if rec2.x() > 0:
                self.label2.setGeometry(rec2.x() - self.moveSpeed, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_R:
            if self.bulletCounter2 == 0:
                self.bulletCounter2 = 20
                temp = QLabel(self)
                temp.setGeometry(rec2.x() + rec2.width() / 2 - 4, rec2.y() - 10, 10, 10)
                temp.setPixmap(QPixmap('bullet2.png'))
                temp.show()
                self.bulletList2.append(temp)

        if key == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.key_notifier.die()
        self.closed.emit()
        event.accept()

    def paintEvent(self, *args, **kwargs):

        p = QPainter(self)

        for i in range(0, 15):
            for j in range(-1, 10):
                p.drawPixmap(i * self.seaTex.width(), j * self.seaTex.height() + self.seaPos, self.seaTex)

    def frame(self):
        if self.bulletCounter1 > 0:
            self.bulletCounter1 -= 1

        if self.bulletCounter2 > 0:
            self.bulletCounter2 -= 1

        self.seaPos += 1
        if self.seaPos > self.seaTex.height():
            self.seaPos = 0

        for bullet1 in self.bulletList1:
            rec: QRect = bullet1.geometry()
            bullet1.setGeometry(rec.x(), rec.y() - 3, rec.width(), rec.height())
            if rec.y() < -10:
                bullet1.clear()
                self.bulletList1.remove(bullet1)
            # if rec.intersects(self.label2.geometry()):
            #    bullet.clear()
            #    self.bulletList.remove(bullet)
        self.update()

        for bullet2 in self.bulletList2:
            rec: QRect = bullet2.geometry()
            bullet2.setGeometry(rec.x(), rec.y() - 3, rec.width(), rec.height())
            if rec.y() < -10:
                bullet2.clear()
                self.bulletList2.remove(bullet2)
            # if rec.intersects(self.label1.geometry()):
            #    bullet.clear()
            #    self.bulletList.remove(bullet)
        self.update()