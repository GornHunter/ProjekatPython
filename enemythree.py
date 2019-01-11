from enemy import Enemy


class EnemyThree(Enemy):

    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.health = 3
        self.label.setPixmap(mainWindow.enemy3)
        self.width = 120
        self.height = 95
        self.speed = 2