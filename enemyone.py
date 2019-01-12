from enemy import Enemy


class EnemyOne(Enemy):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.health = 1
        self.width = 75
        self.height = 60
        self.speed = 2
        self.label.setPixmap(mainWindow.enemy1)
