import socket

import os

HOST ="0.0.0.0"
PORT = 65101 
CHUNK = 4096

"""def test1(): 
	return "Hello World" 
def test2(): 
	return 5 
FUNCTIONS = {
	"test1":test1,
	"test2":test2
}"""


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening...")
    while True:
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)

            data = conn.recv(4096)
            request = data.decode().strip()

            if not os.path.exists(request):
                conn.sendall("Error\n")
            else:
                conn.sendall("OK\n".encode())
                with open(request,"rb") as f: 
                    while True: 
                        chunk = f.read(CHUNK)
                        if not chunk: 
                            break
                        conn.sendall(chunk)
                print("Song ended. Request if needed.")

            """func = FUNCTIONS[request["function"]]
            args = request.get("args", [])
            result = func(*args)"""

       

        	
