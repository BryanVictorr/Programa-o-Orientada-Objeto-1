import abc
from datetime import datetime

lista_funcionarios = {}
lista_clientes = {}
lista_corrente = {}
lista_poupanca = {}
lista_seguro = {}
lista_tributacao = {}
lista_transacoes_correntes = {}
lista_transacoes_poupanca = {}

class Usuario(abc.ABC):
    
    def __init__(self,nome,cpf,data_nascimento):
        
        '''Interface Responsável pelo Cadastro de Usuários'''
        
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        
    @abc.abstractmethod
    def __str__(self):
        pass
  
class Funcionario(Usuario):
    
    def __init__(self,nome,cpf,data_nascimento,salario):
        
        '''Classe Responsável pelo Cadastro de Funcionária'''
        
        self._salario = salario
        
        super().__init__(nome,cpf,data_nascimento)
        
        lista_funcionarios[self._cpf] = [self._nome,self._data_nascimento,self._salario]
        
    def __str__(self):
        
        '''Exibir Funcionarios Cadastrados'''
        
        return "Nome:{}\nCPF:{}\nData Nascimento:{}\nSalario:{}".format(self._nome,self._cpf,self._data_nascimento,self._salario)

class Cliente(Usuario):
    
    def __init__(self,nome,cpf,data_nascimento,profissao,renda):
        
        '''Classe Responsável pelo Cadastro de Clientes'''
        
        self._profissao = profissao
        self._renda = renda
        
        super().__init__(nome,cpf,data_nascimento)
        
        lista_clientes[self._cpf] = [self._nome,self._data_nascimento,self._profissao,self._renda]
        
    def __str__(self):
        
        '''Exibir Clientes Cadastrados'''
        
        return "Nome:{}\nCPF:{}\nData Nascimento:{}\nProfissão:{}\nRenda:{}".format(self._nome,self._cpf,self._data_nascimento,self._profissao,self._renda)

def AlterarSaldo(cpf,valor,tipo,operacao):
    
    """Realiza as Operações Saque,Deposito e Transferência"""
    """Armazena valores alterados no Saldo"""
    
    if operacao == 1:
        
        if tipo == 1:
            
            for key,value in lista_corrente.items():
                if cpf == key:
            
                    if valor <= value[2]:
                        
                        lista_corrente[cpf][2] = value[2] - valor
                        lista_transacoes_correntes[cpf].append("Saque")
                        lista_transacoes_correntes[cpf].append(valor)
                        
                        data_e_hora_atual = datetime.now()
                        data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')
            
                        dataAtual = data_e_hora
                        lista_transacoes_correntes[cpf].append(dataAtual)
                    
                        return True
                        
                    else:
                        return False
                        
        elif tipo == 2:
            
            for key,value in lista_poupanca.items():
                if cpf == key:
                    
                    if valor <= value[2]:
                        
                        lista_poupanca[cpf][2] = value[2] - valor
                        lista_transacoes_poupanca[cpf].append("Saque")
                        lista_transacoes_poupanca[cpf].append(valor)
                        
                        data_e_hora_atual = datetime.now()
                        data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')
            
                        dataAtual = data_e_hora
                        lista_transacoes_poupanca[cpf].append(dataAtual)
                        
                        return True
                        
                    else:
                        return False
                        
    if operacao == 2:
        
        if tipo == 1:
        
            for key,value in lista_corrente.items():
                if cpf == key:
                    
                    lista_corrente[cpf][2] = value[2] + valor
                    lista_transacoes_correntes[cpf].append("Depósito")
                    lista_transacoes_correntes[cpf].append(valor)
                        
                    data_e_hora_atual = datetime.now()
                    data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')
            
                    dataAtual = data_e_hora
                    lista_transacoes_correntes[cpf].append(dataAtual)
                    
                    return True

        if tipo == 2:
            
            for key,value in lista_poupanca.items():
                if cpf == key:
                    
                    lista_poupanca[cpf][2] = value[2] + valor
                    lista_transacoes_poupanca[cpf].append("Depósito")
                    lista_transacoes_poupanca[cpf].append(valor)
                    
                    data_e_hora_atual = datetime.now()
                    data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')
            
                    dataAtual = data_e_hora
                    lista_transacoes_poupanca[cpf].append(dataAtual)
                    
                    return True

def OperacaoConta(cpf,operacao):
    
    """Chama as Operações de Saque,Deposito e Transferência"""
    
    print("\n" * 10)
    valor = float(input("\nInforme Valor:"))
    retorno = ""
    
    if cpf in lista_corrente.keys() and cpf in lista_poupanca.keys():
        
        tipo = int(input("1-Corrente\n2-Poupança\n"))
        
        if tipo == 1:
            
            if operacao == 1:
                
                retorno = Conta.set_sacar(cpf,valor,tipo)
                
            elif operacao == 2:
                
                retorno = Conta.set_depositar(cpf,valor,tipo)
                
            elif operacao == 3:
                
                destino = input("Cpf de Destino:")
                
                retorno = Conta.set_transferir(cpf,destino,valor,tipo)
     
        elif tipo == 2:
            
            if operacao == 1:
                
                retorno = Conta.set_sacar(cpf,valor,tipo)
                
            elif operacao == 2:
                
                retorno = Conta.set_depositar(cpf,valor,tipo)
                
            elif operacao == 3:
                
                destino = input("Cpf de Destino:")
                
                retorno = Conta.set_transferir(cpf,destino,valor,tipo)
   
    elif cpf in lista_corrente.keys():
        
        tipo = 1
        
        if operacao == 1:
            
            retorno = Conta.set_sacar(cpf,valor,tipo)
            
        elif operacao == 2:
            
            retorno = Conta.set_depositar(cpf,valor,tipo)
            
        elif operacao == 3:
            
            destino = input("Cpf de Destino:")
            
            retorno = Conta.set_transferir(cpf,destino,valor,tipo)
    
    elif cpf in lista_poupanca.keys():
        
        tipo = 2
        
        if operacao == 1:
            
            retorno = Conta.set_sacar(cpf,valor,tipo)
            
        elif operacao == 2:
            
            retorno = Conta.set_depositar(cpf,valor,tipo)
            
        elif operacao == 3:
            
            destino = input("Cpf de Destino:")
            
            retorno = Conta.set_transferir(cpf,destino,valor,tipo)

    return retorno

def SaldoContas(cpf):
    
    """Faz a Consulta de Saldo na Conta"""
    
    if cpf in lista_corrente.keys() and cpf in lista_poupanca.keys():
        
        print("\n" * 10)
        print("Cliente:",lista_poupanca[cpf][0])
        print("Saldo Conta Corrente:",lista_corrente[cpf][2])
        print("Saldo Poupança:",lista_poupanca[cpf][2])
        
    elif cpf in lista_corrente.keys():
        
        print("\n" * 10)
        print("Cliente:",lista_corrente[cpf][0])
        print("Saldo Conta Corrente:",lista_corrente[cpf][2])
        
    elif cpf in lista_poupanca.keys():
        
        print("\n" * 10)
        print("Cliente:",lista_corrente[cpf][0])
        print("Saldo Conta Poupança:",lista_poupanca[cpf][2])
        
    else:
        print("Cpf não possui conta no banco!")

def TributacoesConta(cpf):
    
    """Mostrar quanto foi cobrado em cada Tributação"""
    
    aux = 1
    tam = len(lista_tributacao[cpf])
    
    if tam >= 2:
        
        print("\n" * 10)
        
        for key,value in lista_tributacao.items():
            for x in range(0, len(value), 1):
                
                if cpf == key:
                    
                    print("{} Tributação foi de {} Reais".format(aux,value[x]))
                    
                    aux += 1

def registros(cpf,tipo):
    
    """Faz o Controle do Registro de Operações na Conta"""
    
    aux = 1
    print("\n" * 10)
    
    if tipo == 1:
        
        for key,value in lista_transacoes_correntes.items():
            for x in range(0, len(value), 3):
                
                if cpf == key:
                    
                    print("\nTransação {}\nOperação:{}\nValor:{}\nData:{}".format(aux,value[x],value[x+1],value[x+2]))
                    
                    aux += 1

    elif tipo == 2:
        
        for key,value in lista_transacoes_poupanca.items():
            for x in range(0, len(value), 3):
                
                if cpf == key:
                    
                    print("\nTransação {}\nOperação:{}\nValor:{}\nData:{}".format(aux,value[x],value[x+1],value[x+2]))
                
                    aux += 1

def banco(tipo):
    
    if tipo == 1:
        
        for key,value in lista_funcionarios.items():
            
            print("Nome:",value[0])
            print("CPF:",key)
            print("Salário:",value[2])
            print("Data de Nascimento:",value[1])
            
            print("\n \n")
    
    if tipo == 2:
        
        for cpf_1,value in lista_clientes.items():
        
            print("Nome:",value[0])
            print("CPF:",cpf_1)
            print("Profissâo:",value[2])
            print("Data de Nascimento:",value[1])
            print("Renda",value[3])
        
            for cpf_2,value in lista_corrente.items():
            
                if cpf_1 == cpf_2:
            
                    print("Conta:",value[4])
                    print("Saldo:",value[2])
            
            for cpf_3,value in lista_poupanca.items():
            
                if cpf_1 == cpf_3:
                
                    print("Conta:",value[4])
                    print("Saldo:",value[2])
        
            for cpf_4,value in lista_seguro.items():
            
                if cpf_1 == cpf_4:
                
                    quant = len(lista_seguro[cpf_4])
                    quant = (quant - 1) / 2
                
                    print("Quantidade de Seguros de Vida:",quant)
        
            print("\n\n")

class Conta(abc.ABC):
    
    """Classe Abstrata que implementa dados e operações da Conta"""
    
    def __init__(self,cpf,numero,saldo,historico_abertura):
        
        self._cpf = cpf
        self._numero = numero
        self._saldo = saldo
        self._historico_abertura = historico_abertura
    
    def set_sacar(cpf,valor,tipo):
        
        operacao = 1
        
        retorno = AlterarSaldo(cpf,valor,tipo,operacao)
        
        return retorno
        
    def set_depositar(cpf,valor,tipo):
        
        operacao = 2
        
        retorno = AlterarSaldo(cpf,valor,tipo,operacao)
        
        return retorno

    def set_transferir(cpf,destino,valor,tipo):
        
        retorno = Conta.set_sacar(cpf,valor,tipo)
        
        if retorno != False:
            
            Conta.set_depositar(destino,valor,tipo)
            
            return True
            
        else:
            return False

class ContaCorrente(Conta):
    
    """Classe Responsável por abrir Conta Corrente"""
  
    def __init__(self,cpf,nome,numero,saldo,historico_abertura):
        
        self._tipo = "Corrente"
        self._nome = nome
        
        super().__init__(cpf,numero,saldo,historico_abertura)
        
        lista_corrente[cpf] = [self._nome,self._numero,self._saldo,self._historico_abertura,self._tipo]
        
    def get_tributacao(cpf):
        
        novo_saldo = 0
        
        for key,value in lista_corrente.items():
            
            if cpf == key:
                
                novo_saldo = value[2]
                novo_saldo = novo_saldo * 0.01
                break
            
        if novo_saldo == 0:
            return False
            
        return novo_saldo

class ContaPoupanca(Conta):
    
    """Classe Responsável por abrir Conta Poupança"""
    
    def __init__(self,cpf,nome,numero,saldo,historico_abertura):
        
        self._tipo = "Poupança"
        self._nome = nome
        
        super().__init__(cpf,numero,saldo,historico_abertura)
        
        lista_poupanca[cpf] = [self._nome,self._numero,self._saldo,self._historico_abertura,self._tipo]

class SeguroDeVida():
    
    """Classe Responsável por abrir Seguro de Vida"""
    
    def __init__(self,cpf,nome,valor_mensal,valor_total):
        
        self._cpf = cpf
        self._nome = nome
        self._valor_mensal = valor_mensal
        self._valor_total = valor_total
        
        if self._cpf not in lista_seguro.keys():
            
            lista_seguro[self._cpf] = [self._nome,self._valor_mensal,self._valor_total]
            
        else:
            
            lista_seguro[self._cpf].append(self._valor_mensal)
            lista_seguro[self._cpf].append(self._valor_total)
        
    def get_tributacao(cpf):
        
        taxa = 0
        
        for key,value in lista_seguro.items():
            
            for x in range(0, len(value) - 1, 2):
                
                if cpf == key:
                    
                    taxa += (value[x+1]  * 0.02) + 10
                    
        if taxa == 0:
            return False
            
        else:
            return taxa

class CobrarTributacao(abc.ABC):
    
    """Interface que cobrar taxa na conta corrente e seguro de vida"""
    
    @abc.abstractmethod
    def get_tributacao():
        pass
    
def Menu(opcao):
    
    if opcao == 1:
        
        '''Cadastro de Funcionários'''
        
        print("\n" * 10)
        cpf = input("CPF do Funcionário:")
        
        if cpf not in lista_funcionarios.keys():
            
            nome = input("Nome do Funcionário:")
            data_nascimento = input("Data de Nascimento:")
            salario = float(input("Salário:"))
            funcionario = Funcionario(nome,cpf,data_nascimento,salario)
            
            print(funcionario)
            print("\nFuncionario foi Cadastrado!\n")
        
        else:
            print("\nJá existe funcionário associado a esse CPF")
    
    if opcao == 2:
        
        '''Cadastro de Clientes'''
        
        print("\n" * 10)
        cpf = input("CPF do Cliente:")
        
        if cpf not in lista_clientes.keys():
            
            nome = input("Nome do Cliente:")
            data_nascimento = input("Data de Nascimento:")
            profissao = input("Profissão:")
            renda = float(input("Renda:"))
            cliente = Cliente(nome,cpf,data_nascimento,profissao,renda)
            
            print(cliente)
            print("\nCliente foi Cadastrado!")
            
        else:
            print("\nJá existe cliente associado ao CPF")

    if opcao == 3:
        
        '''Abertura Conta Corrente'''
        
        print("\n" * 10)
        cpf = input("Informe o CPF do Cliente:")
        nome = "str"
        
        if cpf in lista_clientes.keys():
            
            if cpf not in lista_corrente.keys():
            
                numero = input("Informe o Número da Conta:")
                saldo = float(input("Saldo da Conta:"))
                
                for key,value in lista_clientes.items():
                    
                    if cpf == key:
                        
                        nome = value[0]
                        break
                    
                data_e_hora_atual = datetime.now()
                data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')
                
                historico_abertura = data_e_hora
                conta_corrente = ContaCorrente(cpf,nome,numero,saldo,historico_abertura)
                
                lista_transacoes_correntes[cpf] = []
                
                print("\nConta Corrente Aberta!")
                
            else:
                print("\nCPF já associado a uma conta corrente")
                
        else:
            print("\nCliente não cadastrado")

    if opcao == 4:
        
        '''Abertura Conta Poupança'''
        
        print("\n" * 10)
        cpf = input("Informe o CPF do Cliente:")
        nome = "str"
        
        if cpf in lista_clientes.keys():
            
            if cpf not in lista_poupanca.keys():
                
                numero = input("Informe o Número da Conta:")
                saldo = float(input("Saldo da Conta:"))
                
                for key,value in lista_clientes.items():
                    
                    if cpf == key:
                        
                        nome = value[0]
                        break
                    
                data_e_hora_atual = datetime.now()
                data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')
                
                historico_abertura = data_e_hora
                conta_poupanca = ContaPoupanca(cpf,nome,numero,saldo,historico_abertura)
                
                lista_transacoes_poupanca[cpf] = []
                
                print("\nConta Poupança Aberta")
            
            else:
                print("\nCPF já associado a conta poupança")
                
        else:
            print("\nCliente não cadastrado")
    
    if opcao == 5:
        
        '''Realiza Saque,Depósito e Transferência'''
        
        print("\n" * 10)
        print("1-Saque")
        print("2-Depósito")
        print("3-Transferência")
        operacao = int(input(""))
        
        cpf = input("CPF associado a Conta:")
        
        retorno = OperacaoConta(cpf,operacao)
        
        if operacao == 1:
            
            if retorno == True:
                print("\nSaque Realizado com Sucesso!")
                
            elif retorno == False:
                print("\nSaldo insuficiente!")
                
            else:
                print("\nCPF Inválido!")
        
        if operacao == 2:
            
            if retorno == True:
                print("\nDepósito Realizado com Sucesso!")
                
            else:
                print("\nCPF Inválido!")
        
        if operacao == 3:
            
            if retorno == True:
                print("\nTransferência Realizada com Sucesso!")
                
            elif retorno == False:
                print("\nSaldo Insuficiente!")
                
            else:
                print("\nCPF Inválido!")
    
    if opcao == 6:
        
        print("\n" * 10)
        cpf = input("Informe o CPF do Cliente:")
        
        if cpf in lista_clientes.keys():
            
            valor_mensal = float(input("Informe o Valor Mensal:"))
            valor_total = float(input("Valor Total do Seguro:"))
            
            for key,value in lista_clientes.items():
                
                if cpf == key:
                    
                    nome = value[0]
                    break
            
            seguro_de_vida = SeguroDeVida(cpf,nome,valor_mensal,valor_total)
            
            print("\nSeguro aberto!")
            
        else:
            print("\nCliente não cadastrado")

    if opcao == 7:
        
        taxa_corrente = 0
        taxa_seguro = 0
        
        """Faz tributação da Conta corrente e seguro de vida"""
        
        print("\n" * 10)
        cpf = input("Informe o CPF para cobrança de Taxas:")
        
        if cpf in lista_corrente.keys():
            
           taxa_corrente = ContaCorrente.get_tributacao(cpf)
           lista_corrente[cpf][2] = lista_corrente[cpf][2] - taxa_corrente
           
           print("\nValor cobrado da Conta Corrente:{}".format(taxa_corrente))
           
        else:
            print("\nCliente não possui Conta Corrente!")
           
        if cpf in lista_seguro.keys():
            
            if cpf in lista_corrente.keys():
                
                taxa_seguro = SeguroDeVida.get_tributacao(cpf)
                lista_corrente[cpf][2] = lista_corrente[cpf][2] - taxa_seguro
                
                print("\nValor cobrado em base do Seguro de vida:{}".format(taxa_seguro))
                
            else:
                print("\nNão é possível cobrar Tributação pois cliente não possui Conta Corrente!")

        else:
            print("\nCliente não possui Seguro de Vida!")
        
        taxa_total = taxa_corrente + taxa_seguro
        
        if taxa_total!= 0:
            
            if cpf not in lista_tributacao.keys():
                
                lista_tributacao[cpf] = [taxa_total]
                
            elif cpf in lista_tributacao.keys():
                
                lista_tributacao[cpf].append(taxa_total)
                
            TributacoesConta(cpf)

    if opcao == 8:
        
        """Consulta Movimentação da Conta"""
        
        print("\n" * 10)
        cpf = input("Informe o CPF para Consulta:")
        
        if cpf in lista_corrente.keys() and cpf in lista_poupanca.keys():
            
            tipo = int(input("\n1-Corrente\n2-Poupança"))
            
            registros(cpf,tipo)
            
        elif cpf in lista_corrente.keys():
            
            tipo = 1
            
            registros(cpf,tipo)
        
        elif cpf in lista_poupanca.keys():
            
            tipo = 2
            
            registros(cpf,tipo)
        
        else:
            print("\nSem Conta associada ao CPF")

    if opcao == 9:
        
        """Consulta Saldo na Conta do Cliente"""
        
        print("\n" * 10)
        cpf = input("Informe Cpf para Consulta:")
        
        SaldoContas(cpf)

    if opcao == 10:
        
        """Passa a relação de todos os Funcionários"""
        
        tipo = 1
        banco(tipo)
        
        
    if opcao == 11:
        
        """Passa a relação Geral dos Clientes"""
        
        tipo = 2
        banco(tipo)

CobrarTributacao.register(ContaCorrente)
CobrarTributacao.register(SeguroDeVida)

while True:
    
    print("----------Menu----------")
    print("1-Cadastrar Funcionário")
    print("2-Cadastrar Cliente")
    print("3-Criar Conta Corrente")
    print("4-Criar Conta Poupança")
    print("5-Realizar Operação")
    print("6-Abrir Seguro de Vida")
    print("7-Cobrar Tributação")
    print("8-Mostrar Movimentação")
    print("9-Saldos do Cliente")
    print("10-Exibir Funcionário")
    print("11-Relação Geral")
    print("0-Sair")
    print("------------------------")
    
    opcao = int(input(""))
    
    Menu(opcao)
    
    if opcao == 0:
        break
    
print("\n" * 30)
print("FEITO POR BRYAN VICTOR DA COSTA MARTINS")