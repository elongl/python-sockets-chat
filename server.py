import socket

s = socket.socket()
host = socket.gethostname()
port = 12221
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       print('Waiting for connection...')
       c, addr = s.accept()
       print('Got connection from', addr)
   else:
       print('Waiting for response...')
       print(c.recv(1024).decode())
       q = input("Enter something to this client: ")
       c.send(q.encode())