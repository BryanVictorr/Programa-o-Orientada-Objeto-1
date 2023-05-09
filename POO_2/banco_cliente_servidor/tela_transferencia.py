# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_transferencia.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tela_Transferencia(object):
    def setupUi(self, Transferencia):
        Transferencia.setObjectName("Transferencia")
        Transferencia.resize(348, 268)
        Transferencia.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.label = QtWidgets.QLabel(Transferencia)
        self.label.setGeometry(QtCore.QRect(150, 30, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.saldo_lineEdit = QtWidgets.QLineEdit(Transferencia)
        self.saldo_lineEdit.setEnabled(False)
        self.saldo_lineEdit.setGeometry(QtCore.QRect(130, 50, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.saldo_lineEdit.setFont(font)
        self.saldo_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.saldo_lineEdit.setText("")
        self.saldo_lineEdit.setFrame(False)
        self.saldo_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.saldo_lineEdit.setObjectName("saldo_lineEdit")
        self.lineEdit = QtWidgets.QLineEdit(Transferencia)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.cpf_destino_lineEdit = QtWidgets.QLineEdit(Transferencia)
        self.cpf_destino_lineEdit.setGeometry(QtCore.QRect(150, 80, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.cpf_destino_lineEdit.setFont(font)
        self.cpf_destino_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.cpf_destino_lineEdit.setText("")
        self.cpf_destino_lineEdit.setObjectName("cpf_destino_lineEdit")
        self.label_2 = QtWidgets.QLabel(Transferencia)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.valor_lineEdit = QtWidgets.QLineEdit(Transferencia)
        self.valor_lineEdit.setGeometry(QtCore.QRect(120, 140, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.valor_lineEdit.setFont(font)
        self.valor_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.valor_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.valor_lineEdit.setObjectName("valor_lineEdit")
        self.voltar_Button = QtWidgets.QPushButton(Transferencia)
        self.voltar_Button.setGeometry(QtCore.QRect(140, 200, 75, 23))
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
        self.enviar_Button = QtWidgets.QPushButton(Transferencia)
        self.enviar_Button.setGeometry(QtCore.QRect(140, 170, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.enviar_Button.setFont(font)
        self.enviar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enviar_Button.setStyleSheet("QPushButton{\n"
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
        self.enviar_Button.setObjectName("enviar_Button")

        self.retranslateUi(Transferencia)
        QtCore.QMetaObject.connectSlotsByName(Transferencia)

    def retranslateUi(self, Transferencia):
        _translate = QtCore.QCoreApplication.translate
        Transferencia.setWindowTitle(_translate("Transferencia", "Form"))
        self.label.setText(_translate("Transferencia", "Saldo"))
        self.lineEdit.setText(_translate("Transferencia", "Informe CPF de Destino:"))
        self.label_2.setText(_translate("Transferencia", "Valor do Transferencia"))
        self.voltar_Button.setText(_translate("Transferencia", "Voltar"))
        self.enviar_Button.setText(_translate("Transferencia", "Enviar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Transferencia = QtWidgets.QWidget()
    ui = Ui_Tela_Transferencia()
    ui.setupUi(Transferencia)
    Transferencia.show()
    sys.exit(app.exec_())

