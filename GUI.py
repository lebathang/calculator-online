import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def start_client(output_widget, num1_entry, num2_entry, operator_entry, connect_button):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = 'localhost'  # Replace with the actual server IP address
    server_port = 54321  # Replace with the actual server port

    try:
        client_socket.connect((server_ip, server_port))
        output_widget.insert(tk.END, f"Kết nối thành công tới server {server_ip}:{server_port}\n")
        output_widget.see(tk.END)
        connect_button.config(state=tk.DISABLED)  # Disable connect button after a successful connection
    except socket.error as e:
        output_widget.insert(tk.END, f"Không thể kết nối đến server:{e}\n")
        output_widget.see(tk.END)
        return

    def send_calculation():
        num1 = num1_entry.get()
        num2 = num2_entry.get()
        operator = operator_entry.get()
        
        if not num1 or not num2 or not operator:
            output_widget.insert(tk.END, "Please fill in all fields.\n")
            output_widget.see(tk.END)
            return

        user_input = f"{num1} {operator} {num2}"

        if user_input.lower() == 'exit':
            client_socket.close()
            output_widget.insert(tk.END, "Disconnected from server.\n")
            output_widget.see(tk.END)
            connect_button.config(state=tk.NORMAL)  # Enable connect button after disconnecting
            return

        client_socket.send(user_input.encode())
        result = client_socket.recv(1024).decode()
        output_widget.insert(tk.END, f"Nhập vào: {user_input}\n")
        output_widget.insert(tk.END, f"Kết quả: {result}\n")
        output_widget.see(tk.END)

    send_button = tk.Button(window, text="Send", command=send_calculation)
    send_button.pack()

def start_client_thread(output_widget, num1_entry, num2_entry, operator_entry, connect_button):
    client_thread = threading.Thread(target=start_client, args=(output_widget, num1_entry, num2_entry, operator_entry, connect_button))
    client_thread.start()

def create_gui():
    global window
    # Create the main window
    window = tk.Tk()
    window.title("Client GUI")

    # Create a text area for displaying messages
    output_widget = scrolledtext.ScrolledText(window, width=50, height=20)
    output_widget.pack()

    # Create labels and entry widgets for user inputs
    tk.Label(window, text="Nhập vào số thứ nhất").pack()
    num1_entry = tk.Entry(window, width=20)
    num1_entry.pack()

    tk.Label(window, text="Nhập vào số thứ hai").pack()
    num2_entry = tk.Entry(window, width=20)
    num2_entry.pack()

    tk.Label(window, text="Nhập dấu vào (+, -, *, /):").pack()
    operator_entry = tk.Entry(window, width=5)
    operator_entry.pack()

    # Create a button to connect to the server
    connect_button = tk.Button(window, text="Nhấn vào đây để kết nối đến Server", command=lambda: start_client_thread(output_widget, num1_entry, num2_entry, operator_entry, connect_button))
    connect_button.pack()

    # Start the GUI loop
    window.mainloop()

if __name__ == "__main__":
    create_gui()
