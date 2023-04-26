from PyQt5.QtWidgets import *
from main import Ui_Form
from PyQt5 import uic
import sys
class Anaekran_screen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("main.ui",self)
        self.sayac = 0
        self.anaekrandeyisen = Ui_Form()
        self.anaekrandeyisen.setupUi(self)
        self.anaekrandeyisen.plus.clicked.connect(self.artir)
        self.anaekrandeyisen.minus.clicked.connect(self.azalt)
    def artir(self):
        if self.sayac < 999999:
            self.sayac += 1
            self.anaekrandeyisen.label.setText(str(self.sayac))
    
    def azalt(self):
        if self.sayac > 0:
            self.sayac -= 1
            self.anaekrandeyisen.label.setText(str(self.sayac))

app = QApplication([])
ekran = Anaekran_screen()
ekran.show()
app.exec_()
