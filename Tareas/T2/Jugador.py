
class Jugador():
    def __init__(self):
        
        self.nombre=""
        self.cartas=[]
        self.coleccion=[]
        self.oro=0
        self.tropas=[]
        self.estructuras= []   

    def atacar(self):
        for i in range(len(self.cartas)):
            dano_total=0
            if self.cartas[i].tipo != "estructura":
                dano=self.cartas[i].atacar()
                dano_total+=dano
                print(f"{self.cartas[i].nombre} generó {dano} daño")
        return dano_total

    def recibir_dano(self,dano):
        estructuras= 0 
        for i in range(len(self.cartas)):
            if self.cartas[i].tipo != "tropa":
                estructuras+=1
                 
        if estructuras > 0:
            ataque_recibido=dano/(estructuras)
            contador=0
            while contador < len(self.cartas):
                if self.cartas[contador].tipo != "tropa":
                    self.cartas[contador].recibir_dano(ataque_recibido)
                    if self.cartas[contador].vida <= 0:
                        print(f"{self.cartas[contador].nombre} ha muerto")
                        self.cartas[contador].vida=0
                        self.cartas.pop(contador)
                    else:
                        print(f"{self.cartas[contador].nombre} queda con {self.cartas[contador].vida} HP")
                        contador+=1
                else:
                    contador+=1
        
        elif len(self.cartas) > estructuras:
            contador=0
            while contador < len(self.cartas):
                if self.cartas[contador].tipo == "tropa":
                    self.cartas[contador].recibir_dano(dano)
                    if self.cartas[contador].vida <= 0:
                        print(f"{self.cartas[contador].nombre} ha muerto")
                        self.cartas[contador].vida=0
                        self.cartas.pop(contador)
                    else:
                        print(f"{self.cartas[contador].nombre} queda con {self.cartas[contador].vida} HP")
                        contador+=1
                else:
                    contador+=1


    def presentarse(self):
        print(f"Jugador: {self.nombre}\n")
        print(f"Cartas en colección\n")
        for i in range(len(self.cartas)):
            carta=self.cartas[i]
            vida_max=carta.vida_maxima
            tipo=carta.tipo
            if tipo == "tropa":
                mensaje= f"Ataque: {carta.ataque}"
            else:
                multiplicador_defensa=carta.multiplicador_defensa
                mensaje=f"Multiplicador de defensa: {multiplicador_defensa}"
                if tipo == "mixto":
                    mensaje+=f", Ataque: {carta.ataque}"
            print(f"\n[{i+1}] {carta.nombre} ({tipo}): {carta.vida}/{vida_max} HP, {mensaje}")
