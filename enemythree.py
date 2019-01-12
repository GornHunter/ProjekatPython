from enemy import Enemy


class EnemyThree(Enemy):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.health = 30
        self.width = 225
        self.height = 125
        self.speed = 2
        self.label.setPixmap(mainWindow.enemy3)
