import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.106.132"
port = 443

def portscanner(port):
    if sock.connect_ex((host,port)):
        print("Port " + str(port) + " is closed")
    else:
        print("Port " + str(port) + " is opened") 

portscanner(port)