from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import pyqtSignal


class VentanaInicio(QWidget):

    signal_username = pyqtSignal(str)

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.initgui()

    def initgui(self):

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Ventana Inicio')

        self.label = QLabel('DCCasino', self)
        self.label.move(40, 40)

        self.boton1 = QPushButton('Ingresar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(200, 150)
        self.boton1.clicked.connect(self.boton)
        self.lineedit = QLineEdit(self)
        self.lineedit.move(30, 150)
        self.label_error = QLabel("Coloca un nombre de usuario valido", self)
        self.label_error.move(30, 90)

        self.show()

    def boton(self):
        texto = self.lineedit.text()
        self.signal_username.emit(texto)

    def validar(self, error):
        if error:
            self.label_error.setText("Hay otro usuario registrado con ese nombre")
            print("No se pudo validar")
        else:
            self.hide()
            self.otra_ventana = VentanaPrincipal(self.client)
            self.otra_ventana.show()


class VentanaPrincipal(QWidget):

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.initgui()

    def initgui(self):

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Ventana Principal')
        self.otra_ventana = None
        self.ventana_recarga = None

        self.botonA = QPushButton('BlackJack', self)
        self.botonA.resize(self.botonA.sizeHint())
        self.botonA.move(250, 100)
        self.botonA.clicked.connect(self.pressbotonA)

        self.botonB = QPushButton('Aviator', self)
        self.botonB.resize(self.botonB.sizeHint())
        self.botonB.move(350, 100)
        self.botonB.clicked.connect(self.pressbotonB)

        self.botonC = QPushButton('Recarga', self)
        self.botonC.resize(self.botonC.sizeHint())
        self.botonC.move(60, 450)
        self.botonC.clicked.connect(self.pressbotonC)

        self.show()

    def pressbotonA(self):

        self.hide()
        self.otra_ventana = VentanaBlackJack(self.client)
        self.otra_ventana.show()

    def pressbotonB(self):
        self.hide()
        self.otra_ventana = VentanaAviator(self.client)
        self.otra_ventana.show()

    def pressbotonC(self):
        self.hide()
        self.ventana_recarga = VentanaRecarga(self.client)


        self.ventana_recarga.signal_monto.connect(self.client.recibir_monto)
        self.client.signal_saldo.connect(self.ventana_recarga.recarga)
        
        self.ventana_recarga.show()


class VentanaRecarga(QWidget):

    signal_monto = pyqtSignal(str)

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.initgui()

    def initgui(self):
        self.setGeometry(700, 100, 400, 300)
        self.setWindowTitle('VentanaRecarga')

        self.otra_ventana = None

        self.boton1 = QPushButton('Validar monto', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(250, 150)
        self.boton1.clicked.connect(self.boton_recarga)
        self.lineedit = QLineEdit(self)
        self.lineedit.move(30, 150)

        self.botonvolver = QPushButton('Volver', self)
        self.botonvolver.resize(self.botonvolver.sizeHint())
        self.botonvolver.move(250, 90)
        self.botonvolver.clicked.connect(self.volver)

        self.label = QLabel("Ingrese monto valido\nNo se aceptan caracteres especiales", self)
        self.label.move(30, 70)
        self.show()

    def boton_recarga(self):
        texto = self.lineedit.text()
        self.signal_monto.emit(texto)
        print(texto)

    def recarga(self, lista):
        if lista[0]:
            print(lista[0], lista[1])
            ingresado = str(int(lista[1]) - int(lista[0]))
            self.label.setText(f"Ingreso:{ingresado}\nAhora tiene:{str(lista[1])}")
        else:
            print("Valor no valido")

    def volver(self):
        self.hide()
        self.otra_ventana = VentanaPrincipal(self.client)
        self.otra_ventana.show()


class VentanaBlackJack(QWidget):

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.initgui()

    def initgui(self):
        self.setGeometry(300, 200, 700, 500)
        self.setWindowTitle('BlackJack')

        self.otra_ventana = None
        self.botonvolver = QPushButton('Volver', self)
        self.botonvolver.resize(self.botonvolver.sizeHint())
        self.botonvolver.move(600, 400)
        self.botonvolver.clicked.connect(self.volver)
        self.show()

    def volver(self):
        self.hide()
        self.otra_ventana = VentanaPrincipal(self.client)
        self.otra_ventana.show()


class VentanaAviator(QWidget):

    def __init__(self, client):
        super().__init__()
        self.client = client

        self.setGeometry(300, 200, 700, 500)
        self.setWindowTitle('Aviator')

        self.otra_ventana = None
        self.botonvolver = QPushButton('Volver', self)
        self.botonvolver.resize(self.botonvolver.sizeHint())
        self.botonvolver.move(600, 400)
        self.botonvolver.clicked.connect(self.volver)
        self.show()

    def volver(self):
        self.otra_ventana = VentanaPrincipal(self.client)
        self.hide()
        self.otra_ventana.show()
