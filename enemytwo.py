from enemy import Enemy


class EnemyTwo(Enemy):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.health = 20
        self.width = 75
        self.height = 61
        self.speed = 2
        self.label.setPixmap(mainWindow.enemy2)
