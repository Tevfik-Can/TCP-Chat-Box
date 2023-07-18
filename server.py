import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

# Create a socket for the server using IPv4 address family and TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to the specified host and port
server.bind((HOST, PORT))

# Listen for incoming connections
server.listen()

# Lists to keep track of connected clients and their nicknames
clients = []
nicknames = []

# Function to broadcast a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle the messages from a client
def handle(client):
    while True:
        try:
            # Receive messages from the client (up to 1024 bytes)
            message = client.recv(1024)

            # Log the received message to the server console
            print(f"{nicknames[clients.index(client)]} is saying: {message}")

            # Broadcast the message to all connected clients
            broadcast(message)
        except:
            # If an error occurs (client disconnects or an exception is raised),
            # remove the client from the list and close the connection.
            index = clients.index(client)
            clients.remove(client)
            client.close()

            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

# Function to receive incoming connections and start a thread to handle each client
def receive():
    while True:
        # Accept a new client connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask the client to send its nickname
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        nicknames.append(nickname)

        # Add the client to the list of connected clients
        clients.append(client)

        # Print the client's nickname on the server console
        print(f"Nickname of the client is {nickname}")

        # Broadcast a message to all clients notifying about the new connection
        broadcast(f"{nickname} has connected to the server".encode('utf-8'))

        # Send a message to the newly connected client
        client.send(f"{nickname} has connected to the server\n".encode('utf-8'))

        # Start a new thread to handle the client's messages
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Main function to start the server and wait for incoming connections
if __name__ == "__main__":
    print("=-=-=-=-=-=-= Server is Running =-=-=-=-=-=-=")
    receive()
