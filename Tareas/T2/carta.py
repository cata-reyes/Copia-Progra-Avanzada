from abc import ABC, abstractmethod

class Carta(ABC):
    
    def __init__(self,nombre,tipo,vida_maxima,multiplicador_defensa,precio,probabilidad_especial):
        self.nombre=nombre
        self.vida_maxima=int(vida_maxima)
        self._vida=int(vida_maxima)
        self.tipo=tipo
        self.multiplicador_defensa=float(multiplicador_defensa)
        self.precio=int(precio)
        self.probabilidad_especial=float(probabilidad_especial)
    
    def __str__(self):
        self.presentarse()

    @abstractmethod
    def recibir_dano(self,dano):
        dano_recibido=round(int(dano)*self.multiplicador_defensa)
        self.vida=self.vida-dano_recibido

    @abstractmethod
    def usar_habilidad_especial(self):
        pass

    @abstractmethod
    def presentarse(self):
        pass

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self,valor):
        if self._vida < 0:
            self._vida = 0
            return self._vida
        else:
            self._vida=valor
    