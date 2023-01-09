import sys

import docx
from docxtpl import DocxTemplate
from PyQt5.QtWidgets import QMainWindow, QApplication
from project_window2 import Ui_MainWindow


pointers = []
variables = []
context = {}


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_button.clicked.connect(self.open)
        self.save_button.clicked.connect(self.save)
        self.clear_button.clicked.connect(self.clear)

    def open(self):
        a = self.comboBox.currentText()
        doc = docx.Document(f'templates/{a}')
        all_paragraphs = doc.paragraphs
        for paragraph in all_paragraphs:
            if '{' in paragraph.text:
                a = (paragraph.text[paragraph.text.find('{') + 2: paragraph.text.find('}')])
                if a not in pointers:
                    pointers.append(a)

        if len(pointers) >= 1:
            self.label.setText(pointers[0])
            self.label.update()
            self.label.show()
            self.lineEdit.show()

        if len(pointers) >= 2:
            self.label_2.setText(pointers[1])
            self.label_2.update()
            self.label_2.show()
            self.lineEdit_2.show()

        if len(pointers) >= 3:
            self.label_3.setText(pointers[2])
            self.label_3.update()
            self.label_3.show()
            self.lineEdit_3.show()

        if len(pointers) >= 4:
            self.label_4.setText(pointers[3])
            self.label_4.update()
            self.label_4.show()
            self.lineEdit_4.show()

        if len(pointers) >= 5:
            self.label_5.setText(pointers[4])
            self.label_5.update()
            self.label_5.show()
            self.lineEdit_5.show()

        if len(pointers) >= 6:
            self.label_6.setText(pointers[5])
            self.label_6.update()
            self.label_6.show()
            self.lineEdit_6.show()

        if len(pointers) >= 7:
            self.label_7.setText(pointers[6])
            self.label_7.update()
            self.label_7.show()
            self.lineEdit_7.show()

        if len(pointers) >= 8:
            self.label_8.setText(pointers[7])
            self.label_8.update()
            self.label_8.show()
            self.lineEdit_8.show()

        if len(pointers) >= 9:
            self.label_9.setText(pointers[8])
            self.label_9.update()
            self.label_9.show()
            self.lineEdit_9.show()

        if len(pointers) >= 10:
            self.label_10.setText(pointers[9])
            self.label_10.update()
            self.label_10.show()
            self.lineEdit_10.show()

        if len(pointers) >= 11:
            self.label_11.setText(pointers[10])
            self.label_11.update()
            self.label_11.show()
            self.lineEdit_11.show()

        if len(pointers) >= 12:
            self.label_12.setText(pointers[11])
            self.label_12.update()
            self.label_12.show()
            self.lineEdit_12.show()

        if len(pointers) >= 13:
            self.label_13.setText(pointers[12])
            self.label_13.update()
            self.label_13.show()
            self.lineEdit_13.show()

        if len(pointers) >= 14:
            self.label_14.setText(pointers[13])
            self.label_14.update()
            self.label_14.show()
            self.lineEdit_14.show()

        if len(pointers) >= 15:
            self.label_15.setText(pointers[14])
            self.label_15.update()
            self.label_15.show()
            self.lineEdit_15.show()

        if len(pointers) >= 16:
            self.label_16.setText(pointers[15])
            self.label_16.update()
            self.label_16.show()
            self.lineEdit_16.show()

        if len(pointers) >= 17:
            self.label_17.setText(pointers[16])
            self.label_17.update()
            self.label_17.show()
            self.lineEdit_17.show()

        if len(pointers) >= 18:
            self.label_18.setText(pointers[17])
            self.label_18.update()
            self.label_18.show()
            self.lineEdit_18.show()

        if len(pointers) >= 19:
            self.label_19.setText(pointers[18])
            self.label_19.update()
            self.label_19.show()
            self.lineEdit_19.show()

        if len(pointers) >= 20:
            self.label_20.setText(pointers[19])
            self.label_20.update()
            self.label_20.show()
            self.lineEdit_20.show()

    def save(self):
        if len(self.lineEdit.text()) > 0:
            variables.append(self.lineEdit.text())
        if len(self.lineEdit_2.text()) > 0:
            variables.append(self.lineEdit_2.text())
        if len(self.lineEdit_3.text()) > 0:
            variables.append(self.lineEdit_3.text())
        if len(self.lineEdit_4.text()) > 0:
            variables.append(self.lineEdit_4.text())
        if len(self.lineEdit_5.text()) > 0:
            variables.append(self.lineEdit_5.text())
        if len(self.lineEdit_6.text()) > 0:
            variables.append(self.lineEdit_6.text())
        if len(self.lineEdit_7.text()) > 0:
            variables.append(self.lineEdit_7.text())
        if len(self.lineEdit_8.text()) > 0:
            variables.append(self.lineEdit_8.text())
        if len(self.lineEdit_9.text()) > 0:
            variables.append(self.lineEdit_9.text())
        if len(self.lineEdit_10.text()) > 0:
            variables.append(self.lineEdit_10.text())
        if len(self.lineEdit_11.text()) > 0:
            variables.append(self.lineEdit_11.text())
        if len(self.lineEdit_12.text()) > 0:
            variables.append(self.lineEdit_12.text())
        if len(self.lineEdit_13.text()) > 0:
            variables.append(self.lineEdit_13.text())
        if len(self.lineEdit_14.text()) > 0:
            variables.append(self.lineEdit_14.text())
        if len(self.lineEdit_15.text()) > 0:
            variables.append(self.lineEdit_15.text())
        if len(self.lineEdit_16.text()) > 0:
            variables.append(self.lineEdit_16.text())
        if len(self.lineEdit_17.text()) > 0:
            variables.append(self.lineEdit_17.text())
        if len(self.lineEdit_18.text()) > 0:
            variables.append(self.lineEdit_18.text())
        if len(self.lineEdit_19.text()) > 0:
            variables.append(self.lineEdit_19.text())
        if len(self.lineEdit_20.text()) > 0:
            variables.append(self.lineEdit_20.text())

        if len(pointers) >= 1 and len(variables) >= 1:
            context[pointers[0]] = variables[0]
        if len(pointers) >= 2 and len(variables) >= 2:
            context[pointers[1]] = variables[1]
        if len(pointers) >= 3 and len(variables) >= 3:
            context[pointers[2]] = variables[2]
        if len(pointers) >= 4 and len(variables) >= 4:
            context[pointers[3]] = variables[3]
        if len(pointers) >= 5 and len(variables) >= 5:
            context[pointers[4]] = variables[4]
        if len(pointers) >= 6 and len(variables) >= 6:
            context[pointers[5]] = variables[5]
        if len(pointers) >= 7 and len(variables) >= 7:
            context[pointers[6]] = variables[6]
        if len(pointers) >= 8 and len(variables) >= 8:
            context[pointers[7]] = variables[7]
        if len(pointers) >= 9 and len(variables) >= 9:
            context[pointers[8]] = variables[8]
        if len(pointers) >= 10 and len(variables) >= 10:
            context[pointers[9]] = variables[9]
        if len(pointers) >= 11 and len(variables) >= 11:
            context[pointers[10]] = variables[10]
        if len(pointers) >= 12 and len(variables) >= 12:
            context[pointers[11]] = variables[11]
        if len(pointers) >= 13 and len(variables) >= 13:
            context[pointers[12]] = variables[12]
        if len(pointers) >= 14 and len(variables) >= 14:
            context[pointers[13]] = variables[13]
        if len(pointers) >= 15 and len(variables) >= 15:
            context[pointers[14]] = variables[14]
        if len(pointers) >= 16 and len(variables) >= 16:
            context[pointers[15]] = variables[15]
        if len(pointers) >= 17 and len(variables) >= 17:
            context[pointers[16]] = variables[16]
        if len(pointers) >= 18 and len(variables) >= 18:
            context[pointers[17]] = variables[17]
        if len(pointers) >= 19 and len(variables) >= 19:
            context[pointers[18]] = variables[18]
        if len(pointers) >= 20 and len(variables) >= 20:
            context[pointers[19]] = variables[19]

        a = self.comboBox.currentText()
        doc = DocxTemplate(f'templates/{a}')
        doc.render(context)
        doc.save('templates/finished_form.docx')

    def clear(self):
        pointers.clear()
        variables.clear()
        context.clear()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()
        self.label_19.hide()
        self.label_20.hide()

        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        self.lineEdit_8.hide()
        self.lineEdit_9.hide()
        self.lineEdit_10.hide()
        self.lineEdit_11.hide()
        self.lineEdit_12.hide()
        self.lineEdit_13.hide()
        self.lineEdit_14.hide()
        self.lineEdit_15.hide()
        self.lineEdit_16.hide()
        self.lineEdit_17.hide()
        self.lineEdit_18.hide()
        self.lineEdit_19.hide()
        self.lineEdit_20.hide()

        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_14.setText('')
        self.lineEdit_15.setText('')
        self.lineEdit_16.setText('')
        self.lineEdit_17.setText('')
        self.lineEdit_18.setText('')
        self.lineEdit_19.setText('')
        self.lineEdit_20.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

