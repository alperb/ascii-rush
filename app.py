import os

from dotenv import load_dotenv
load_dotenv()

from server.server import PixelServer

if __name__ == "__main__":
    if os.getenv('ENV') == 'development':
        host = 'localhost'
    else:
        host = '0.0.0.0'

    port = 5000
    server = PixelServer(host, port)
    server.run()