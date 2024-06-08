from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

app = QApplication ([])
window = QMainWindow()

# Setting up window
window.setMinimumSize(400,500)
window.setWindowTitle("A new application")
window.setWindowIcon(QIcon("application_icon.png"))
# Adding widgets
# label = QLabel()
# label.setPixmap (QPixmap("application_icon.png").scaled ToHeight (250))
button = QPushButton("Click Me")

font = window.font()
font.setPointSize(17)

button.setFont(font)
button.setFixedSize(200, 200)

window.setCentralWidget(button)

window.show()
app.exec()