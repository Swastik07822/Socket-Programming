import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == 'NICK':
                client_socket.send(nickname.encode('ascii'))
            else:
                chat_area.config(state=tk.NORMAL)
                chat_area.insert(tk.END, message + "\n")
                chat_area.yview(tk.END)
                chat_area.config(state=tk.DISABLED)
        except:
            print("An error occurred!")
            client_socket.close()
            break

# Function to send messages to the server
def send_message():
    message = f"{nickname}: {message_entry.get()}"
    client_socket.send(message.encode('ascii'))
    message_entry.delete(0, tk.END)

# Function to close the GUI window
def on_closing():
    client_socket.close()
    window.destroy()

# Prompt for nickname
root = tk.Tk()
root.withdraw()  # Hide the main window
nickname = simpledialog.askstring("Nickname", "Choose your nickname:", parent=root)

if nickname:
    # Client setup
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # Localhost or the server IP
    port = 12345        # Port number

    client_socket.connect((host, port))

    # GUI setup
    window = tk.Tk()
    window.title("Chat Application")

    chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
    chat_area.grid(row=0, column=0, columnspan=2)

    message_entry = tk.Entry(window, width=50)
    message_entry.grid(row=1, column=0)

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.grid(row=1, column=1)

    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Start threads for receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    window.mainloop()
else:
    print("Nickname cannot be empty!")
