import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

class LoginPage(QWidget):
    def __init__(self, stacked_widget, user_accounts):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.user_accounts = user_accounts

        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login", self)
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        register_button = QPushButton("Register", self)
        register_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(register_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.user_accounts and self.user_accounts[username] == password:
            self.stacked_widget.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

class RegisterPage(QWidget):
    def __init__(self, stacked_widget, user_accounts):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.user_accounts = user_accounts

        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        register_button = QPushButton("Register", self)
        register_button.clicked.connect(self.register)
        layout.addWidget(register_button)

        back_to_login_button = QPushButton("Back to Login", self)
        back_to_login_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(back_to_login_button)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.user_accounts:
            QMessageBox.warning(self, "Registration Failed", "Username already exists")
        else:
            self.user_accounts[username] = password
            QMessageBox.information(self, "Registration Successful", "You have registered successfully")
            self.stacked_widget.setCurrentIndex(0)

class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        welcome_label = QLabel("Welcome to the Home Page!", self)
        layout.addWidget(welcome_label)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Page Application with Login and Registration")

        self.user_accounts = {}

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_page = LoginPage(self.stacked_widget, self.user_accounts)
        self.register_page = RegisterPage(self.stacked_widget, self.user_accounts)
        self.home_page = HomePage()

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.register_page)
        self.stacked_widget.addWidget(self.home_page)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
