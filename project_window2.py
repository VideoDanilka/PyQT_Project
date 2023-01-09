import os

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 733)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 10, 141, 31))
        self.comboBox.setObjectName("comboBox")
        file_names = os.listdir('templates')
        self.comboBox.addItems(file_names)

        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(200, 10, 211, 31))
        self.open_button.setObjectName("open_button")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 141, 21))
        self.label.setObjectName("label")
        self.label.hide()

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 60, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.hide()

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(38, 120, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.hide()

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 110, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.hide()

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(38, 220, 141, 21))
        self.label_4.setObjectName("label_4")
        self.label_4.hide()

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 141, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.hide()

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 210, 201, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.hide()

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 160, 201, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.hide()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(38, 320, 141, 21))
        self.label_6.setObjectName("label_6")
        self.label_6.hide()

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 360, 201, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.hide()

        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 410, 201, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.hide()

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 270, 141, 21))
        self.label_5.setObjectName("label_5")
        self.label_5.hide()

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(38, 420, 141, 21))
        self.label_8.setObjectName("label_8")
        self.label_8.hide()

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 310, 201, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.hide()

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 370, 141, 21))
        self.label_7.setObjectName("label_7")
        self.label_7.hide()

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 260, 201, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.hide()

        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(200, 510, 201, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.hide()

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(38, 520, 141, 21))
        self.label_10.setObjectName("label_10")
        self.label_10.hide()

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 470, 141, 21))
        self.label_9.setObjectName("label_9")
        self.label_9.hide()

        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 460, 201, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.hide()

        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(610, 510, 201, 31))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_20.hide()

        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(610, 410, 201, 31))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_18.hide()

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(448, 420, 141, 21))
        self.label_18.setObjectName("label_18")
        self.label_18.hide()

        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(610, 160, 201, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.hide()

        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(610, 360, 201, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_17.hide()

        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(610, 460, 201, 31))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_19.hide()

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(448, 120, 141, 21))
        self.label_12.setObjectName("label_12")
        self.label_12.hide()

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(448, 220, 141, 21))
        self.label_14.setObjectName("label_14")
        self.label_14.hide()

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(450, 170, 141, 21))
        self.label_13.setObjectName("label_13")
        self.label_13.hide()

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(450, 70, 141, 21))
        self.label_11.setObjectName("label_11")
        self.label_11.hide()

        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(610, 210, 201, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.hide()

        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(610, 310, 201, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.hide()

        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(610, 110, 201, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.hide()

        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(610, 60, 201, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.hide()

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(450, 270, 141, 21))
        self.label_15.setObjectName("label_15")
        self.label_15.hide()

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(448, 320, 141, 21))
        self.label_16.setObjectName("label_16")
        self.label_16.hide()

        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(610, 260, 201, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.hide()

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(450, 370, 141, 21))
        self.label_17.setObjectName("label_17")
        self.label_17.hide()

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(448, 520, 141, 21))
        self.label_20.setObjectName("label_20")
        self.label_20.hide()

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(450, 470, 141, 21))
        self.label_19.setObjectName("label_19")
        self.label_19.hide()

        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(200, 600, 191, 51))
        self.lineEdit_21.setObjectName("lineEdit_21")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 570, 811, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(30, 610, 141, 31))
        self.label_21.setObjectName("label_21")

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(420, 600, 141, 51))
        self.save_button.setObjectName("save_button")

        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(590, 600, 141, 51))
        self.clear_button.setObjectName("clear_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_button.setText(_translate("MainWindow", "Открыть"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.save_button.setText(_translate("MainWindow", "Сохранить"))
        self.clear_button.setText(_translate("MainWindow", "Очистить"))
        self.label_21.setText(_translate("MainWindow", "Введите название файла:"))
