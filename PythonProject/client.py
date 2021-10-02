# import socket
# def client():
#     sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     sc.connect(('192.168.106.148',50005))
#     msg = sc.recv(1024)
#     msg_decode = msg.decode('utf-8')
#     print(msg_decode)

    
#     msg_two = 'You are Welcome'
#     msg_encode = msg_two.encode('utf-8')
#     sc.send(msg_encode)
# client()