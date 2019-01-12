from enemy import Enemy


class EnemyTwo(Enemy):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.health = 2
        self.width = 123
        self.height = 119
        self.speed = 2
        self.label.setPixmap(mainWindow.enemy2)
