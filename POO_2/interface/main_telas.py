import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication

from tela_inicial import Tela_inicial
from tela_cadastro import Tela_cadastro
from tela_busca import Tela_busca

from pessoa import Pessoa
from cadastro import Cadastro

class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_busca = Tela_busca()
        self.tela_busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Ui_Main):

    def __init__(self, parent = None):

        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaBusca)
        self.tela_inicial.pushButton_3.clicked.connect(self.fecharTela)
        self.tela_cadastro.pushButton_2.clicked.connect(self.abrirTelaInicial)
        self.tela_busca.pushButton_2.clicked.connect(self.abrirTelaInicial)


        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastro)
        self.tela_busca.pushButton.clicked.connect(self.botaoBusca)

    def botaoCadastro(self):
        nome = self.tela_cadastro.lineEdit.text()
        endereco = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        data = self.tela_cadastro.lineEdit_4.text()

        if not(nome == '' or endereco == '' or cpf == '' or data == ''):
            p = Pessoa(nome, endereco, cpf, data)

            if (self.cad.cadastro(p)):
                QMessageBox.information(None, 'POO2', 'Cadastro Realizado com sucesso')

                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, 'POO2', 'O CPF informado já foi cadastrado')
        else:
            QMessageBox.information(None, 'POO2', 'Não é permitdo campos em Branco!')

    def botaoBusca(self):
        cpf = self.tela_busca.lineEdit.text()
        pessoa = self.cad.busca(cpf)

        if (pessoa != None):

            self.tela_busca.lineEdit_2.setText(pessoa.nome)
            self.tela_busca.lineEdit_3.setText(pessoa.endereco)
            self.tela_busca.lineEdit_4.setText(pessoa.data)
        else:
            QMessageBox.information(None, 'POO2', 'CPF não encotrado')

    def fecharTela(self):
        QMessageBox.information(None, 'Exit', 'Aplicação Encerrada!')
        exit()

    def abrirTelaInicial(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBusca(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())