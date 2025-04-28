import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog
from tkinter import messagebox
import sys

HOST = '127.0.0.1'
PORT = 9090

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Client")

        self.nickname = None
        self.running = True

        self.create_widgets()
        self.setup_connection()

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def create_widgets(self):
        # Display chat messages
        self.chat_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=20, pady=5, expand=True, fill='both')

        # Input field
        self.msg_entry = tk.Entry(self.master)
        self.msg_entry.pack(padx=20, pady=5, fill='x')
        self.msg_entry.bind("<Return>", lambda event: self.send_message())

        # Send button
        self.send_button = tk.Button(self.master, text="Send", command=self.send_message)
        self.send_button.pack(padx=20, pady=5)

        # Exit button
        self.exit_button = tk.Button(self.master, text="Exit", command=self.close_connection)
        self.exit_button.pack(padx=20, pady=5)

    def setup_connection(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client.connect((HOST, PORT))
        except ConnectionRefusedError:
            messagebox.showerror("Connection Error", "Failed to connect to server.")
            sys.exit(1)

        self.nickname = tk.simpledialog.askstring("Nickname", "Choose your nickname:")
        if not self.nickname:
            messagebox.showinfo("Exit", "You must provide a nickname.")
            sys.exit(0)

    def receive_messages(self):
        while self.running:
            try:
                message = self.client.recv(4096).decode('utf-8')
                if not message:
                    break

                if message == "NICK":
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    self.display_message(message)
            except:
                break
        self.close_connection()

    def send_message(self):
        message = self.msg_entry.get()
        if message:
            if message.lower() == "/exit":
                self.close_connection()
                return

            full_message = f"{self.nickname}: {message}"
            try:
                self.client.send(full_message.encode('utf-8'))
            except:
                pass

            self.msg_entry.delete(0, tk.END)

    def display_message(self, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

    def close_connection(self):
        if self.running:
            self.running = False
            try:
                self.client.send("/exit".encode('utf-8'))
                self.client.close()
            except:
                pass
            self.master.destroy()
            sys.exit(0)

def main():
    root = tk.Tk()
    app = ChatClient(root)
    root.protocol("WM_DELETE_WINDOW", app.close_connection)
    root.mainloop()

if __name__ == "__main__":
    main()
