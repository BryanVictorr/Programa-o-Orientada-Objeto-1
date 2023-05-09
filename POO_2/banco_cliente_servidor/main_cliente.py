import sys
import socket
from hashlib import md5

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication

from tela_login import Ui_Tela_Login
from tela_cadastro import Ui_Tela_Cadastro
from tela_menu import Ui_Tela_Menu
from tela_deposito import Ui_Tela_Deposito
from tela_saque import Ui_Tela_Saque
from tela_transferencia import Ui_Tela_Transferencia
from tela_historico import Ui_Tela_Extrato

ip = host = socket.gethostbyname(socket.gethostname())
port = 8080
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(addr)
except:
    print("\nNao foi possivel ser conectar ao servidor!\n")
    exit()

class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Ui_Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_menu = Ui_Tela_Menu()
        self.tela_menu.setupUi(self.stack2)

        self.tela_deposito = Ui_Tela_Deposito()
        self.tela_deposito.setupUi(self.stack3)

        self.tela_saque = Ui_Tela_Saque()
        self.tela_saque.setupUi(self.stack4)

        self.tela_transferencia = Ui_Tela_Transferencia()
        self.tela_transferencia.setupUi(self.stack5)

        self.tela_historico = Ui_Tela_Extrato()
        self.tela_historico.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, Ui_Main):

    login = list()

    def __init__(self, parent = None):

        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.tela_login.login_Button.clicked.connect(self.botaoLogin)
        self.tela_login.nova_conta_Button.clicked.connect(self.abrirTelaCadastro)
        self.tela_login.sair_Button.clicked.connect(self.encerrar)

        self.tela_cadastro.cadastrar_Button.clicked.connect(self.botaoCadastro)
        self.tela_cadastro.voltar_Button.clicked.connect(self.abrirTelaLogin)

        self.tela_menu.sair_Button.clicked.connect(self.abrirTelaLogin) 
        self.tela_menu.deposito_Button.clicked.connect(self.abrirTelaDeposito)
        self.tela_menu.saque_Button.clicked.connect(self.abrirTelaSaque)
        self.tela_menu.transferencia_Button.clicked.connect(self.abrirTelaTransferencia)
        self.tela_menu.extrato_Button.clicked.connect(self.abrirTelaExtrato)

        self.tela_deposito.depositar_Button.clicked.connect(self.botaoDepositar)
        self.tela_deposito.voltar_Button.clicked.connect(self.abrirTelaMenu)

        self.tela_saque.sacar_Button.clicked.connect(self.botaoSaque)
        self.tela_saque.voltar_Button.clicked.connect(self.abrirTelaMenu)

        self.tela_transferencia.enviar_Button.clicked.connect(self.botaoTransfere)
        self.tela_transferencia.voltar_Button.clicked.connect(self.abrirTelaMenu)

        self.tela_historico.voltar_Button.clicked.connect(self.abrirTelaMenu)

    def botaoCadastro(self):

        nome = self.tela_cadastro.nome_lineEdit.text()
        cpf = self.tela_cadastro.cpf_lineEdit.text()
        senha = self.tela_cadastro.senha_lineEdit.text()
        nascimento = self.tela_cadastro.nascimento_lineEdit.text()
        genero = self.tela_cadastro.genero_comboBox.currentText()

        if not(nome == '' or cpf == '' or senha == '' or nascimento == ''):

            client_socket.send('1'.encode())

            self.tela_cadastro.nome_lineEdit.setText('')
            self.tela_cadastro.cpf_lineEdit.setText('')
            self.tela_cadastro.senha_lineEdit.setText('')
            self.tela_cadastro.nascimento_lineEdit.setText('')
            self.tela_cadastro.genero_comboBox.setCurrentIndex(0)

            senha = senha.encode("utf8")
            senha = md5(senha).hexdigest()

            lista_de_dados = []
            lista_de_dados.append(nome)
            lista_de_dados.append(cpf)
            lista_de_dados.append(senha)
            lista_de_dados.append(nascimento)
            lista_de_dados.append(genero)
            dados = ",".join(lista_de_dados)
            client_socket.send(dados.encode())

            try:
                retorno = client_socket.recv(4096).decode()
            except:
                print("\nNao foi possivel permanecer conectado!\n")
                print("\nnPressione <Enter> para continuar...")
                client_socket.close()

            if(retorno == '1'):
                QMessageBox.information(None, 'Aviso', 'Cadastro Realizado com sucesso')
                self.abrirTelaLogin()

            elif(retorno == '0'):
                QMessageBox.information(None, 'Aviso', 'O CPF informado já foi cadastrado')
                self.abrirTelaLogin()
        else:
            QMessageBox.information(None, 'Aviso', 'Não é permitdo campos em Branco!')

    def botaoLogin(self):

        cpf = self.tela_login.cpf_lineEdit.text()
        senha = self.tela_login.senha_lineEdit.text()

        if not(cpf == '' or senha == ''):

            client_socket.send('2'.encode())

            senha = senha.encode("utf8")
            senha = md5(senha).hexdigest()

            lista_de_dados = []
            lista_de_dados.append(cpf)
            lista_de_dados.append(senha)
            dados = ",".join(lista_de_dados)
            client_socket.send(dados.encode())
            dados = client_socket.recv(4096).decode()

            if (dados != '1' and dados != '0'):

                Main.login = dados.split(',')
                nome = Main.login[0].split(" ",2)
                self.tela_menu.cliente_lineEdit.setText("Olá, " + nome[0])
                self.abrirTelaMenu()

            elif (dados == '0'):
                QMessageBox.information(None, 'Aviso', 'CPF não cadastrado!')

            elif (dados == '1'):
                QMessageBox.information(None, 'Aviso', 'Senha incorreta!')
        else:
            QMessageBox.information(None, 'Aviso', 'Não é permitdo campos em Branco!')
        
        self.tela_login.cpf_lineEdit.setText('')
        self.tela_login.senha_lineEdit.setText('')

    def botaoDepositar(self):

        if not(self.tela_deposito.valor_lineEdit.text() == ""):

            client_socket.send('3'.encode())
            lista_de_deposito = []

            valor_deposito = self.tela_deposito.valor_lineEdit.text()

            lista_de_deposito.append(valor_deposito)
            lista_de_deposito.append(Main.login[1])
            lista_de_deposito = ",".join(lista_de_deposito)
            client_socket.send(lista_de_deposito.encode())
            retorno = client_socket.recv(4096).decode()

            if(retorno == '0'):

                QMessageBox.information(None, 'Aviso', 'Deposito realizado com sucesso!')
                novo_saldo = float(Main.login[5]) + float(valor_deposito)
                Main.login[5] = str(novo_saldo)

            else:
                QMessageBox.information(None, 'Aviso', 'Informe valor Valido!')
        else:
            QMessageBox.information(None, 'Aviso', 'valor em Branco!')

        self.tela_deposito.valor_lineEdit.setText("")
        self.tela_deposito.saldo_lineEdit.setText("R$" + Main.login[5])

    def botaoSaque(self):

        if not(self.tela_saque.valor_lineEdit.text() == ""):

            client_socket.send('4'.encode())
            lista_de_saque = []

            valor_saque = self.tela_saque.valor_lineEdit.text()

            lista_de_saque.append(valor_saque)
            lista_de_saque.append(Main.login[1])
            lista_de_saque = ",".join(lista_de_saque)
            client_socket.send(lista_de_saque.encode())
            retorno = client_socket.recv(4096).decode()

            if(retorno == '0'):

                QMessageBox.information(None, 'Aviso', 'Saque realizado com sucesso!')
                novo_saldo = float(Main.login[5]) - float(valor_saque)
                Main.login[5] = str(novo_saldo)

            else:
                QMessageBox.information(None, 'Aviso', 'Infome valor invalido!')
        else:
            QMessageBox.information(None, 'Aviso', 'valor em Branco!')

        self.tela_saque.saldo_lineEdit.setText("R$" + Main.login[5])
        self.tela_saque.valor_lineEdit.setText("")

    def botaoTransfere(self):

        cpf_destino = self.tela_transferencia.cpf_destino_lineEdit.text()
        valor = self.tela_transferencia.valor_lineEdit.text()

        if not(cpf_destino == "" and valor == ""):

            client_socket.send('5'.encode())
            lista_de_transferencia = []

            lista_de_transferencia.append(valor)
            lista_de_transferencia.append(Main.login[1])
            lista_de_transferencia.append(cpf_destino)
            lista_de_transferencia = ",".join(lista_de_transferencia)

            client_socket.send(lista_de_transferencia.encode())
            retorno = client_socket.recv(4096).decode()

            if(retorno == '0'):

                QMessageBox.information(None, 'Aviso', 'Transferencia realizada com sucesso!')
                novo_saldo = float(Main.login[5]) - float(valor)
                Main.login[5] = str(novo_saldo)

            elif(retorno == '1'):
                QMessageBox.information(None, 'Aviso', 'Conta Invalida!')

            elif(retorno == '2'):
                QMessageBox.information(None, 'Aviso', 'Informe valor valido!')
        else:
            QMessageBox.information(None, 'Aviso', 'Não é permitido campos em branco!')

        self.tela_transferencia.cpf_destino_lineEdit.setText("")
        self.tela_transferencia.valor_lineEdit.setText("")
        self.tela_transferencia.saldo_lineEdit.setText("R$" + Main.login[5])

    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaMenu(self):
        self.tela_menu.saldo_lineEdit.setText("R$ "+ Main.login[5])
        self.QtStack.setCurrentIndex(2)

    def abrirTelaDeposito(self):
        self.tela_deposito.saldo_lineEdit.setText("R$" + Main.login[5])
        self.QtStack.setCurrentIndex(3)

    def abrirTelaSaque(self):
        self.tela_saque.saldo_lineEdit.setText("R$" + Main.login[5])
        self.QtStack.setCurrentIndex(4)

    def abrirTelaTransferencia(self):
        self.tela_transferencia.saldo_lineEdit.setText("R$" + Main.login[5])
        self.QtStack.setCurrentIndex(5)

    def abrirTelaExtrato(self):

        client_socket.send('6'.encode())
        client_socket.send(Main.login[1].encode())

        historico = client_socket.recv(4096).decode()

        if (historico != '0'):
            historico = historico.replace(",","\n")
        else:
            historico = 'Nao foi realizado operacões!'

        self.tela_historico.extrato_Edit.setText(historico)
        self.QtStack.setCurrentIndex(6)

    def encerrar(self):
        client_socket.send('0'.encode())
        client_socket.close()
        exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())