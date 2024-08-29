import socket
import threading

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = 'localhost'  # Replace with the actual server IP address
    server_port = 54321  # Replace with the actual server port

    try:
        print("Kết nối thành công!")
        client_socket.connect((server_ip, server_port))
        print(f"Kết nối thành công tới server {server_ip}:{server_port}")
    except socket.error as e:
        print(f"Không thể kết nối đến server: {e}")


    while True:
        user_input = input("Nhập phép tính (ví dụ: 10 + 5) hoặc 'exit' để thoát: ")
        if user_input.lower() == 'exit':
            break

        client_socket.send(user_input.encode())
        result = client_socket.recv(1024).decode()
        print(f"Kết quả: {result}")

    client_socket.close()

if __name__ == "__main__":
    start_client()