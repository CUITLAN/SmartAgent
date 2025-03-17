from Diccionario import Diccionario
from State import State
import random

class Explorar(State):

    def __init__(self, id):
        super().__init__(id)

    def Start(self):
        print("Estado: Explorar iniciado")

    def Update(self, perception):
        percepciones = Diccionario(perception)  
        action = 0
        print("Vidas:", percepciones.vidas)
        print("Posición del agente en X:", percepciones.agent_x)
        return action, False

    def Transit(self, perception):
        percepciones = Diccionario(perception) 

        #if percepciones.veJugador():
           # return "Disparar"
        if percepciones.BalaDetectada():
            print(" - - - - - - - - - - - Vot a Orientar - - - --  -- - - - - - -")
            return "Orientar"
        return self.id
    
    def End(self):
        print("Saliendo del estado: Explorar")
