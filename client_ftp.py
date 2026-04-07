import socket
import os

HOST = '192.168.56.1' # The server's hostname or IP address
PORT = 65432       # The port used by the server

filename = "hello.txt" # Replace with your file name

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to server {HOST}:{PORT}")
    
    # Send filename (simple way; for robust use, send length first)
    s.sendall(filename.encode())
    
    # Open file in binary read mode and send data in chunks
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024) # Read data in chunks
            if not data:
                break
            s.sendall(data)
    print(f"File {filename} sent successfully.")
