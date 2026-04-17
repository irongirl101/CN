import socket 

HOST = "127.0.0.1"
PORT = 65100 

def Test():
	return "helloworld"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
	s.connect((HOST,PORT))
	r = Test()
	s.sendall(r.encode())
	data = s.recv(1024)
print("Data: ", data)
