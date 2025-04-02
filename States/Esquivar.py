from State import State
from Diccionario import Diccionario

class Esquivar(State):
    def __init__(self, id):
        super().__init__(id)
        self.next_state = id 

    def Start(self):
        print("Estado: Esquivar iniciado- - - - - - - - -")
        self.next_state = self.id

    def Update(self, perception):
        percepciones = Diccionario(perception)
        
        # Constantes de movimiento
        MOVE_UP = 1
        MOVE_DOWN = 2
        MOVE_RIGHT = 3
        MOVE_LEFT = 4
        NOTHING = 0

        # Inicializamos dirección y distancia de la bala
        direccion_bala = NOTHING
        distancia_bala = None

        # Detectamos la bala en cada dirección
        if percepciones.vecindario_arriba == 5:
            direccion_bala = MOVE_UP
            distancia_bala = percepciones.dist_vecin_arri
        elif percepciones.vecindario_abajo == 5:
            direccion_bala = MOVE_DOWN
            distancia_bala = percepciones.dist_vecin_aba
        elif percepciones.vecindario_derecha == 5:
            direccion_bala = MOVE_RIGHT
            distancia_bala = percepciones.dist_vecin_dere
        elif hasattr(percepciones, "vecindario_izquierda") and percepciones.vecindario_izquierda == 5:
            direccion_bala = MOVE_LEFT
            distancia_bala = getattr(percepciones, "dist_vecin_izq", 0)

        print("Esquivar: Dirección de bala:", direccion_bala, "Distancia:", distancia_bala)

        threshold = 3  

        if distancia_bala is not None and distancia_bala > threshold:
            self.next_state = "Explorar"
            movimiento = NOTHING
            
            if hasattr(percepciones, "dist_vecin_izq") and percepciones.dist_vecin_izq > 1 and direccion_bala != MOVE_LEFT:
                movimiento = MOVE_LEFT
            elif hasattr(percepciones, "dist_vecin_dere") and percepciones.dist_vecin_dere > 1 and direccion_bala != MOVE_RIGHT:
                movimiento = MOVE_RIGHT
            elif hasattr(percepciones, "dist_vecin_arri") and percepciones.dist_vecin_arri > 1 and direccion_bala != MOVE_UP:
                movimiento = MOVE_UP
            elif hasattr(percepciones, "dist_vecin_aba") and percepciones.dist_vecin_aba > 1 and direccion_bala != MOVE_DOWN:
                movimiento = MOVE_DOWN
            
            print("Esquivar: Huyendo con movimiento:", movimiento)
            return movimiento, False

        self.next_state = "Disparar"
        if direccion_bala == MOVE_UP:
            return MOVE_DOWN, False
        elif direccion_bala == MOVE_DOWN:
            return MOVE_UP, False
        elif direccion_bala == MOVE_RIGHT:
            return MOVE_LEFT, False
        elif direccion_bala == MOVE_LEFT:
            return MOVE_RIGHT, False
    def Transit(self, perception):
        percepciones = Diccionario()
        if percepciones.VeJugadorenEjeX or percepciones.veJugadorEnEjeY:
            return "Disparar"
        else:
            return "Explorar"

    def End(self):
        print("Saliendo del estado: Esquivar")
