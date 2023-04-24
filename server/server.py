import socket
import threading

from server.connection import Connection

class ASCIIServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        print(f'Server starting on {self.host}:{self.port}...')

        self.conn_bucket = {}

    def run(self):
        self.socket.listen()
        print(f'Listening on {self.host}:{self.port}...')

        while True:
            try:
                conn, addr = self.socket.accept()
                connection = Connection(conn, addr)
                threading.Thread(target=connection.run).start()

                if addr not in self.conn_bucket:
                    self.conn_bucket[addr] = connection
            except ConnectionError as e:
                print(f'Connection with {addr} has been reset.')
                if addr in self.conn_bucket:
                    del self.conn_bucket[addr]
            except Exception as e:
                print(e)

