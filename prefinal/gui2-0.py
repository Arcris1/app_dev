from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("Clicked Me")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 200, 300, 300)
    win.setWindowTitle("Tech With Cris!")
    
    label = QtWidgets.QLabel(win)
    label.setText("Hello World")
    label.move(0, 50)
    
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me")
    b1.clicked.connect(clicked)
    
    
    win.show()
    sys.exit(app.exec())
    
window()