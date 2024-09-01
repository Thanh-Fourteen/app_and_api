import sys
from PyQt6.QtWidgets import QApplication, QWidget

from PyQt6 import uic
import getRespone as GS

class MyApp(QWidget):
    def __init__(self):
       super().__init__()
       uic.loadUi(r"C:\Users\admin\Desktop\Test2\form.ui", self)
       self.setWindowTitle('9.5 Translate')
       self.E2V.clicked.connect(self.Eng2Vie)
       self.V2E.clicked.connect(self.Vie2Eng)
    
    def Eng2Vie(self):
        inputText = self.input.toPlainText()
        res = GS.getRes(inputText, "E2V")
        self.output.setPlainText(f"{res}")
    
    def Vie2Eng(self):
        inputText = self.input.toPlainText()
        res = GS.getRes(inputText, "V2E")
        self.output.setPlainText(f"{res}")


app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec()