import socket
from datetime import datetime
host = '192.168.106.148'
port = 22222
max_byte = 1024

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('server_sock created ')
print('Starting The Server At: ', datetime.now())
server_sock.bind((host,port))
print('server_sock binding to port')
server_sock.listen(1)
print('server_sock listen 1 device')
client_sock,client_info = server_sock.accept()
print('server_sock have accepted client')
print('Waiting For The Incoming Connection From Client .....')

while True:
    data = client_sock.recv(max_byte)
    if data.lower() == 'q':
        break
    print('At ',datetime.now(),client_info,' said ',data.decode('utf-8'))
    msg_to_client = input("Enter Message To Client: ")
    client_sock.send(msg_to_client.encode('utf-8'))
    if msg_to_client.lower() == 'q':
        break
client_sock.close()
server_sock.close()