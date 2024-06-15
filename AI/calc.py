import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Go to Page 2", self, clicked=lambda: self.switch_page(1)))
        layout.addWidget(QPushButton("Go to Page 3", self, clicked=lambda: self.switch_page(2)))
        self.setLayout(layout)

    def switch_page(self, index):
        self.parentWidget().setCurrentIndex(index)

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Go to Page 1", self, clicked=lambda: self.switch_page(0)))
        self.setLayout(layout)

    def switch_page(self, index):
        self.parentWidget().setCurrentIndex(index)

class Page3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Go to Page 1", self, clicked=lambda: self.switch_page(0)))
        self.setLayout(layout)

    def switch_page(self, index):
        self.parentWidget().setCurrentIndex(index)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Page Application")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.page1 = Page1()
        self.page2 = Page2()
        self.page3 = Page3()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
