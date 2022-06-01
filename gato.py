from animales import Animales

class Gato(Animales):
    
    def __init__(self, nombre, anos) -> None:
        super().__init__(nombre, anos)
    
    def Comer(self):
        print(f"El Gato {self.nombre} esta comiendo \n")
    
    def Maullar(self):
        print(f"El Gato {self.nombre} esta maullando \n")
    
    def Rrr(self):
        print(f"El gato {self.nombre} esta ronroneando, creo que le agaradas \n\n")