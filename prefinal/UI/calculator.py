from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

Form, Window = uic.loadUiType("simple_calculator.ui")

class Calculator(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        
        self.ui.calculate_btn.clicked.connect(self.calculate)
        # self.result_label = self.ui.result_lbl
        
        self.invalid_data = self.ui.invalid_data
        self.invalid_data.hide()
    
    def calculate(self):
        self.update()
        try:
            self.invalid_data.hide()
            num1 = float(self.ui.num1.text())
            num2 = float(self.ui.num2.text())
            operators = self.ui.operators.currentText()
            
            result = 0
            match(operators):
                case '+':
                    result = num1 + num2
                case '-':
                    result = num1 - num2
                case '*':
                    result = num1 * num2
                case '/':
                    result = num1 / num2
                case '%':
                    result = num1 % num2
            
            self.ui.result.setText(str(result))
        except ValueError:
            print("Error: Invalid provided data")
            self.invalid_data.setStyleSheet("color: red;")
            self.invalid_data.setText("Error: Invalid input number, please check your fields.")
            self.invalid_data.show()
    
    def update(self):
        self.invalid_data.adjustSize()
        


if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec()