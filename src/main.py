import socket
import struct

def gethttp(url):
    i = url.index(b":")

    p = url[:i]
    print("p", p)
    if p == b"https":
        p = 443
    else:
        p = 80

    i += 3
    print(url[i:])
    j = url[i:].index(b"/")+i
    addr = url[i:j]
    print(addr)
    path = url[j:]
    print(path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print((addr, int(p)))
        s.connect((addr, int(p)))
        s.sendall(b"GET " + path + b" HTTP/1.1\r\nHost: " + addr + b"\r\n\r\n")
        data = s.recv(2048)
        return data

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 5678))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            header = conn.recv(3)
            if not header or len(header)<3: break

            command, pyload_len = struct.unpack(">BH",header)
            pyload = conn.recv(pyload_len)

            if not pyload or len(pyload)<pyload_len: break
            data = gethttp(pyload)
            conn.sendall(data)