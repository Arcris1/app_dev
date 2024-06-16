from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
Form, Window = uic.loadUiType("frontend/login.ui")
from backend.db import Users, lastUserId

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        
        self.ui.loginBtn.clicked.connect(self.login_user)
        self.ui.create_acct_btn.clicked.connect(self.create_acct_page)
        
    def create_acct_page(self):
        self.hide()
        from backend.Register import RegisterPage
        self.register_page = RegisterPage()
        self.register_page.show()
        
    def login_user(self):
        from backend.Home import HomePage
        username = self.ui.username.text()
        password = self.ui.password.text()
        
        if not Users:
            QMessageBox.warning(self, "No Users", "No users are registered yet")
            return
        
        for user in Users.values():
            if user['username'] == username and user['password'] == password:
                QMessageBox.information(self, "Login Successful", "You have logged in successfully")
                self.home_page = HomePage()
                self.home_page.show()
                self.hide()
                return
        
        QMessageBox.warning(self, "Invalid Credentials", "Please check your username or password")

            
