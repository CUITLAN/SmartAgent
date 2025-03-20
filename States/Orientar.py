from State import State
from Diccionario import Diccionario

class Orientar(State):        

    def __init__(self, id):
        super().__init__(id)
        self.orientado = False 

    def Start(self):
        print("Estado: Orientar iniciado")
        self.orientado = False 

    def Update(self, perception):
        percepciones = Diccionario(perception)  
        print("Orientando")

        if not self.orientado:  
            action, Shot = percepciones.GirarHaciaBala()
            self.orientado = True 
            return action, Shot  
        else:
            return 0, False 

    def Transit(self, perception):   
        percepciones = Diccionario(perception)  
        if percepciones.veJugadorEnEjeY or percepciones.veJugadorEnEjeY:
            return "Disparar"
        else:
            return "Explorar"
    
         

    def End(self):
        print("Saliendo del estado de Orientar")
