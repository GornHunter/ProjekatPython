import sys
from PyQt5.QtWidgets import QApplication
from menu import Menu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
