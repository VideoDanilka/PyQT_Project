import sys
from docxtpl import DocxTemplate
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main window.ui', self)
        self.save_button.clicked.connect(self.save)
