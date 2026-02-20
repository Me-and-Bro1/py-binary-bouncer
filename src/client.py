import socket
import struct

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    server_ip_port = input("Enter server IP: ")
    i = server_ip_port.index(":")
    print("Connecting to server...", (server_ip_port[:i], int(server_ip_port[i+1:])))
    s.connect((server_ip_port[:i], int(server_ip_port[i+1:])))
    url = b"https://fs.uit.ac.ma/"
    data = struct.pack(">BH", 1, len(url))
    data += url
    s.sendall(data)
    data=s.recv(2048)
    print(data)
