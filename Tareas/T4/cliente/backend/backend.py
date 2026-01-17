from PyQt5.QtCore import pyqtSignal, QObject
from parametros_cliente import CLAVE_CASINO
from sys import exit
import socket
import threading
import json
import random


class Cliente(QObject):

    signal_nombre_valido = pyqtSignal(bool)
    signal_saldo = pyqtSignal(list)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port

        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connect_to_server()
            self.listen()
        except ConnectionRefusedError:
            print(f'Error: No se pudo conectar al servidor en {host}:{port}')
            self.socket_cliente.close()

    def connect_to_server(self):
        self.socket_cliente.connect((self.host, self.port))
        self.is_connected = True
        print(f'Cliente conectado a servidor {self.host}:{self.port}')

    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def listen_thread(self):
        while self.is_connected:
            try:
                # print("Manda un mensaje")
                # mens = input()
                # self.mandar_json(mens)

                mensaje = self.recibir_mensaje()
                # print(f"Se recibio mensaje: {mensaje}")
                if not mensaje:
                    print("Servidor cerró la conexión")
                    break

                self.procesar_mensajes(mensaje)

            except json.JSONDecodeError:
                print(f"Error: Se recibió un JSON mal formado: {mensaje}")
            except (ConnectionError, ConnectionResetError, OSError):
                print("Conexión con el servidor perdida.")
                self.is_connected = False

        print("Hilo de escucha terminado.")
        self.is_connected = False
        self.socket_cliente.close()
        exit()

    def recibir_mensaje(self):

        clave = CLAVE_CASINO
        try:
            # header
            bytes_leidos = bytearray()
            lenght_bytes = len(bytes_leidos)

            while lenght_bytes < 4:
                diferencia = 4 - lenght_bytes
                respuesta = self.socket_cliente.recv(diferencia)
                if len(respuesta) < diferencia:
                    return "No hay mensaje para leer"
                bytes_leidos.extend(respuesta)
                lenght_bytes = len(bytes_leidos)

            # resto

            lenght_original = int.from_bytes(bytes_leidos, byteorder='little')
            if lenght_original % 124 != 0:
                diferencia = lenght_original % 124
                extencion = 124 - diferencia
            else:
                extencion = 0
            lenght_total = lenght_original + extencion
            num_chunks = lenght_total // 124
            lenght_encriptado = num_chunks * 128

            bytes_mensaje = bytearray()
            while len(bytes_mensaje) < lenght_encriptado:
                restante = lenght_encriptado - len(bytes_mensaje)
                bytes_leer = min(124, restante)
                respuesta = self.socket_cliente.recv(bytes_leer)
                if len(respuesta) == 0:
                    return "Error: Conexión cerrada"
                bytes_mensaje.extend(respuesta)

            paquetes = []
            lenght_bytes_mensaje = len(bytes_mensaje)

            # desencriptar
            for i in range(0, lenght_bytes_mensaje, 128):
                paquete = bytearray(bytes_mensaje[i:i + 128])
                for j in range(len(paquete)):
                    paquete[j] = paquete[j] ^ clave[j]
                paquetes.append(paquete)

            paquetes_id = []

            # sacar id
            for paquete in paquetes:
                id_paquete = int.from_bytes(paquete[:4], byteorder="big")
                chunk = paquete[4:128]
                paquetes_id.append((id_paquete, chunk))

            paquetes_id.sort(key=lambda x: x[0])

            paquetes_ordenados = bytearray()
            for paquete in paquetes_id:
                paquetes_ordenados.extend(paquete[1])

            mensaje_final = paquetes_ordenados[:lenght_original].decode("utf-8")
            return json.loads(mensaje_final)

        except ConnectionError:
            print("Usuario se ha desconectado")
            return None

    def procesar_mensajes(self, mensaje):
        # print("se esta procesando el mensaje")

        if mensaje[0] == "username":
            error = mensaje[1]
            self.signal_nombre_valido.emit(error)

        elif mensaje[0] == "saldo":
            saldo_previo = mensaje[1]
            saldo = mensaje[2]
            if saldo:
                lista = [saldo_previo, saldo]
            else:
                lista = [False, saldo_previo]
            self.signal_saldo.emit(lista)

    def mandar_json(self, data):

        if not self.is_connected:
            print("Error: No conectado.")
            return

        try:
            json_msg = json.dumps(data)
            msg = json_msg.encode('utf-8')
            length_msg = len(msg)
            clave = CLAVE_CASINO

            if length_msg % 124 != 0:
                diferencia = 124 - (length_msg % 124)
                extencion = b"\x00" * diferencia
                msg += extencion

            paquetes = bytearray()

            for i in range(0, length_msg, 124):
                chunk = msg[i:i + 124]
                num_chunk = (i // 124)
                num_chunk = num_chunk.to_bytes(4, byteorder='big')
                paquetes += num_chunk + chunk

            length_paquete = len(paquetes)
            paquetes_xor = []

            for i in range(0, length_paquete, 128):
                chunk = bytearray(paquetes[i:i + 128])
                for byte in range(128):
                    chunk[byte] = chunk[byte] ^ clave[byte]
                paquetes_xor.append(bytearray(chunk))

            length_final = length_msg.to_bytes(4, byteorder='little')

            random.shuffle(paquetes_xor)

            data_to_send = b"".join(paquetes_xor)
            msg_to_send = length_final + data_to_send
            self.socket_cliente.sendall(msg_to_send)
            print("se mando el mensaje")
            return msg_to_send

        except (ConnectionResetError, OSError) as e:
            print(f"Error al enviar: {e}")
            self.is_connected = False

    def recibir_username(self, user):
        print(f"Se recibio {user}")
        self.mandar_json(["username", user])

    def recibir_monto(self, monto):
        self.mandar_json(["dinero_a_cargar", monto])
        print(monto)
