# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tela_Cadastro(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(496, 397)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(90, 100, 291, 251))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nome_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.nome_lineEdit.setGeometry(QtCore.QRect(50, 30, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nome_lineEdit.setFont(font)
        self.nome_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome_lineEdit.setText("")
        self.nome_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.cpf_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.cpf_lineEdit.setGeometry(QtCore.QRect(50, 60, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpf_lineEdit.setFont(font)
        self.cpf_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cpf_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.cpf_lineEdit.setObjectName("cpf_lineEdit")
        self.senha_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.senha_lineEdit.setGeometry(QtCore.QRect(50, 90, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.senha_lineEdit.setFont(font)
        self.senha_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.senha_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.senha_lineEdit.setObjectName("senha_lineEdit")
        self.nascimento_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.nascimento_lineEdit.setGeometry(QtCore.QRect(50, 120, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nascimento_lineEdit.setFont(font)
        self.nascimento_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nascimento_lineEdit.setInputMask("")
        self.nascimento_lineEdit.setText("")
        self.nascimento_lineEdit.setMaxLength(32767)
        self.nascimento_lineEdit.setFrame(True)
        self.nascimento_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nascimento_lineEdit.setDragEnabled(False)
        self.nascimento_lineEdit.setReadOnly(False)
        self.nascimento_lineEdit.setObjectName("nascimento_lineEdit")
        self.genero_comboBox = QtWidgets.QComboBox(self.frame)
        self.genero_comboBox.setGeometry(QtCore.QRect(130, 150, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.genero_comboBox.setFont(font)
        self.genero_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.genero_comboBox.setObjectName("genero_comboBox")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.cadastrar_Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_Button.setGeometry(QtCore.QRect(110, 180, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastrar_Button.setFont(font)
        self.cadastrar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_Button.setStyleSheet("QPushButton{\n"
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
        self.cadastrar_Button.setObjectName("cadastrar_Button")
        self.voltar_Button = QtWidgets.QPushButton(self.frame)
        self.voltar_Button.setGeometry(QtCore.QRect(110, 210, 75, 23))
        font = QtGui.QFont()
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
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(180, 30, 101, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("user.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_5 = QtWidgets.QLineEdit(Cadastro)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 80, 21, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.raise_()
        self.frame.raise_()
        self.label.raise_()

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.nome_lineEdit.setPlaceholderText(_translate("Cadastro", "Nome"))
        self.cpf_lineEdit.setPlaceholderText(_translate("Cadastro", "CPF"))
        self.senha_lineEdit.setPlaceholderText(_translate("Cadastro", "Senha"))
        self.nascimento_lineEdit.setPlaceholderText(_translate("Cadastro", "Nascimento"))
        self.genero_comboBox.setItemText(0, _translate("Cadastro", "Masculino"))
        self.genero_comboBox.setItemText(1, _translate("Cadastro", "Feminino"))
        self.genero_comboBox.setItemText(2, _translate("Cadastro", "Outro"))
        self.label_2.setText(_translate("Cadastro", "Genêro"))
        self.cadastrar_Button.setText(_translate("Cadastro", "Cadastrar"))
        self.voltar_Button.setText(_translate("Cadastro", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Ui_Tela_Cadastro()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())

