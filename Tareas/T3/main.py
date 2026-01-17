from backend import consultas
from frontend.frontend import VentanaEntrada, VentanaPrincipal, VentanaMapa
from PyQt5.QtWidgets import QApplication
from sys import exit


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaEntrada()   
    ventana.show()          
    exit(app.exec_())  # el de PyQT
