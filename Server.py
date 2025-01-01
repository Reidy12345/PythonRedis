from socket import socket, AF_INET, SOCK_STREAM
import sys
from ProtcolHandler import from_protocol_array, to_protocol_array, to_protocol_simple_string
from config import HOST, PORT

OKAY = r'+OK\r\n'
ERROR = r'+ERR\r\n'

database = {}

def handle_request(request):
    
    parts = from_protocol_array(request)
    # print(parts)
    
    command = parts[0]
    # print('command', command)
    
    if command == 'SET':
        
        key = parts[1]
        value = parts[2]
        database[key] = value
        
        return to_protocol_simple_string('OK')
    
    elif command == 'GET':
        
        key = parts[1]
        value = database.get(key, 'None')
        
        return to_protocol_simple_string(value)
         
    elif command == 'DELETE':
        
        key = parts[1]
        database.pop(key)
        
        return to_protocol_simple_string('OK')
    
    elif command == 'FLUSH':
        
        database.clear()
        
        return to_protocol_simple_string('OK')
    
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