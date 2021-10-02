import socket
from datetime import datetime

host = '192.168.106.148'
port = 22222
max_byte = 1024
client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Starting the Client At: ',datetime.now())
client_sock.connect((host,port))

while True:
    msg_to_server = input("Enter message to Server: ")
    client_sock.send(msg_to_server.encode('utf-8'))
    if msg_to_server.lower() == 'q':
        break
    msg_from_server = client_sock.recv(max_byte).decode('utf-8')
    if msg_from_server.lower() == 'q':
        break
    print('Server said: ' + msg_from_server)

client_sock.close()