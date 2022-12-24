import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def main():
    s.connect(("192.168.0.146", 5000))
    
    while True:
        msg = input("Inserisci comando: ")
        s.sendall(msg.encode())

if __name__ == "__main__":
    main()
    