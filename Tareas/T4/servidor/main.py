from server import Server
#from sys import exit
import json
import os

json_file = os.path.join('database','conexion.json')

with open(json_file, 'r', encoding= 'utf-8') as file:
    datos = json.load(file)

host = datos['host']
port = datos['port']

if __name__ == "__main__":
    client = Server(port, host)
