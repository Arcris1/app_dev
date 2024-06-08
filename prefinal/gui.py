from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(650, 200, 500, 500)
    win.setWindowTitle("Tech With Cris!")
    
    label = QLabel(win)
    label.setText("Hello World")
    label.move(0, 50)
    
    button = QPushButton(win)
    button.setText("Hello World")
    button.move(100, 50)
    
    win.show()
    sys.exit(app.exec())
    
window()