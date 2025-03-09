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
            self.state = "Explorar"

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
