# client.py
import socket
import json

HOST = "10.20.200.174"
PORT = 65101

"""request = {
    "function": "greet",
    "args": ["Arch Linux"]
}"""

request = {
	"function":"test1",
	"args": []
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(json.dumps(request).encode())

    data = s.recv(4096)

print("Response:", json.loads(data.decode()))

