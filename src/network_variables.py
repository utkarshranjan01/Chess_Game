import socket
from errno import ECONNRESET, EPIPE

class NetworkManager:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_connected = 0

