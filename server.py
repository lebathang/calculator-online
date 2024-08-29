import socket

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
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server đang chờ kết nối...")

    conn, addr = server_socket.accept()
    print("Kết nối thành công đến client!")
    print(f"Kết nối từ: {addr}")

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