import socket
import threading


class ThreadedServer:
    def __init__(self, port):
        self.socket = socket.socket()
        self.socket.bind((socket.gethostname(), port))

    def listen(self):
        self.socket.listen(5)
        while True:
            client, address = self.socket.accept()
            threading.Thread(target=self.listen_to_client, args=(client, address)).start()

    @staticmethod
    def listen_to_client(client, address):
        print(address[0] + ' Has enter the chat.')
        while True:
            try:
                data = client.recv(1024)
                print(data.decode())
            except ConnectionResetError:
                client.close()
                return


if __name__ == '__main__':
    ThreadedServer(2412).listen()
