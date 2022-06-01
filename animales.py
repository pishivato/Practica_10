class Animales:
    
    nombre = None
    anos = None
    vacuna = False
    
    def __init__(self, nombre="perro", anos="0") -> None:
        self.nombre = nombre
        self.anos  = anos 
    
    def Comer(self):
        print(f"{self.nombre.upper()} esta comiendo \n")

    def Dormir(self):
        print(f"{self.nombre.upper()} esta durmiendo \n")
    
    def set_Vacuna(self, vacuna):
        self.vacuna = vacuna
