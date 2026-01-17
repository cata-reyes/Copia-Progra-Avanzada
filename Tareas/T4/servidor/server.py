import socket
import threading
import json
import parametros_servidor
from sys import exit
import random


class Server():
    def __init__(self, port, host):

        self.port = port
        self.host = host

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info_lock = threading.Lock()
        self.client_info = {}
        self.dinero_inicial = parametros_servidor.saldo_inicial
        print("Para cerrar servidor presione CTRL + C y espere")
        self.bind_and_listen()

        self.accept_connections()

    def bind_and_listen(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.server_socket.settimeout(20)
        print(f"Server listening on {self.host}:{self.port}")

    def accept_connections(self):

        try:
            while True:
                try:
                    client_socket, addr = self.server_socket.accept()

                    with self.info_lock:
                        self.client_info[addr] = {"socket": client_socket, "username": None}

                    listening_client_thread = threading.Thread(
                        target=self.manejar_cliente,
                        args=(client_socket, addr),
                        daemon=True)
                    listening_client_thread.start()

                except OSError:
                    print("Se esta esperando accion")

        except KeyboardInterrupt:
            print("Se hizo CTRL + C se va a cerrar el programa")
            client_socket.close()
            exit()

    def manejar_cliente(self, client_socket, addr):
        print("Cliente conectado")
        print(addr)

        while True:
            # print("Se está recibiendo mensaje")
            mensaje = self.recibir_mensaje(client_socket)
            # print(f"Se recibio {mensaje} de cliente {addr}")
            if mensaje is None:
                print(f"Cliente {addr} desconectado")
                self.eliminar_usuario(addr)
                break

            self.procesar_mensaje(mensaje, client_socket, addr)

            # print("Manda un mensaje")
            # mens = input()
            # self.mandar_json(mens, client_socket)

        client_socket.close()

    def recibir_mensaje(self, client_socket) -> str:
        print("escuchando mensaje")
        clave = parametros_servidor.CLAVE_CASINO
        try:

            # calcular header
            bytes_leidos = bytearray()

            lenght_bytes = len(bytes_leidos)

            while lenght_bytes < 4:
                diferencia = 4 - lenght_bytes
                respuesta = client_socket.recv(diferencia)
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
                respuesta = client_socket.recv(bytes_leer)
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
            client_socket.close()
            return None

    def mandar_json(self, data, socket):

        try:
            json_msg = json.dumps(data)
            msg = json_msg.encode('utf-8')
            length_msg = len(msg)
            clave = parametros_servidor.CLAVE_CASINO

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

            random.shuffle(paquetes_xor)

            length_final = length_msg.to_bytes(4, byteorder='little')

            data_to_send = b"".join(paquetes_xor)
            msg_to_send = length_final + data_to_send
            socket.sendall(msg_to_send)

        except (ConnectionResetError, OSError) as e:
            print(f"Error al enviar: {e}")

    def procesar_mensaje(self, mensaje, socket, addr):
        # print("se esta procesando el mensaje")

        if mensaje[0] == "username":
            error = False
            if len(self.client_info) > 0:
                for direccion in self.client_info.keys():
                    if self.client_info[direccion]["username"] == mensaje[1]:
                        error = True
                        break
            if error is False:
              with self.info_lock:
                self.client_info[addr]["username"] = mensaje[1]
                self.client_info[addr]["saldo"] = int(parametros_servidor.saldo_inicial)
            self.mandar_json(["username", error], socket)

        elif mensaje[0] == "dinero_a_cargar":

            with self.info_lock:
                saldo_previo = int(self.client_info[addr]["saldo"])
                print(saldo_previo)
                if str(mensaje[1]).isdigit():
                    self.client_info[addr]["saldo"] += int(mensaje[1])
                    saldo = str(self.client_info[addr]["saldo"])
                else:
                    saldo = False
                print(saldo)
            self.mandar_json(["saldo", str(saldo_previo), saldo], socket)

    def eliminar_usuario(self, addr):

        with self.info_lock:
            self.client_info[addr]["socket"].close()
            del self.client_info[addr]
            print("se elimino usuario")
