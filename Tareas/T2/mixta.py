from tropa import Tropa
from estructura import Estructura

class TropaEstructura(Tropa,Estructura):
    def __init__(self, nom, tip, vida_t, def_t, oro, esp_t, ataque, m_ataque, vida_e, def_e, es_e):
        Tropa.__init__(nom, tip, vida_t, def_t, oro, esp_t, ataque, m_ataque)
        Estructura.__init__(nom, tip, vida_e, def_e, oro, es_e)
        self.vida_maxima=int(vida_e) + (int(vida_t)/2)
        self.vida=int(vida_e) + (int(vida_t)/2)
        self.multiplicador_defensa=max(float(def_e),float(def_t))
        self.probabilidad_especial=(float(es_e)+float(esp_t))/2 + 0.1

    
    def atacar(self):
        return super().atacar()
    
    def recibir_dano(self, dano):
        return super().recibir_dano(dano)
    
    def presentarse(self):
        return super().presentarse()
    
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