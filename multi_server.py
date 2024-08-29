import socket
import threading

def handle_client_connection(client_socket, operator):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Xử lý dữ liệu và tính toán
            a, b = data.split()  # Split the data into 'a', 'b', and 'operator'
            a = float(a)
            b = float(b)
            response = calculate(a, b, operator)
            client_socket.send(response.encode('utf-8'))
    finally:
        client_socket.close()

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Lỗi: Không thể chia cho 0"
    else:
        return "Lỗi: Toán tử không hợp lệ"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = 'localhost'
    server_port = 54321
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

        # Lấy địa chỉ IP của server
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("Server đang kết nối từ {local_ip}:{server_port}...")

    conn, addr = server_socket.accept()
    print("Kết nối thành công đến client!")
    print(f"Kết nối thành công từ: {addr}")

    # Tạo một thread mới để xử lý kết nối từ client
    client_handler = threading.Thread(target=handle_client_connection, args=(conn,))
    client_handler.start()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        a, operator, b = data.split()
        a = float(a)
        b = float(b)
        result = calculate(a, b, operator)
        conn.send(str(result).encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()