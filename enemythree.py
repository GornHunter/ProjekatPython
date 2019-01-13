from enemy import Enemy


class EnemyThree(Enemy):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.health = 3
        self.width = 150
        self.height = 83
        self.speed = 2
        self.label.setPixmap(mainWindow.enemy3)
