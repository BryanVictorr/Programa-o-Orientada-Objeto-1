# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_saque.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tela_Saque(object):
    def setupUi(self, Saque):
        Saque.setObjectName("Saque")
        Saque.resize(342, 240)
        Saque.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.sacar_Button = QtWidgets.QPushButton(Saque)
        self.sacar_Button.setGeometry(QtCore.QRect(130, 140, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.sacar_Button.setFont(font)
        self.sacar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sacar_Button.setStyleSheet("QPushButton{\n"
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
        self.sacar_Button.setObjectName("sacar_Button")
        self.label = QtWidgets.QLabel(Saque)
        self.label.setGeometry(QtCore.QRect(140, 30, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Saque)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.saldo_lineEdit = QtWidgets.QLineEdit(Saque)
        self.saldo_lineEdit.setEnabled(False)
        self.saldo_lineEdit.setGeometry(QtCore.QRect(140, 50, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.saldo_lineEdit.setFont(font)
        self.saldo_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.saldo_lineEdit.setText("")
        self.saldo_lineEdit.setFrame(False)
        self.saldo_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.saldo_lineEdit.setObjectName("saldo_lineEdit")
        self.valor_lineEdit = QtWidgets.QLineEdit(Saque)
        self.valor_lineEdit.setGeometry(QtCore.QRect(110, 110, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.valor_lineEdit.setFont(font)
        self.valor_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.valor_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.valor_lineEdit.setObjectName("valor_lineEdit")
        self.voltar_Button = QtWidgets.QPushButton(Saque)
        self.voltar_Button.setGeometry(QtCore.QRect(130, 170, 75, 23))
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

        self.retranslateUi(Saque)
        QtCore.QMetaObject.connectSlotsByName(Saque)

    def retranslateUi(self, Saque):
        _translate = QtCore.QCoreApplication.translate
        Saque.setWindowTitle(_translate("Saque", "Form"))
        self.sacar_Button.setText(_translate("Saque", "Sacar"))
        self.label.setText(_translate("Saque", "Saldo"))
        self.label_2.setText(_translate("Saque", "Valor do Saque"))
        self.voltar_Button.setText(_translate("Saque", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Saque = QtWidgets.QWidget()
    ui = Ui_Tela_Saque()
    ui.setupUi(Saque)
    Saque.show()
    sys.exit(app.exec_())

