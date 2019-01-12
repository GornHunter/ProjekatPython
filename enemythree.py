from enemy import Enemy


class EnemyThree(Enemy):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.health = 3
        self.width = 300
        self.height = 166
        self.speed = 2
        self.label.setPixmap(mainWindow.enemy3)
