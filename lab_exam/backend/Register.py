from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from backend.db import Users, lastUserId

Form, Window = uic.loadUiType("frontend/register.ui")

class RegisterPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        
        self.ui.loginBtn.clicked.connect(self.login_page)
        self.ui.registerBtn.clicked.connect(self.register_user)
        
    def login_page(self):
        self.hide()
        from backend.Login import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()
        
    def register_user(self):
        global lastUserId
        first_name = self.ui.firstname.text()
        last_name = self.ui.lastname.text()
        age = self.ui.age.text()
        email = self.ui.email.text()
        username = self.ui.username.text()
        password = self.ui.password.text()
        
        if username in Users:
            QMessageBox.warning(self, "Registration Failed", "Username already exists")
        else:
            lastUserId += 1
            Users[lastUserId] = {
                'first_name': first_name,
                'last_name': last_name,
                'age': age,
                'email': email,
                'username': username,
                'password': password
            }
            QMessageBox.information(self, "Registration Successful", "You have registered successfully")
            print(Users)