import abc

quant_pets = {'Gato': 0,'Cachorro': 0,'Coelho': 0,'Passaro': 0,'Hamster': 0}
lista_clientes = {}
lista_funcionario = {}
dados_pets = {'Gato':[],'Cachorro':[],'Coelho':[],'Passaro':[],'Hamster':[]}
lista_donos = {}

def verificar_petshop(animal):
    
    if quant_pets[animal] >= 1:
        
        return True
        
    else:
        return False

def listar_pets(animal = '',adotar = False):
    
    print("----PetShop Adoção----")
    
    aux = 1
    
    for key,value in dados_pets.items():
        
        for x in range(0, len(value), 3):
            
            if animal == key:
            
                print("\n{} = Sexo: {} - Raça: {} - Idade: {}".format(aux,value[x],value[x+1],value[x+2]))
                
                aux += 1
            
            if animal == '':
                
                print("{} = Sexo: {} - Raça: {} - Idade: {}".format(key,value[x],value[x+1],value[x+2]))
                
    if adotar == True:
        
        aux = int(input('Qual Deseja Adotar? '))
        print("\nAdotado!")
        return aux
    
def remover_pet(animal,aux):
    
    i = aux * 3
    
    quant_pets[animal] -= 1
    
    for key,value in dados_pets.items():
        
        if key == animal:
            
            dados_pets[key].pop(i-1)
            dados_pets[key].pop(i-2)
            dados_pets[key].pop(i-3)

def verificar_funcionario(cpf):
    
    if cpf in lista_funcionario.keys():
        
        return True
        
    else:
        return False
 
def verificar_cliente(cpf):
    
    if cpf in lista_clientes.keys():
        
        return True
        
    else:
        return False

def listar_funcionario(cpf = ''):
    
    if listar_funcionario != {}:
        
        print("----Resultado da consulta----")
    
        for key,value in lista_funcionario.items():
            
            if cpf == key:
                if len(value) == 4:
            
                    print("\nFuncionário:{} - CPF:{} - Salário:{} - Veterinário:{} - Telefone:{}".format(value[0],key,value[1],value[2],value[3]))
            
                if len(value) == 5:
            
                    print("\nFuncionário:{} - CPF:{} - Salário:{} - Veterinário:{} - Telefone:{} - {}".format(value[0],key,value[1],value[2],value[3],value[4]))
                    
            if cpf == '':
                
                if len(value) == 4:
            
                    print("\nFuncionário:{} - CPF:{} - Salário:{} - Veterinário:{} - Telefone:{}".format(value[0],key,value[1],value[2],value[3]))
            
                if len(value) == 5:
            
                    print("\nFuncionário:{} - CPF:{} - Salário:{} - Veterinário:{} - Telefone:{} - {}".format(value[0],key,value[1],value[2],value[3],value[4]))
                    
        return True
        
    else:
        return False

def listar_clientes(cpf):
    
    for key,value in lista_clientes.items():
        
        if cpf == key:
            
            if len(value) == 3:
                
                print("\nCliente:{} - CPF:{} - Telefone:{} - {}".format(value[0],key,value[1],value[2]))
                
            if len(value) == 2:
                
                print("\nCliente:{} - CPF:{} - Telefone:{}".format(value[0],key,value[1]))
   
def listar_donos():
    
    for key,value in lista_donos.items():
        
        print("Dono:{}".format(key))
        
        for x in range(0, len(value), 1):
            
            print("Pet:{}".format(value[x]))

class Pet():
    
    def __init__(self,animal,sexo,raca,idade):
        
        self._animal = animal
        self._sexo = sexo
        self._raca = raca
        self._idade = idade
        
        Pet.adicionar(self._animal,self._sexo,self._raca,self._idade)
        
    def adicionar(animal,sexo,raca,idade):
    
        quant_pets[animal] += 1
        dados_pets[animal].append(sexo)
        dados_pets[animal].append(raca)
        dados_pets[animal].append(idade)
        
    def adotar(animal,cpf):
        
        if verificar_petshop(animal) == True:
            
            aux = listar_pets(animal,True)
            remover_pet(animal,aux)
            
            if lista_donos == {}:
                
                nome = lista_clientes[cpf][0]
                
                lista_donos[nome] = [animal]
                return True
                
            else:
                
                nome = lista_clientes[cpf][0]
                
                lista_donos[nome].append(animal)
                return True
            
        else:
            return False

class Usuario(abc.ABC):
    
    def __init__(self,nome,cpf,telefone):
        
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
    
    @abc.abstractmethod
    def adicionarTelefone(cpf):
        pass
    
    @abc.abstractmethod
    def removerUsuario(cpf):
        pass

class Funcionario(Usuario):
    
    def __init__(self,nome,cpf,salario,veterinario,telefone):
        
        self._salario = salario
        self._veterinario = veterinario
        
        super().__init__(nome,cpf,telefone)
        
        retorno = verificar_funcionario(self._cpf)
        
        if retorno == False:
            
            lista_funcionario[self._cpf] = [self._nome,self._salario,self._veterinario,self._telefone]
    
    def alterarSalario(cpf,novo_salario):
        
        if cpf in lista_funcionario.keys():
            
            lista_funcionario[cpf][1] = novo_salario
            
            return True
        else:
            return False

    def adicionarTelefone(cpf,novo_telefone):
        
        if cpf in lista_funcionario.keys():
            
            if len(lista_funcionario[cpf]) < 5:
            
                lista_funcionario[cpf].append(novo_telefone)
                return True
            
            else:
                return False
                
        else:
            return False
    
    def removerUsuario(cpf):
        
        retorno = verificar_funcionario(cpf)
        
        if retorno == True:
            
            del lista_funcionario[cpf]
            return True
        
        else:
            return False
    
class Cliente(Usuario):
    
    def __init__(self,nome,cpf,telefone):
        
        super().__init__(nome,cpf,telefone)
        
        retorno = verificar_cliente(self._cpf)
        
        if retorno == False:
            
            lista_clientes[self._cpf] = [self._nome,self._telefone]
            
    def adicionarTelefone(cpf,novo_telefone):
        
        if cpf in lista_clientes.keys():
            
            if len(lista_clientes[cpf]) < 3:
                
                lista_clientes[cpf].append(novo_telefone)
                return True
            
            else:
                return False
        
        else:
            return False
    
    def removerUsuario(cpf):
        
        retorno = verificar_cliente(cpf)
        
        if retorno == True:
            
            del lista_clientes[cpf]
            return True
        
        else:
            return False

def Menu(op):
    
    if op == 1:
        
        nome = input("Nome do Funcionário:")
        cpf = input("CPF do Funcionário:")
        
        retorno = verificar_funcionario(cpf)
        
        while retorno == True:
            
            print("CPF já associado a um Funcionário!")
            cpf = input("Digite novamente o CPF ou 0 para cancelar:")
            
            if cpf == '0':
                return False
            
            retorno = verificar_funcionario(cpf)
        
        if retorno == False:
            
            salario = float(input("Salário do Funcionário:"))
            veterinario = int(input("Funcionário é Veterinário?\n1-Sim - 2-Não\n"))
            telefone = input("Telefone do Funcionário:")
            
            if veterinario == 1:
                
                funcionario = Funcionario(nome,cpf,salario,'Sim',telefone)
                
            elif veterinario == 2:
                
                funcionario = Funcionario(nome,cpf,salario,'Não',telefone)
        
        print("\nFuncionário Cadastrado !")

    if op == 2:
        
        nome = input("Nome do Cliente:")
        cpf = input("CPF do Cliente:")
        
        retorno = verificar_cliente(cpf)
        
        while retorno == True:
            
            print("CPF já associado a um Cliente!")
            cpf = input("Digite novamente o CPF ou 0 para cancelar:")
            
            if cpf == '0':
                return False
            
            retorno = verificar_cliente(cpf)
            
        if retorno == False:
            
            telefone = input("Telefone do Cliente:")
            
            cliente = Cliente(nome,cpf,telefone)
            
        print("\nCliente Cadastrado !")

    if op == 3:
        
        if lista_funcionario == {}:
            
            print("Não existe Funcionário cadastrados!")
            
            return False
        
        cpf = input("Informe do CPF do Funcionário:")
        retorno = verificar_funcionario(cpf)
        
        while retorno == False:
            
            print("CPF não associado a nenhum Funcionário!")
            cpf = input("Digite novamente o CPF ou 0 para cancelar:")
            
            if cpf == '0':
                return False
            
            retorno = verificar_funcionario(cpf)
            
        novo_salario = float(input("Informe o Novo salário:"))
        
        Funcionario.alterarSalario(cpf,novo_salario)
        
        print("\nNovo salário atualizado!")
        
    if op == 4:
        
        usuario = int(input("1-Adicionar ao Cliente\n2-Adicionar ao Funcionário\n"))
    
        if usuario == 1:
            
            if lista_clientes == {}:
                print("Não existe Clientes cadastrados!")
                
                return False
                
        if usuario == 2:
            
            if lista_funcionario == {}:
                print("Não existe Funcionários cadastrados!")
                
                return False

        cpf = input("Informe o CPF:")
        
        if usuario == 1:
            
            retorno = verificar_cliente(cpf)
            
            while retorno == False:
                
                print("CPF não associado a nenhum Cliente!")
                cpf = input("Digite novamente o CPF ou 0 para cancelar:")
                
                if cpf == '0':
                    return False
                    
            
                retorno = verificar_cliente(cpf)
            
            novo_telefone = input("Digite o novo Telefone:")
            retorno = Cliente.adicionarTelefone(cpf,novo_telefone)
            
            if retorno == False:
                print("Máximo de 2 Telefones, número não adicionado!")
                
            else:
                print("Telefone adicionado com Sucesso!")
                
        if usuario == 2:
            
            retorno = verificar_funcionario(cpf)
            
            while retorno == False:
                
                print("CPF não associado a nenhum Funcionário!")
                cpf = input("Digite novamente o CPF ou 0 para cancelar")
                
                if cpf == '0':
                    return False
            
                retorno = verificar_funcionario(cpf)
                
            novo_telefone = input("Digite o novo Telefone:")
            retorno = Funcionario.adicionarTelefone(cpf,novo_telefone)
            
            if retorno == False:
                print("Máximo de 2 Telefones, número não adicionado!")
                
            else:
                print("Telefone adicionado com Sucesso!")

    if op == 5:
        
        op = int(input("1-Funcionario - 2-Cliente\n"))
        
        if lista_funcionario == {} and op == 1:
            print("Não existe Funcionários Cadastrados!")
            return False
            
        elif lista_clientes == {} and op == 2:
            print("Não existe Cliente Cadastrados!")
            return False
            
        if op == 1:
            
            cpf = input("Consulta de Funcionario, informe CPF:")
            retorno = verificar_funcionario(cpf)
        
            while retorno == False:
            
                print("CPF não associado a nenhum Funcionário!")
                cpf = input("Digite novamente o CPF ou 0 para cancelar")
            
                if cpf == '0':
                    return False
            
                retorno = verificar_funcionario(cpf)
            
            listar_funcionario(cpf)
            
        elif op == 2:
            
            cpf = input("Consulta de Cliente, informe CPF:")
            retorno = verificar_cliente(cpf)
            
            while retorno == False:
                
                print("CPF não associado a nenhum Cliente!")
                cpf = input("Digite novamente o CPF ou 0 para cancelar:")
            
                if cpf == '0':
                    return False
            
                retorno = verificar_cliente(cpf)
                
            listar_clientes(cpf)
            
    if op == 6:
        
        animal = ''
        
        cpf = input("Informe o CPF do Cliente que vai adotar:")
        
        retorno = verificar_cliente(cpf)
        
        if retorno == False:
            
            print("CPF incorreto  ou não registrado")
            return False
    
        op = int(input("\n1-Gato\n2-Cachorro\n3-Coelho\n4-Passaro\n5-Hamster\nQual Animal você quer Adotar?\n"))
        
        if op == 1:
            
            animal = 'Gato'
            
        elif op == 2:
            
            animal = 'Cachorro'
            
        elif op == 3:
            
            animal = 'Coelho'
            
        elif op == 4:
            
            animal = 'Passaro'
            
        elif op == 5:
            
            animal = 'Hamster'
            
        if op < 1 or op > 5:
            
            print("Opção de Animal não Disponível!\n\n")
            
        else:
            
            Pet.adotar(animal,cpf)

    if op == 7:
        
        op = int(input("\n1-Gato\n2-Cachorro\n3-Coelho\n4-Passaro\n5-Hamster\nQual Animal você quer adicionar?\n"))
        
        if op == 1:
            
            animal = 'Gato'
            
        elif op == 2:
            
            animal = 'Cachorro'
            
        elif op == 3:
            
            animal = 'Coelho'
            
        elif op == 4:
            
            animal = 'Passaro'
            
        elif op == 5:
            
            animal = 'Hamster'
            
        if op < 1 or op > 5:
            
            print("Opção de Animal não Disponível!\n\n")
            
        else:
            
            sexo = int(input("1-Macho - 2-Fêmea\n"))
            
            if sexo == 1:
                sexo = 'Macho'
                
            elif sexo == 2:
                sexo = 'Fêmea'
                
            raca = input("Raça:")
            idade = input("Idade:")
            Pet.adicionar(animal,sexo,raca,idade)
            
            print("Animal foi adicionado ao PetShop")
            
    if op == 8:
        
        listar_pets()
        
    if op == 9:
        
        listar_donos()
        
    if op == 10:
        
        listar_funcionario()
        
    if op == 11:
        
        op = int(input('1-Remover Funcionario - 2-Remover Cliente\n'))
        
        if op == 1 and lista_funcionario == {}:
            
            print("Não existe Funcionarios Cadastrados!")
            return False
            
        elif op == 2 and lista_clientes == {}:
            
            print("Não existe Cliente Cadastrados!")
            return False
            
        if op == 1:
            
            cpf = input("Informe CPF do Funcionário:")
            retorno = verificar_funcionario(cpf)
            
            while retorno == False:
            
                print("CPF não associado a nenhum Funcionário!")
                cpf = input("Digite novamente o CPF ou 0 para cancelar")
            
                if cpf == '0':
                    return False
            
                retorno = verificar_funcionario(cpf)
            
            Funcionario.removerUsuario(cpf)
            print("\nFuncionario removido!")
            
        elif op == 2:
            
            cpf = input("Informe CPF do Cliente:")
            retorno = verificar_cliente(cpf)
            
            while retorno == False:
            
                print("CPF não associado a nenhum Cliente!")
                cpf = input("Digite novamente o CPF ou 0 para cancelar")
            
                if cpf == '0':
                    return False
            
                retorno = verificar_cliente(cpf)
            
            Cliente.removerUsuario(cpf)
            print("\nCliente removido")

gato1 = Pet('Gato','Macho','Egípcio','6 Mesês')
gato2 = Pet('Gato','Fêmea','Siamês','1 Ano')
cachorro1 = Pet('Cachorro','Macho','PitBull','8 Mesês')
cachorro2 = Pet('Cachorro','Fêmea','Labrador','2 Anos')
coelho1 = Pet('Coelho','Macho','Branco','2 Semanas')
passaro1 = Pet('Passaro','Fêmea','Cabeça Vermelha','2 Mesês')
hamster = Pet('Hamster','Macho','Porquinho da Índia','4 Mesês')

funcionario1 = Funcionario('Pedro','123',2890.0,'Sim','(89)99990-4670')
cliente1 = Cliente('Tercio','321','(89)99933-7305')

while True:
    
    print("----------Menu----------")
    print("1-Cadastrar Funcionário")
    print("2-Cadastrar Cliente")
    print("3-Alterar Salário do Funcionário")
    print("4-Adicionar novo Telefone")
    print("5-Consultar Funcionário ou Cliente")
    print("6-Adotar Pet")
    print("7-Adicionar Pet")
    print("8-Listar PetShop")
    print("9-Listar todos os Donos de Pets")
    print("10-Listar todos os Funcionarios")
    print("11-Remover Usuario")
    print("0-Sair")
    print("------------------------")
    
    try:
        
        opcao = int(input("Escolha uma Função:"))
        
    except ValueError:
        
        opcao = int(input("Opção indisponível/Digite novamente:"))
        

    Menu(opcao)

    if opcao == 0:
        break
    