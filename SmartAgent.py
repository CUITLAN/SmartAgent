# SmartAgent.py
from BaseAgent import BaseAgent
from Diccionario import Diccionario  # Importamos la función

class SmartAgent(BaseAgent):
    # Constructor
    def __init__(self, id, name):
        super().__init__(id, name)
        self.state = "Explorar"  # Estado inicial del agente

    # Método para actualizar la percepción y tomar decisiones
    def update(self, perception):
        percepciones = Diccionario(perception)  # Convertimos percepción en diccionario

        # Verifica si hay un bloque indestructible en las direcciones
        BloqueIndestructible = (
            percepciones["VecindarioArriba"] == 1 or
            percepciones["VecindarioAbajo"] == 1 or
            percepciones["VecindarioDerecha"] == 1 or
            percepciones["VecindarioIzquierda"] == 1
        )

        print(f"Estado antes: {self.state}")
        print("Toma de decisiones del agente")

        # Transición de estados
        if self.state == "Explorar":
            if 4 in [
                percepciones["VecindarioArriba"],
                percepciones["VecindarioAbajo"],
                percepciones["VecindarioDerecha"],
                percepciones["VecindarioIzquierda"]
            ]:
                self.state = "Disparar"
            else:
                self.state = "Mover"
                action = self.move(
                    percepciones["Jugador_P_X"],
                    percepciones["Jugador_P_Y"],
                    percepciones["Agent_X"],
                    percepciones["Agent_Y"]
                )
                return action, False

        elif self.state == "Disparar":
            if not BloqueIndestructible:
                return 0, True  # Dispara solo si no hay bloque indestructible
            else:
                self.state = "Explorar"

        elif self.state == "Esquivar":
            if percepciones["VecindarioAbajo"] == 5:
                direccion_bala = DOWN;

            self.state = "Explorar"
            return NOTHING, False

        print(f"Estado después: {self.state}")
        return 0, False  # No dispara por defecto

    # Definimos la función de movimiento
    def move(self, Jugador_P_X, Jugador_P_Y, Agent_X, Agent_Y):
        # Definimos las acciones de movimiento
        MOVE_UP = 1
        MOVE_DOWN = 2
        MOVE_RIGHT = 3
        MOVE_LEFT = 4
        NOTHING = 0

        # Lógica de movimiento
        action = NOTHING
        if Jugador_P_X > Agent_X:
            action = MOVE_RIGHT
        elif Jugador_P_Y < Agent_Y:
            action = MOVE_LEFT
        elif Jugador_P_Y > Agent_Y:
            action = MOVE_DOWN
        elif Jugador_P_X < Agent_X:
            action = MOVE_UP

        return action

def dodge(self, perception):
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_RIGHT = 3
    MOVE_LEFT = 4
    NOTHING = 0

    #Ver donde esta la bala y a que distancia se encuentra
    if perception["VecindarioArriba"] == 5:
        direccion_bala = MOVE_UP
        distancia_bala = perception["Dist_VecinArri"]
    elif perception["VecindarioAbajo"] == 5:
        direccion_bala = MOVE_DOWN
        distancia_bala = perception["Dist_VecinAba"]
    elif perception["VecindarioDerecha"] == 5:
        direccion_bala = MOVE_RIGHT
        distancia_bala = perception["Dist_VecinDere"]
    elif perception["VecindarioIzquierda"] == 5:
        direccion_bala = MOVE_LEFT
        distancia_bala = perception["Dist_VecinIzq"]

    #Ver si el agente esta mirando a la bala -> Disparar
    if perception["Disparar"] and direccion_bala == perception["Agent_Direccion"]:
        self.state = "Disparar"
        return NOTHING, False
    
    #Si no puede disparar y la bala esta lejos -> Huir
    if distancia_bala > 5:
        self.state = "Explorar"
        if perception["Dist_VecinIzq"] > 1 and direccion_bala != MOVE_LEFT:
            movimiento = MOVE_LEFT
            distancia = perception["Dist_VecinIzq"]
        elif perception["Dist_VecinDere"] > distancia and direccion_bala != MOVE_RIGHT:
            movimiento = MOVE_RIGHT
            distancia = perception["Dist_VecinDere"]
        elif perception["Dist_VecinArri"] > distancia and direccion_bala != MOVE_UP:
            movimiento = MOVE_RIGHT
            distancia = perception["Dist_VecinArri"]
        elif perception["Dist_VecinAba"] and direccion_bala != MOVE_DOWN:
            movimiento = MOVE_DOWN
            distancia = perception["Dist_VecinAba"]
        return movimiento, False

    #Si la bala esta cerca pero no puede disparar -> Orientar y disparar
    self.state = "Disparar" #Si al final no es ninguno de estos casos volvera a Explorar
    if direccion_bala == MOVE_UP and perception["Agent_Direccion"] != MOVE_UP:
        return MOVE_UP, False
    elif direccion_bala == MOVE_DOWN and perception["Agent_Direccion"] != MOVE_DOWN:
        return MOVE_DOWN, False
    elif direccion_bala == MOVE_RIGHT and perception["Agent_Direccion"] != MOVE_RIGHT:
        return MOVE_RIGHT, False
    elif direccion_bala == MOVE_LEFT and perception["Agent_Direccion"] != MOVE_LEFT:
        return MOVE_LEFT, False

    self.state = "Explorar"
    return NOTHING, False