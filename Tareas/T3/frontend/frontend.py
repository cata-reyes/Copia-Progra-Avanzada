from sys import exit
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QLineEdit)



class VentanaEntrada(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(100, 200, 350, 250)
  
        self.init_gui()
    
    def init_gui(self) -> None:
        self.setWindowTitle('Ventana de Entrada')

        
        self.label1 = QLabel('Bienvenidos!', self)
        self.label1.move(130, 15)

        self.label2 = QLabel('Para ir a la ventana principal pulse el boton', self)
        self.label2.move(70, 50)

        self.boton1 = QPushButton('Presionar para continuar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(100, 100)
        self.boton1.clicked.connect(self.abrir_otra_ventana)

        self.show()
    
    def abrir_otra_ventana(self):
        self.hide()
        self.otra_ventana = VentanaPrincipal()
        self.otra_ventana.show()


class VentanaPrincipal(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(100, 200, 630, 400)
  
        self.init_gui()
    
    def init_gui(self) -> None:
        self.setWindowTitle('Ventana de Entrada')

        self.boton = QPushButton('Buscar archivo', self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.move(450, 35)


        self.label3 = QLabel('Consultas!', self)
        self.label3.move(350, 25)
        self.edit = QLineEdit('', self)
        self.edit.setGeometry(340, 45, 100, 20)
        

        self.boton4 = QPushButton('Ejecutar consulta', self)
        self.boton4.resize(self.boton4.sizeHint())
        self.boton4.move(450, 35)

        self.boton2 = QPushButton('Mapa', self)
        self.boton2.resize(self.boton2.sizeHint())
        self.boton2.move(450, 300)
        self.boton2.clicked.connect(self.abrir_otra_ventana)
    
    def abrir_otra_ventana(self):
        self.hide()
        self.otra_ventana = VentanaMapa()
        self.otra_ventana.show()
    



class VentanaMapa(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(100, 200, 700, 400)
  
        self.init_gui()
    
    def init_gui(self) -> None:
        self.setWindowTitle('Ventana Mapa')

        self.boton1 = QPushButton('Regresar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(300, 25)
        self.boton1.clicked.connect(self.volver_a_ventana)
    
    def volver_a_ventana(self):
        self.hide()
        self.otra_ventana = VentanaPrincipal()
        self.otra_ventana.show()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    app = QApplication([])
    ventana = VentanaEntrada()   
    ventana.show()          
    exit(app.exec())  
