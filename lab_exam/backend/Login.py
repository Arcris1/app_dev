from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
Form, Window = uic.loadUiType("frontend/login.ui")

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
        QMessageBox.warning(self, "Failed to login", "Please check your username and password")
