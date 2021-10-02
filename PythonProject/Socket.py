# Server --- Client
# -----------------
# Socket     Socket
# Bind       Connect
# Listen     Send
# Accept     Recv
# recv       Send
# send       Close
# recv
# Close
import socket

def server():
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.bind(('192.168.106.148',50005))
    ss.listen(5)
    global client_socket,client_address
    client_socket,client_address = ss.accept()
    msg = 'Hello, thanks'
    msg_encoded = msg.encode('utf-8')
    client_socket.send(msg_encoded)
    msg = client_socket.recv(1024)
    print(msg.decode('utf-8'))
server()   

print(str(client_socket)+"\\\\\\\\\\"+str(client_address))