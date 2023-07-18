# Client-Server Chat Application
This is a simple client-server chat application implemented in Python using sockets and the Tkinter library for the graphical user interface (GUI). The application allows multiple clients to connect to the server and exchange messages in a chat-like manner.

# How the Application Works
## Server Side
The server is responsible for handling incoming connections from clients and broadcasting messages to all connected clients. When a client connects, the server prompts the client to provide a nickname. The server then stores the client's nickname and sends a notification to all connected clients about the new client's arrival.

![image](https://github.com/Tevfik-Can/TCP-Chat-Box/assets/74112509/b25d92e5-d2a6-4273-8a29-2d7f70e41cb8)

## Client Side
The client connects to the server and provides a chosen nickname. The client GUI displays a chat window, allowing the user to view incoming messages and send messages to the server, which then broadcasts them to all other connected clients. When the client sends a message, it includes the chosen nickname, ensuring proper identification.

![image](https://github.com/Tevfik-Can/TCP-Chat-Box/assets/74112509/60b8ce9a-c360-481f-af26-74bb51d083c2)

## Running the Application
First, run the server.py file in cmd using [ python server.py ] in the location of the file to start the server.
Next, run the client.py file to start the client. The application will prompt you to enter your desired nickname.
Multiple clients can run independently and connect to the server simultaneously, allowing real-time communication.

# What I've Learned
Through this project, I've learned the following key concepts:

### Socket Programming:
How to use sockets to establish communication between a server and multiple clients.
### Threading:
How to create and manage threads to handle concurrent tasks, such as receiving messages while running the GUI.
### Tkinter GUI: 
How to design and implement a simple graphical user interface for the chat client using Tkinter.
### Broadcasting Messages: 
How to send messages from one client to the server and then broadcast them to all connected clients.
The client-server chat application showcases the fundamentals of network programming and GUI development in Python. With this basic understanding, you can explore more complex applications and build upon this foundation for further projects.
