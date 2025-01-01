from socket import socket, AF_INET, SOCK_STREAM
from config import HOST, PORT

database = {}

def handle_request(request):
    return 'test'

def start_server():
    with socket(AF_INET, SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        
        print(f"Server started on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024).decode('utf-8')
                    if not data:
                        break
                    print(f"Received: {repr(data)}")
                    response = handle_request(data)
                    conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()