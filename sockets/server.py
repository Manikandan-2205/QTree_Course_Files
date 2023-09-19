import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen()
while True:
    conn, addr = s.accept()
    conn.send(b'Hello world')
    print('Connecting Established')
