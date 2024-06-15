from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.Login import LoginPage

if __name__ == '__main__':
    app = QApplication([])
    window = LoginPage()
    window.show()
    app.exec()