from cadastro import Cadastro
from cliente import Cliente

import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (host, port)
cadastro = Cadastro()

def menu(con, cliente):

    connected  = True
    while connected:

        msg = int(con.recv(1024).decode())
        
        if msg == 0:
            connected =  False
        
        elif msg  == 1:

            dados = con.recv(4096).decode()
            lista = dados.split(',')
            cliente = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4])
            retorno = cadastro.cadastro(cliente)

            if(retorno == True):
                con.send('1'.encode())
            elif(retorno == False):
                con.send('0'.encode())

        elif msg == 2:

            dados = con.recv(4096).decode()
            lista_de_login = dados.split(',')

            if(cadastro.busca(lista_de_login[0]) == None):
                con.send('0'.encode())

            else:

                objeto_login = cadastro.login(lista_de_login[0],lista_de_login[1])

                if (objeto_login != None):

                    login = []
                    login.append(objeto_login.nome)
                    login.append(objeto_login.cpf)
                    login.append(objeto_login.senha)
                    login.append(objeto_login.nascimento)
                    login.append(objeto_login.genero)
                    login.append(str(objeto_login.saldo))
                    dados = ",".join(login)
                    con.send(dados.encode())
                else:
                    con.send('1'.encode())

        elif msg == 3:

            dados = con.recv(4096).decode()
            lista_de_deposito = dados.split(',')
                
            objeto_login = cadastro.busca(lista_de_deposito[1])
            valor_deposito = float(lista_de_deposito[0])

            if(objeto_login.deposito(valor_deposito) != False):

                cadastro.deposito(objeto_login.cpf, objeto_login.saldo)
                cadastro.historico_deposito(objeto_login.cpf, valor_deposito)
                con.send('0'.encode())

            else:
                con.send('1'.encode())

        elif msg == 4:

            dados = con.recv(4096).decode()
            lista_de_saque = dados.split(',')

            objeto_login = cadastro.busca(lista_de_saque[1])
            valor_saque = float(lista_de_saque[0])

            if(objeto_login.saque(valor_saque) != -1):

                cadastro.saque(objeto_login.cpf, objeto_login.saldo)
                cadastro.historico_saque(objeto_login.cpf, valor_saque)
                con.send('0'.encode())

            else:
                con.send('1'.encode())

        elif msg == 5:
            
            dados = con.recv(4096).decode()
            lista_de_transferencia = dados.split(',')

            objeto_destino = cadastro.busca(lista_de_transferencia[2])

            if(objeto_destino == None):
                con.send('1'.encode())
            else:

                valor = float(lista_de_transferencia[0])
                objeto_envio = cadastro.busca(lista_de_transferencia[1])

                if(objeto_envio.saque(valor) != -1):

                    objeto_envio.saque(valor)
                    cadastro.saque(objeto_envio.cpf, objeto_envio.saldo)

                    objeto_destino.deposito(valor)
                    cadastro.deposito(objeto_destino.cpf, objeto_destino.saldo)
                    cadastro.historico_transferencia(objeto_envio.cpf, objeto_destino.cpf, valor)
                    con.send('0'.encode())

                else:
                    con.send('2'.encode())

        elif msg == 6:

            cpf = con.recv(4096).decode()
            historico = cadastro.historico(cpf)
            con.send(historico.encode())

    print(f"[DESCONECTADO] client: {cliente}")
    con.close()

def main():

    print("[INICIADO] Aguardado conexão...")
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen()

    while True:

        con, cliente = serv_socket.accept()
        print(f"[CONECTADO] client: {cliente}")
        thread = threading.Thread(target=menu, args=(con, cliente))
        thread.start()

if __name__ == "__main__":
    main()