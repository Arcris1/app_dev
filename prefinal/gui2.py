from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setGeometry(500, 200, 300, 300)
        self.setWindowTitle("Tech With Cris!")
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hi World")
        self.label.move(50, 50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked)
    
    def clicked(self):
        self.label.setText("Hello, Lorem ipsum sit amet consectur")
        self.update()
    
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec())
    
window()