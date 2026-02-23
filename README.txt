# Sistema de Chat en Tiempo Real en Python para terminal.

Proyecto académico que implementa un chat en tiempo real utilizando Python y sockets. Consta de dos componentes:
    -Servidor: maneja las conexiones de múltiples clientes, envía el historial de mensajes y reenvía los mensajes a todos los clientes conectados.
    -Cliente: permite conectarse al servidor, enviar y recibir mensajes, y ver un historial de los últimos mensajes.

## Objetivos del proyecto:
    -Demostrar manejo de sockets TCP en Python.
    -Implementar comunicación concurrente usando hilos (threading).
    -Gestionar un historial de mensajes.
    -Implementar comandos básicos como /usuarios y /salir.

## Estructura del proyecto

# Servidor (server.py):
    -Escucha conexiones entrantes en localhost:12345.
    -Mantiene una lista de clientes conectados y un historial de los últimos 50 mensajes.
    -Para cada cliente:
        -Envía el historial actual al conectarse.
        -Reenvía mensajes recibidos a todos los demás clientes.
        -Responde al comando /usuarios mostrando la lista de usuarios conectados.
        -Maneja desconexiones de manera segura.
    -Uso de hilos para manejar múltiples clientes concurrentemente.
# Cliente (cliente.py):
    -Se conecta al servidor y envía el nombre de usuario.
    -Ejecuta un hilo que recibe mensajes del servidor y los muestra en pantalla.
    -Mantiene un historial local de los últimos 20 mensajes.
    -Permite enviar mensajes normales o comandos:
        /salir → cierra la conexión.
        /usuarios → solicita la lista de usuarios conectados.
    -Los mensajes se envían en formato JSON con usuario, mensaje y hora.
    -La pantalla se limpia y redibuja el historial para mostrar los últimos mensajes.

## Cómo ejecutar
# Requisitos:
    Python 3.x
    Bibliotecas estándar (socket, threading, json, datetime, os)

# Pasos:
    -Inicia el servidor:
        ```bash
        python server.py
    -Inicia uno o varios clientes en otras terminales:
        ```bash
        python cliente.py
    -Ingresa un nombre de usuario y comienza a chatear.

    Comandos disponibles en el cliente:
        /usuarios → muestra la lista de usuarios conectados.
        /salir → desconecta del servidor.

## Funcionalidades implementadas:
    -Conexión de múltiples clientes simultáneos.
    -Envío y recepción de mensajes en tiempo real.
    -Historial de mensajes limitado a los últimos 50 (servidor) y 20 (cliente).
    -Comandos para consultar usuarios conectados y salir.
    -Manejo básico de errores y desconexiones.

Autor: HacheGeGit
