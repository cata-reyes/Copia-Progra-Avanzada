class InteligenciaArtificial():

    def __init__(self,nombre,vida_maxima,ataque,descripcion,probabilidad_especial,velocidad):
        self.nombre=nombre
        self.vida_maxima=int(vida_maxima)
        self._vida=int(vida_maxima)
        self.ataque=float(ataque)
        self.multiplicador_defensa=0
        self.multiplicador_ataque=0
        self.probabilidad_especial=probabilidad_especial
        self.velocidad=float(velocidad)
        self.descripcion=descripcion

    def atacar(self):
        dano_generado=round(float(self.ataque)*float(self.multiplicador_ataque))
        return dano_generado

    def recibir_dano(self,dano):
        dano_recibido=round(int(dano)*float(self.multiplicador_defensa))
        self.vida=self.vida - dano_recibido

    def presentarse(self):
        print(f"{self.nombre}: {self.vida}/{self.vida_maxima} HP")
        print(f"{self.descripcion}")

    def usar_habilidad_especial(self):
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
    

    