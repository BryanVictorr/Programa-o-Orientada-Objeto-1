import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (host, port)

def func_client(con, cliente):

    print(f"[NOVA CONEXÃO] {cliente} conectado.")

    connected  = True
    while connected:
        msg = con.recv(1024).decode()
        if msg == "desconect":
            connected =  False
        
        print(f"[{cliente}] {msg}")
        msg = f"Msg recebida: {msg}"
        con.send(msg.encode())

    con.close()

def main():

    print("[INICIADO] Aguardado conexão...")
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen()
    print(f"[CONECTADO] in {host}:{port}")

    while(True):

        con, cliente = serv_socket.accept()
        thread = threading.Thread(target=func_client, args=(con, cliente))
        thread.start()
        print(f"[CONEXÕES ATIVAS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()