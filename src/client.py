import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    server_ip_port = input("Enter server IP: ")
    i = server_ip_port.index(":")
    print("Connecting to server...", (server_ip_port[:i], int(server_ip_port[i+1:])))
    s.connect((server_ip_port[:i], int(server_ip_port[i+1:])))
    s.sendall(b"https://fs.uit.ac.ma/")
    data=s.recv(2048)
    print(data)
