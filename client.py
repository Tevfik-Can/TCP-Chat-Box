import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 9090

class Client:

    def __init__(self, host, port):
        # Initialize the client's socket and connect to the server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        # Ask the user to enter their nickname using a pop-up dialog
        msg = tkinter.Tk()
        msg.withdraw()
        self.nickname = simpledialog.askstring("Nickname", "Enter your nickname", parent=msg)

        # Set up variables for GUI and client running status
        self.gui_done = False
        self.running = True

        # Create two separate threads for GUI and receiving messages
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        # Start the threads
        gui_thread.start()
        receive_thread.start()

    # Front-end part: GUI loop for the chat window
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="gray")

        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="white")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        # Chat history area using a scrolled text widget
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.win, text="Message:", bg="gray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text="Send!", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        # Handle the window close event
        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    # Method to stop the client and close the connection
    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    # Method to send a message from the input area to the server
    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')

    # Method to receive messages from the server and update the chat window
    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == "NICK":
                    # The server is requesting the nickname from the client
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    # If the GUI is ready, update the chat window with the received message
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("Error Occurred!")
                self.sock.close()
                break

# Create a Client instance and start the chat client
client = Client(HOST, PORT)
