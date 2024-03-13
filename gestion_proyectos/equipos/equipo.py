class Equipo:
    def __init__(self, nombreEquipo, numIntegrantes):
        self.nombreEquipo=nombreEquipo
        self.numIntegrantes=numIntegrantes
    def paraImprimir(self):
        txt="{0} {1}, {2}"
        return txt.format(self.nombreEquipo,self.numIntegrantes,"Hola")

class Calificacion(Equipo):
    def __init__(self,nombreEquipo,numIntegrantes,calificacion):
        super().__init__(nombreEquipo,numIntegrantes)
        self.calificacion=calificacion


equi=Calificacion("buenos",4,20)
print(equi.paraImprimir())
print(equi.calificacion)

    
