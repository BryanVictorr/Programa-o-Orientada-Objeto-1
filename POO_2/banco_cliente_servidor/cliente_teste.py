import socket

host = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (host, port)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    print(f"[CONECTADO] ao servidor {host}:{port}")

    connected = True
    while connected:
        msg = input("Digite:")
        client.send(msg.encode())

        if msg == "desconect":
            connected = False
        else:
            msg = client.recv(1024).decode()
            print(f"[SERVIDOR] {msg}")
        
if __name__ == "__main__":
    main()