import socket
import threading
import json

# Lista de clientes: cada cliente es {"socket": socket, "usuario": nombre}
clientes = []

# Historial de mensajes (máximo 50)
historial = []
MAX_HISTORIAL = 50

def manejar_cliente(cliente_info):
    cliente = cliente_info["socket"]
    nombre = cliente_info["usuario"]

    # Enviar historial al cliente recién conectado
    for msg in historial:
        try:
            cliente.send((json.dumps(msg) + "\n").encode('utf-8'))
        except:
            pass

    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if not mensaje:
                continue

            # Detectar comando /usuarios
            if mensaje.strip() == "/usuarios":
                lista = [c["usuario"] for c in clientes]
                cliente.send(f"Usuarios conectados: {', '.join(lista)}\n".encode('utf-8'))
                continue

            # Intentamos cargar JSON para mensajes normales
            try:
                data = json.loads(mensaje)
                # Guardamos en historial
                historial.append(data)
                if len(historial) > MAX_HISTORIAL:
                    historial.pop(0)  # eliminar el mensaje más antiguo
            except:
                # Si no es JSON, simplemente ignoramos
                continue

            # Reenviar mensaje a los demás clientes
            for c in clientes:
                if c["socket"] != cliente:
                    try:
                        c["socket"].send((json.dumps(data) + "\n").encode('utf-8'))
                    except:
                        pass

        except:
            print(f"{nombre} se desconectó")
            clientes.remove(cliente_info)
            cliente.close()
            break

# Configuración del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen()

print("Servidor escuchando...")

while True:
    client, address = server.accept()
    # Recibir nombre del cliente
    nombre = client.recv(1024).decode('utf-8')
    cliente_info = {"socket": client, "usuario": nombre}
    clientes.append(cliente_info)
    print(f"{nombre} se conectó desde {address}")
    hilo = threading.Thread(target=manejar_cliente, args=(cliente_info,))
    hilo.start()
