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
        action = random.randint(1, 4)
        print("Vidas:", percepciones.vidas)
        print("Posición del agente en X:", percepciones.agent_x)
        return action, False

    def Transit(self, perception):
        percepciones = Diccionario(perception) 

        # if 2 in [percepciones.vecindario_derecha, percepciones.vecindario_izquierda, percepciones.vecindario_abajo, percepciones.vecindario_arriba]:
        #     if random.randint(1, 10) <= 5:
        #         return "Disparar"

        # # Si hay un enemigo en linea
        # if percepciones.EnemigoEnLinea():
        #     return "Disparar"
        
        # Si veo al jugador
        if percepciones.veJugador():
            return "Disparar"

        return self.id
    
    def End(self):
        print("Saliendo del estado: Explorar")
