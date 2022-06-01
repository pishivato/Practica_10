from animales import Animales

class Pez(Animales):
    
    def __init__(self, nombre, anos) -> None:
        super().__init__(nombre, anos)
    
    def Comer(self):
        print(f"El pez {self.nombre} esta comiendo \n")
    
    def Nadar(self):
        print(f"El pez {self.nombre} esta Nadando \n")
    
    def masComida(self):
        print(f"El pez {self.nombre} esta regordete \n")
