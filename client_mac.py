# client.py
import socket
import subprocess 

HOST = "192.168.139.14"
PORT = 65101

player = subprocess.Popen(["ffplay","-nodisp", "-autoexit", "-"], stdin=subprocess.PIPE)
"""request = {
    "function": "greet",
    "args": ["Arch Linux"]
}"""

"""request = {
	"function":"test1",
	"args": []
}"""

song ="Another Brick in the Wall, Pt. 1 - Pink Floyd.flac"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall((song+"\n").encode())
	response = s.recv(4096).decode().strip()
	
	if response == "Error": 
		print("Song not found")
	else:
		with open("recieved_song.flac","wb") as f: 
			while True: 
				data = s.recv(4096)

				if not data: 
					break
				player.stdin.write(data)

player.stdin.close()
player.wait()

print("Ended")

