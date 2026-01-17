from carta import Carta

class Tropa(Carta):

    def __init__(self,nombre,tipo,vida_max,mult_defensa,precio,prob_especial,ataque,mult_ataque):
        super().__init__(nombre,tipo,vida_max,mult_defensa,precio,prob_especial)
        self.ataque=int(ataque)
        self.multiplicador_ataque=float(mult_ataque)
    
    def atacar(self):
        dano_generado=round(self.ataque*self.multiplicador_ataque)
        return int(dano_generado)
    
    def recibir_dano(self, dano):
        return super().recibir_dano(dano)
    
    def presentarse(self):
        vida_maxima=self.vida_maxima
        print(f"{self.nombre} ({self.tipo}): {self._vida}/{vida_maxima} HP, Ataque: {self.ataque}")
    
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
