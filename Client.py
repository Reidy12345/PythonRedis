from socket import socket, AF_INET, SOCK_STREAM
from string import Template
from ProtcolHandler import from_protocol_simple_string, to_redis_protocol, from_protocol_array
from config import HOST, PORT

def handle_response(response):
    if response[0] == '+': # simple String
        decoded_response = from_protocol_simple_string(response)
        print(f"Decoded Response: {decoded_response}")
    elif response[0] == '*': # list
        decoded_response = from_protocol_array(response)
        print(f"Decoded Response: {decoded_response}")

def start_client():
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        while True:
            command = input("Enter command (SET / GET / DELETE / FLUSH): ")
            
            payload = to_redis_protocol(command)
            
            print(f"Sending payload {repr(payload)}")
            client_socket.sendall(payload.encode('utf-8'))
            
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response: {repr(response)}")
            
            handle_response(response)

if __name__ == "__main__":
    start_client()
