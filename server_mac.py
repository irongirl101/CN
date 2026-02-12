import socket
import json

HOST = "0.0.0.0"
PORT = 65101 

def test1(): 
	return "Hello World" 
def test2(): 
	return 5 
FUNCTIONS = {
	"test1":test1,
	"test2":test2
}


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening...")

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)

        data = conn.recv(4096)
        request = json.loads(data.decode())

        func = FUNCTIONS[request["function"]]
       	args = request.get("args", [])
        result = func(*args)

        conn.sendall(json.dumps({"result": result}).encode())

        	
