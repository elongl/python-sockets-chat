import socket

alias = input('Welcome, what is your name?\n>>> ')
s = socket.socket()
s.connect((socket.gethostname(), 2412))
while True:
    message = input(f'{alias}: ')
    s.send(f'{alias}: {message}'.encode())
