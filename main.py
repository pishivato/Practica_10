from zoo import Zoo

class Main:
    
    op = 0
    ZOO = Zoo()
    
    def menu(self):
        
        print("|->           Menu         <-|\n")
        print("|->(1)   Listar Animal     <-|\n")
        print("|->(2)   Agregar Animal    <-|\n")
        print("|->(3)   Quitar Animal     <-|\n")
        print("|->(4)   Salir             <-|\n")
        self.op = int(input("Elige una opcion: "))

        if self.op == 1:
            self.ZOO.Listar()
        
        elif self.op == 2:
            self.ZOO.Agregar(animal = input("Ingresa animal: \n"))
        
        elif self.op == 3:
            self.ZOO.Quitar()
        
        elif self.op == 4:
            print("Vuelva pronto \n")
            exit()
        
        else:
            pass
        
        if self.op != 4:
            self.menu()
    
if __name__ == "__main__":
    mnu = Main()
    mnu.menu()