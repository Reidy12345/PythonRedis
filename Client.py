import re
from socket import socket, AF_INET, SOCK_STREAM
from string import Template
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
            print(f"Sending payload {payload}")
            client_socket.sendall(payload)
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response: {response}")

def to_redis_protocol(command):
    
    flush_pattern = r'FLUSH'  
    match = re.match(flush_pattern, command)
    if match:        
        return '$1\r\nFLUSH\r\n'.encode('utf-8')

    simple_get_pattern = r'GET (\w+)'    
    match = re.match(simple_get_pattern, command)
    if match:
        key = match.group(1)
                        
        encoded_command = '*2\r\n'        
        for part in ['SET', key]:
            encoded_command += "$"
            encoded_command += str(len(part))
            encoded_command += "\r\n"
            encoded_command += part
            encoded_command += "\r\n"
        
        return encoded_command.encode('utf-8')
    
    simple_delete_pattern = r'DELETE (\w+)'    
    match = re.match(simple_delete_pattern, command)
    if match:
        key = match.group(1)
                        
        encoded_command = '*2\r\n'        
        for part in ['DELETE', key]:
            encoded_command += "$"
            encoded_command += str(len(part))
            encoded_command += "\r\n"
            encoded_command += part
            encoded_command += "\r\n"
        
        return encoded_command.encode('utf-8')
    
    simple_set_pattern = r'SET (\w+) (\w+)'    
    match = re.match(simple_set_pattern, command)
    if match:
        key = match.group(1)
        value = match.group(2)
                        
        encoded_command = '*3\r\n'        
        for part in ['SET', key, value]:
            encoded_command += "$"
            encoded_command += str(len(part))
            encoded_command += "\r\n"
            encoded_command += part
            encoded_command += "\r\n"
        
        return encoded_command.encode('utf-8')
    
    raise Exception('Command pattern is not supported', command)

if __name__ == "__main__":
    start_client()
