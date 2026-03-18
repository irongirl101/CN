# client.py
import socket
import subprocess 
import queue
import threading

HOST = "192.168.139.14"
PORT = 65101
BUFFER_SIZE = 4096 
BUFFER_CHUNK = 50 
# a buffer would keep a certain amount of data, till processed. 
buffer = queue.Queue(maxsize=BUFFER_CHUNK)

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

# adding data into queue
def recv_data(sock): 
	while True: 
		data = sock.recv(BUFFER_SIZE)
		if not data: 
			buffer.put(None)
			break 
		buffer.put(data)

# playing data 

def play_data(): 
	while True: 
		chunk = buffer.get()
		if chunk is None: 
				break 
		player.stdin.write(chunk)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall((song+"\n").encode())
	response = s.recv(4096).decode().strip()
	
	if response == "Error": 
		print("Song not found")
	else:
		recieve_thread = threading.Thread(target=recv_data,args=(s,))
		play_thread = threading.Thread(target=play_data)

		recieve_thread.start()
		play_thread.start()

		recieve_thread.join()
		recieve_thread.join() 

player.stdin.close()
player.wait()

print("Ended")

