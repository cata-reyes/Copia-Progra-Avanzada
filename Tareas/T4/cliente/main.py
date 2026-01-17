from backend.backend import Cliente
from frontend.frontend import VentanaInicio
from PyQt5.QtWidgets import QApplication
import sys
import os
import json

json_file = os.path.join('backend', 'conexion.json')

with open(json_file, 'r', encoding='utf-8') as file:
    datos = json.load(file)

host = datos['host']
port = datos['port']

if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    client = Cliente(host, port)
    ventana = VentanaInicio(client)

    ventana.show()

    ventana.signal_username.connect(client.recibir_username)
    client.signal_nombre_valido.connect(ventana.validar)

    sys.exit(app.exec_())
