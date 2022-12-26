import sys
from docxtpl import DocxTemplate
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MVP.ui', self)
        self.save_button.clicked.connect(self.save)

    def save(self):
        doc = DocxTemplate('MVP.docx')
        context = {'name': 'Вася'}
        doc.rendert(context)
        doc.save('MVP2.docx')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
