import re

def from_protocol_simple_string(str):
    return str.split('\r\n')[0][1:]

def to_protocol_simple_string(str):
    return '+' + str + '\r\n'

def to_protocol_array(array):
    
    encoded_command = '*'
    encoded_command += str(len(array))
    encoded_command += '\r\n' 
    
    for part in array:
            encoded_command += "$"
            encoded_command += str(len(part))
            encoded_command += "\r\n"
            encoded_command += part
            encoded_command += "\r\n"  
    
    return encoded_command

def from_protocol_array(array):
    
    parts = array.split('\r\n')
    output = []
    for idx in range((len(parts) // 2) - 1):
        output.append(parts[2 * idx + 2])
    
    return output

def to_redis_protocol(command):
    
    flush_pattern = r'FLUSH'
    match = re.match(flush_pattern, command)
    if match:        
        return to_protocol_array(['FLUSH'])

    simple_get_pattern = r'GET (\w+)'    
    match = re.match(simple_get_pattern, command)
    if match:
        key = match.group(1)
        return to_protocol_array(['GET', key])
    
    simple_delete_pattern = r'DELETE (\w+)'    
    match = re.match(simple_delete_pattern, command)
    if match:
        key = match.group(1)
        return to_protocol_array(['DELETE', key])
    
    simple_set_pattern = r"SET((?:\s+\S+)*)"  
    match = re.match(simple_set_pattern, command)
    if match:
        values = match.group(1).strip().split()
        print('values', values)
        return to_protocol_array(['SET'] + values)
    
    raise Exception('Command pattern is not supported', command)
