from State import State
from Diccionario import Diccionario

class Disparar(State):        

    def __init__(self, id):
        super().__init__(id)
    
    def Start(self):
        print("Estado: Disparar iniciado")

    def Update(self, perception):
        print("Disparando 🔫  - - - - ")
        return 0, True

    def Transit(self, perception):   
    
        return "Explorar"
    
    def End(self):

        return print("Saliendo del estado de explorar")