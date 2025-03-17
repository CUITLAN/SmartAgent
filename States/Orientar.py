from State import State
from Diccionario import Diccionario

class Orientar(State):        

    def __init__(self, id):
        super().__init__(id)
    def Start(self):
        print("Estado: Orientar iniciado")
    def Update(self, perception):
        percepciones = Diccionario(perception)  
        print("Orientando 🧭-🧭-🧭-🧭-🧭-🧭-🧭-🧭-🧭-🧭")
        action, Shot = percepciones.GirarAbalaDerecha()
        return action, Shot
    def Transit(self, perception):   
    
        return "Disparar"
    def End(self):
        return print("Saliendo del estado de explorar")