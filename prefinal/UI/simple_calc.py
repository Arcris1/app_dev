from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

Form, Window = uic.loadUiType("simple_calc.ui")

class SimpleCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.calculate_btn.clicked.connect(self.calculate)
        self.result_label = self.ui.result_lbl
        self.invalid_lbl = self.ui.invalid_lbl
    
    def calculate(self):
        try:
            self.invalid_lbl.hide()
            num1 = float(self.ui.num1.text())
            num2 = float(self.ui.num2.text())
            operators = self.ui.operators.currentText()
            
            # Perform calculations
            result = 0
            match(operators):
                case '+':
                    result = num1 + num2
                case '-':
                    result = num1 - num2
                case '/':
                    result = num1 / num2
                case '*':
                    result = num1 * num2
                case '%':
                    result = num1 % num2
        
            self.result_label.setText(str(result))
            
        except ValueError:
            print("Error: Invalid input number, please check your fields.")
            self.invalid_lbl.show()
            self.invalid_lbl.setStyleSheet("color: red;")
            self.invalid_lbl.setText("Error: Invalid input number, please check your fields.")
    
    def update(self):
        self.invalid_lbl.adjustSize()