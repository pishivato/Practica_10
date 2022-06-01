from animales import Animales


class Veterinaria:
    
    nombre = None
    salario = 0.0
    a = Animales()
    
    def __init__(self, nombre, salario) -> None:
        self.set_Salario(salario)
        self.set_Nombre(nombre)

    def set_Salario(self, salario):
        self.salario = salario
    
    def set_Nombre(self, nombre):
        self.nombre = nombre

    def get_Salario(self) -> float:
        return self.salario

    def get_Nombre(self):
        return self.nombre

    def Vacunar(self, a):
        a.set_Vacuna(True)
    
    def Revisar(self, a):
        if (a.vacuna):
            print(f"{a.nombre} esta vacunado !!\n")
        else:
            print(f"{a.nombre} no esta vacuando !!\n")