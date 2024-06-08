from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from simple_calc import SimpleCalculatorApp

if __name__ == "__main__":
    app = QApplication([])
    window = SimpleCalculatorApp()
    window.show()
    app.exec()