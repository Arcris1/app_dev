from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


Form, Window = uic.loadUiType("tutorial_calc.ui")

class TutorialCalc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        
        self.ui.calculate_btn.clicked.connect(self.calculate)
        
    # For event calculations
    def calculate(self):
        try:
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
                    
            self.ui.result.setText(str(result))
        except ValueError:
            print("Error: Invalid provided data")
            
if __name__ == '__main__':
    app = QApplication([])
    window = TutorialCalc()
    window.show()
    app.exec()