
from animales import Animales
from perro import Perro
from gato import Gato
from pez import Pez
from veterinaria import Veterinaria

class Zoo:
    
    Anmls = []
    a = Animales()
    vet = Veterinaria(nombre=input("Nombre del veterinario \n"), salario=input("Salario: \n"))
    def __init__(self) -> None:
        pass
    
    def Agregar(self, animal):
        animal = animal.lower() 

        if animal == "perro":
            a = Perro(nombre = input("Nombre del perro: \n"), anos = int(input("Edad del perro: \n")))
        
        elif animal == "gato":
            a = Gato(nombre = input("Nombre del gato: \n"), anos = int(input("Edad del gato: \n")))        
        
        elif animal == "pez":
            a = Pez(nombre = input("NOmbre del pez: \n"), anos= int(input("Edad del pez\n")))
        
        else:
            print("Animal no Admitido \n")
            exit()
        
        
        if a != None:
            self.Anmls.append(a)
        else:
            pass

    
    

    def Listar(self):
        if not self.Anmls:
            print("No hay animales en el zoologico aun :/\n\n")
        else: 
            for anml in self.Anmls:
                anml.Comer()
                self.vet.Vacunar(anml)
                self.vet.Revisar(anml)
                
                if isinstance(anml, Perro):
                    anml.Ladrar()
                
                elif isinstance(anml, Gato):
                    anml.Maullar()
                
                elif isinstance(anml, Pez):
                    anml.Nadar()
                
                print("\n")
        self.Adicional(anml)
        
    def Adicional(self, anml):
        print("Elige una opcion adicional\n")
        
        if isinstance(anml, Perro):
            print("|->     Adicional     <-|\n")
            print("|->(1)  Interactuar   <-|\n")
            op = int(input("Deseas Interactuar((1:si), (2:no)): \n"))
            if op == 1:
                anml.Cola()
            elif op == 2:
                print("Tu te lo pierdes :,( \n\n")
        
        elif isinstance(anml, Pez):
            print("|->     Adicional     <-|\n")
            print("|->(1)  Interactuar   <-|\n")
            op = int(input("Deseas Interactuar((1:si), (2:no)): \n"))
            if op == 1:
                anml.masComida()
            elif op == 2:
                print("Tu te lo pierdes :,( \n\n")

        elif isinstance(anml, Gato):
            print("|->     Adicional     <-|\n")
            print("|->(1)  Interactuar   <-|\n")
            op = int(input("Deseas Interactuar((1:si), (2:no)): \n"))
            if op == 1:
                anml.Rrr()
            elif op == 2:
                print("Tu te lo pierdes :,( \n\n")  
        else:
            pass    

    def Quitar(self) -> None:
        i = 0
        
        if not self.Anmls:
            print("No hay animales que eliminar :/\n\n")
        else:
            for anml in self.Anmls:
                i = self.Anmls.index(anml)
                print(f"Numero({i})", f"-> {anml.nombre}\n")

            op = int(input("Elige un animal: \n"))
            del self.Anmls[op]
            print(f"Borrado !\n")

    

