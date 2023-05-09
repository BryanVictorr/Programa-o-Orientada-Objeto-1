# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_deposito.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tela_Deposito(object):
    def setupUi(self, Deposito):
        Deposito.setObjectName("Deposito")
        Deposito.resize(345, 242)
        Deposito.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.valor_lineEdit = QtWidgets.QLineEdit(Deposito)
        self.valor_lineEdit.setGeometry(QtCore.QRect(100, 120, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.valor_lineEdit.setFont(font)
        self.valor_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.valor_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.valor_lineEdit.setObjectName("valor_lineEdit")
        self.saldo_lineEdit = QtWidgets.QLineEdit(Deposito)
        self.saldo_lineEdit.setEnabled(True)
        self.saldo_lineEdit.setGeometry(QtCore.QRect(110, 60, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.saldo_lineEdit.setFont(font)
        self.saldo_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.saldo_lineEdit.setText("")
        self.saldo_lineEdit.setFrame(False)
        self.saldo_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.saldo_lineEdit.setObjectName("saldo_lineEdit")
        self.label = QtWidgets.QLabel(Deposito)
        self.label.setGeometry(QtCore.QRect(130, 40, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Deposito)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.depositar_Button = QtWidgets.QPushButton(Deposito)
        self.depositar_Button.setGeometry(QtCore.QRect(120, 150, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.depositar_Button.setFont(font)
        self.depositar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.depositar_Button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.depositar_Button.setObjectName("depositar_Button")
        self.voltar_Button = QtWidgets.QPushButton(Deposito)
        self.voltar_Button.setGeometry(QtCore.QRect(120, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.voltar_Button.setFont(font)
        self.voltar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voltar_Button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.voltar_Button.setObjectName("voltar_Button")

        self.retranslateUi(Deposito)
        QtCore.QMetaObject.connectSlotsByName(Deposito)

    def retranslateUi(self, Deposito):
        _translate = QtCore.QCoreApplication.translate
        Deposito.setWindowTitle(_translate("Deposito", "Form"))
        self.label.setText(_translate("Deposito", "Saldo"))
        self.label_2.setText(_translate("Deposito", "Valor do Deposito"))
        self.depositar_Button.setText(_translate("Deposito", "Depositar"))
        self.voltar_Button.setText(_translate("Deposito", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Deposito = QtWidgets.QWidget()
    ui = Ui_Tela_Deposito()
    ui.setupUi(Deposito)
    Deposito.show()
    sys.exit(app.exec_())

