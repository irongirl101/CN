# client.py
import socket
import subprocess 
import queue
import threading
import time

bitrates = [64, 128, 320]
current_bitrate = 128

def measure_bandwidth(start, end, bytes_recv):
    return bytes_recv / (end - start + 1e-6)

def choose_bitrate(bw):
    if bw < 100000:
        return 64
    elif bw < 300000:
        return 128
    else:
        return 320

HOST = "192.168.139.14"
PORT = 65101
BUFFER_SIZE = 4096 
BUFFER_CHUNK = 50 
# a buffer would keep a certain amount of data, till processed.
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
		stats["bytes"] += len(data)
		buffer.put(data)

# playing data 
def play_data(): 
	while True: 
		chunk = buffer.get()
		if chunk is None: 
				break 
		player.stdin.write(chunk) 
	
while True:
	buffer = queue.Queue(maxsize=BUFFER_CHUNK)

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		request_path = f"{current_bitrate}/{song}"
		s.sendall((request_path + "\n").encode())
		response = s.recv(4096).decode().strip()
		
		if response == "Error": 
			print("Song not found")
			break
		else:
			stats = {"bytes": 0}
			start = time.time()
			recieve_thread = threading.Thread(target=recv_data,args=(s,))
			play_thread = threading.Thread(target=play_data)

			recieve_thread.start()
			play_thread.start()

			recieve_thread.join()
			play_thread.join() 

			end = time.time()

			bw = measure_bandwidth(start, end, stats["bytes"])
			print(f"Bandwidth: {bw:.2f}")

			new_bitrate = choose_bitrate(bw)
			print(f"Switching to {new_bitrate} kbps")

			# stop if stable
			if new_bitrate == current_bitrate:
				break

			current_bitrate = new_bitrate

			# safety exit
			if stats["bytes"] == 0:
				break

player.stdin.close()
player.wait()

print("Ended")
