from carta import Carta

class Estructura(Carta):

    def __init__(self,nombre,tipo,vida_maxima,multiplicador_defensa,precio,probabilidad_especial):
        super().__init__(nombre,tipo,vida_maxima,multiplicador_defensa,precio,probabilidad_especial)
    
    def __str__(self):
        return super().__str__()
    
    def recibir_dano(self, dano):
        return super().recibir_dano(dano)
    
    def presentarse(self):
        print(f"{self.nombre} ({self.tipo}): {self.vida}/{self.vida_maxima}HP")
        pass
    
    def usar_habilidad_especial(self):
        return super().usar_habilidad_especial()
    
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self,valor):
        if self._vida < 0:
            self._vida = 0
        else:
            self._vida=valor
