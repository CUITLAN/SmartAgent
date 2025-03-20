from Diccionario import Diccionario
from State import State

class Explorar(State):

    def __init__(self, id):
        super().__init__(id)

    def Start(self):
        print("Estado: Explorar iniciado")

    def Update(self, perception):
        percepciones = Diccionario(perception)  
        objetivo_x, objetivo_y, objetivo_nombre = percepciones.FijarObjetivo()
        print(f"Objetivo fijado: {objetivo_nombre} en ({objetivo_x}, {objetivo_y})")
        action = percepciones.moverHaciaObjetivo()
        return action, False

    def Transit(self, perception):
        percepciones = Diccionario(perception) 
        if percepciones.DestruirBloque():
            return "Disparar"
        if percepciones.veJugadorCercano():
            return "Disparar"
        if percepciones.veJugadorEnEjeY():
            return "Disparar"
        if percepciones.VeJugadorenEjeX():
            return "Disparar"
        if percepciones.DeteccionBala():
            return "Orientar"
        if percepciones.BalaEnDistanciaMayor():
            return "Esquivar"
        return self.id
    
    def End(self):
        print("Saliendo del estado: Explorar")
