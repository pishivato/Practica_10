from animales import Animales

class Perro(Animales):
    
    def __init__(self, nombre, anos) -> None:
        super().__init__(nombre, anos)
    
    def Comer(self):
        print(f"El perro {self.nombre} esta comiendo \n\n")
    
    def Ladrar(self):
        print(f"El perro {self.nombre} esta ladrando \n\n")
    
    def Cola(self):
        print(f"El perro {self.nombre} esta Moviendo la cola le agardas\n\n")