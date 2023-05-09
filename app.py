import os
from server.server import ASCIIServer


if __name__ == "__main__":
    try:
        print(f'Running in {os.getenv("ENV")} mode.')
        
        host = '0.0.0.0'
        port = 5000

        server = ASCIIServer(host, port)
        server.run()
    except Exception as e:
        print(e)