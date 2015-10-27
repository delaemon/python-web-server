import socket

def server():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 8000))
    server.listen(100)
    while 1:
        con, _ = server.accept()
        con.recv(32*1024)
        con.sendall(b"""HTTP/1.1 200 OK \r
Content-Type: text/plain\r
Content-Length: 5\r
\r
hello""")
        con.close()

if __name__ == '__main__':
    server()