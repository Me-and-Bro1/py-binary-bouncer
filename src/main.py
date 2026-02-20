import socket


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
            while True:
                data = conn.recv(2048)
                if not data: break
                print(data)
                data = gethttp(data)
                conn.sendall(data)
