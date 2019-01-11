from enemy import Enemy


class EnemyOne(Enemy):

    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.health = 1
        self.label.setPixmap(mainWindow.enemy1)
        self.width = 120
        self.height = 95
        self.speed = 2