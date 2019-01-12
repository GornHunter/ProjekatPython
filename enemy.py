from movement import *


class Enemy:
    def __init__(self, mainWindow):
        self.health = 0
        self.width = 0
        self.height = 0
        self.x = 0
        self.y = 0
        self.targetx = 0
        self.targety = 0
        self.bulletCounter = 0
        self.speed = 0
        self.isMoving = False
        self.label = QLabel(mainWindow)
        self.label.show()
        self.mainWindow = mainWindow

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.label.setGeometry(x, y, self.width, self.height)

    def hit(self):
        self.health -= 1
        return self.health == 0

    def moveTo(self, x, y):
        self.targetx = x
        self.targety = y
        self.isMoving = True

    def update(self):
        if self.isMoving:
            if self.x == self.targetx and self.y == self.targety:
                self.isMoving = False
            else:
                if self.targetx > self.x:
                    if abs(self.targetx - self.x) > self.speed:
                        self.x += self.speed
                    else:
                        self.x += self.targetx - self.x
                else:
                    if abs(self.targetx - self.x) > self.speed:
                        self.x -= self.speed
                    else:
                        self.x += self.targetx - self.x

                if self.targety > self.y:
                    if abs(self.targety - self.y) > self.speed:
                        self.y += self.speed
                    else:
                        self.y += self.targety - self.y
                else:
                    if abs(self.targety - self.y) > self.speed:
                        self.y -= self.speed
                    else:
                        self.y += self.targety - self.y

                self.label.setGeometry(self.x, self.y, self.width, self.height)

    def fire(self):
        if self.bulletCounter > 0:
            self.bulletCounter -= 1

        if self.bulletCounter == 0:
            self.bulletCounter = 20
            temp = QLabel(self.mainWindow)
            temp.setObjectName(" 3")
            rect = self.label.geometry()
            temp.setGeometry(rect.x() + rect.width() / 2 - 3, rect.y() + 69, 6, 10)
            temp.setPixmap(QPixmap('images/bulletE.png'))
            temp.show()
            self.mainWindow.bulletListE.append(temp)
