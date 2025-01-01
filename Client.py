from socket import socket, AF_INET, SOCK_STREAM
from config import HOST, PORT

def start_client():
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        while True:
            command = input("Enter command (SET key value / GET key): ")
            if command.lower() in ['exit', 'quit']:
                print("Exiting client.")
                break
            
            payload = to_redis_protocol(command)
            print("Sending payload {payload}")
            client_socket.sendall(payload)
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response: {response}")

def to_redis_protocol(command):
    return command.encode('utf-8')

if __name__ == "__main__":
    start_client()
