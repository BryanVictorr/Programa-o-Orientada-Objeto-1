import mysql.connector
from cliente import Cliente
from datetime import date

class Cadastro():

    __slots__ = ['_conexao','_cursor','_mysql']

    def __init__(self):

        self._conexao = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'banco')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS contas(nome varchar(30) NOT NULL,cpf varchar(14) PRIMARY KEY, senha varchar(50) NOT NULL, nascimento varchar(50) NOT NULL,genero varchar(20) NOT NULL, saldo varchar(20) NOT NULL)"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()

        self._mysql = """CREATE TABLE IF NOT EXISTS historico(cpf varchar(11) PRIMARY KEY, extrato varchar(10000))"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()

    def cadastro(self, cliente):

        dados = self.busca(cliente.cpf)

        if(dados == None):

            self._cursor.execute('INSERT INTO contas(nome,cpf,senha,nascimento,genero,saldo) VALUES(%s,%s,%s,%s,%s,%s)',(cliente.nome,cliente.cpf,cliente.senha
            ,cliente.nascimento,cliente.genero,cliente.saldo))
            self._conexao.commit()

            self._cursor.execute('INSERT INTO historico(cpf, extrato) VALUES(%s,%s)',(cliente.cpf, ""))
            self._conexao.commit()
            return True
        else:
            return False

    def busca(self, cpf):
        self._cursor.execute('SELECT * from contas WHERE cpf = %s',(cpf,))
        dados = self._cursor.fetchone()
        
        if(dados == None):
            return None
        else:
            cliente = Cliente(dados[0],dados[1],dados[2],dados[3],dados[4],float(dados[5]))
            return cliente

    def login(self, cpf, senha):

        objeto_login = self.busca(cpf)

        if(objeto_login.senha == senha):
            return objeto_login

        return None

    def deposito(self, cpf, valor):

        self._cursor.execute('UPDATE contas SET saldo = %s WHERE cpf = %s', (str(valor),cpf))
        self._conexao.commit()

    def saque(self, cpf, valor):

        self._cursor.execute('UPDATE contas SET saldo = %s WHERE cpf = %s', (str(valor),cpf))
        self._conexao.commit()

    def historico_deposito(self, cpf, valor):

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf,))
        dados = self._cursor.fetchone()

        data = date.today().strftime('%d/%m/%Y')
        extrato = "{}Deposito realizado de R$ {} - {},".format(dados[1],valor,data)

        self._cursor.execute('UPDATE historico SET extrato = %s WHERE cpf = %s', (extrato,cpf,))
        self._conexao.commit()

    def historico_saque(self, cpf, valor):

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf,))
        dados = self._cursor.fetchone()

        data = date.today().strftime('%d/%m/%Y')
        extrato = "{}Saque realizado de R$ {} - {},".format(dados[1],valor,data)

        self._cursor.execute('UPDATE historico SET extrato = %s WHERE cpf = %s', (extrato,cpf,))
        self._conexao.commit()

    def historico_transferencia(self, cpf_envio, cpf_destino, valor):

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf_envio,))
        dados = self._cursor.fetchone()

        data = date.today().strftime('%d/%m/%Y')
        extrato_envio = "{}Transferencia enviada de R${} - {},".format(dados[1],valor,data)

        self._cursor.execute('UPDATE historico SET extrato = %s WHERE cpf = %s', (extrato_envio,cpf_envio,))
        self._conexao.commit()

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf_destino,))
        dados = self._cursor.fetchone()

        data = date.today().strftime('%d/%m/%Y')
        extrato_destino = "{}Transferencia recebida de R${} - {},".format(dados[1],valor,data)
        self._cursor.execute('UPDATE historico SET extrato = %s WHERE cpf = %s', (extrato_destino,cpf_destino,))
        self._conexao.commit()

    def historico(self, cpf):

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf,))
        dados = self._cursor.fetchone()
        historico = dados[1]

        if(historico != ""):
            return historico
        else:
            return '0'