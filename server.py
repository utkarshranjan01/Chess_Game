import socket
import threading
import time
from constants import *

# Connection Data
host = socket.gethostbyname(socket.gethostname())
port = PORT

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()

# List of clients (no nicknames)
clients = []

MAX_CLIENTS = 2

def broadcast(message):
    for client in clients[:]:  # Iterate over a copy of the list
        try:
            client.send(message)
        except BrokenPipeError:
            disconnect(client)

def direct_message(message, sender): # Sends to all but the client it received the message from
    for client in clients:
        if client != sender:  # Skip the sender
            try:
                client.send(message)
            except BrokenPipeError:
                disconnect(client)

def handle(client):
    clients.append(client)  # Add client to list immediately
    print(f"[ACTIVE CONNECTIONS] {len(clients)}")  # Print updated count
    # client.send(f"Welcome! There are {len(clients) - 1} other users online.".encode('ascii'))  # Send message with active connections count
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            if len(message) == 0:
                # Removing And Closing Clients
                time.sleep(1)
                message = client.recv(1024)
                disconnect(client)
                break
            else:
                if message.decode('ascii') == "3^%&^5768>[]&|":
                    client.send(f"{len(clients)}".encode('ascii'))
                # elif message.decode('ascii') == "Disconnect|":
                #     disconnect(client)
                else:
                    # broadcast(message)
                    direct_message(message,client)
        except:
            # Removing And Closing Clients
            disconnect(client)
            break

def disconnect(client):
    if client in clients:
        clients.remove(client)
        client.close()
        print(f"[SOMEONE LEFT ACTIVE CONNECTIONS] {len(clients)}")

def receive():
    print(f"[LISTENING] Server is listening on {host} using port {port}")
    while True:
        if len(clients) >= MAX_CLIENTS:
            client, address = server.accept()  # Accept to send a message
            client.send("Server is full".encode('ascii'))
            client.close()
            print("Connection rejected from", address)
        else:
            # Accept Connection
            client, address = server.accept()
            print("Connected with {}".format(str(address)))
            print(f"[ACTIVE CONNECTIONS] {len(clients)}")

            # Start Handling Thread For Client (no nickname handling)
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

receive()
