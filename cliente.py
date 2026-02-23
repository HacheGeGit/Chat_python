import socket
import threading
import json
import datetime
import os

# Función para limpiar pantalla según SO
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

historial_local = []

def recibir_mensajes(cliente):
    buffer = ""
    while True:
        try:
            datos = cliente.recv(1024).decode('utf-8')
            if datos:
                buffer += datos
                while "\n" in buffer:
                    linea, buffer = buffer.split("\n", 1)
                    if linea.strip() == "":
                        continue
                    try:
                        data = json.loads(linea)
                        historial_local.append(f"[{data['hora']}] [{data['usuario']}]: {data['mensaje']}")
                    except:
                        # Mensaje plano (como lista de usuarios)
                        historial_local.append(linea)
                    # Limpiamos pantalla y mostramos todo el historial
                    limpiar_pantalla()
                    for msg in historial_local[-20:]:  # mostramos solo últimos 20 mensajes
                        print(msg)
        except:
            print("Se perdió la conexión con el servidor")
            cliente.close()
            break

# Conectar con el servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 12345))

# Enviar nombre al servidor
usuario = input("Tu nombre: ")
cliente.send(usuario.encode('utf-8'))

# Hilo para recibir mensajes
hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente,))
hilo_recibir.daemon = True  # para que cierre con Ctrl+C
hilo_recibir.start()

# Bucle principal para enviar mensajes
while True:
    texto = input()
    if texto.lower() == "/salir":
        cliente.close()
        break
    elif texto == "/usuarios":
        cliente.send("/usuarios".encode('utf-8'))
    else:
        data = {
            "usuario": usuario,
            "mensaje": texto,
            "hora": datetime.datetime.now().strftime("%H:%M:%S")
        }
        cliente.send(json.dumps(data).encode('utf-8'))
        # Añadimos al historial local y redibujamos pantalla
        historial_local.append(f"[{data['hora']}] [{data['usuario']}]: {data['mensaje']}")
        limpiar_pantalla()
        for msg in historial_local[-20:]:
            print(msg)
