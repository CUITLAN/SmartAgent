from State import State
from Diccionario import Diccionario

class Esquivar(State):
    def __init__(self, id):
        super().__init__(id)
        self.next_state = id 

    def Start(self):
        print("Estado: Esquivar iniciado")
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
        elif percepciones.vecindario_izquierda == 5:
            direccion_bala = MOVE_LEFT
            distancia_bala = percepciones.dist_vecin_izq
        
        print("Esquivar: Dirección de bala:", direccion_bala, "Distancia:", distancia_bala)

        threshold = 3  

        if percepciones.disparar == 0 and distancia_bala >= 5:
            self.next_state = "Explorar"
            if percepciones.dist_vecin_izq > 1 and direccion_bala != MOVE_LEFT:
                movimiento = MOVE_LEFT
                distancia = percepciones.dist_vecin_izq
            elif percepciones.dist_vecin_dere > distancia and direccion_bala != MOVE_RIGHT:
                movimiento = MOVE_RIGHT
                distancia = percepciones.dist_vecin_dere
            elif percepciones.dist_vecin_arri > distancia and direccion_bala != MOVE_UP:
                movimiento = MOVE_UP
                distancia = percepciones. dist_vecin_arri
            elif percepciones.dist_vecin_aba > distancia and direccion_bala != MOVE_DOWN:
                movimiento = MOVE_DOWN
            return movimiento, False
        
        if distancia_bala < 5:
            self.next_state = "Disparar"
            return direccion_bala, False

    def Transit(self, perception):
        percepciones = Diccionario()
        if percepciones.VeJugadorenEjeX or percepciones.veJugadorEnEjeY:
            return "Disparar"
        else:
            return "Explorar"

    def End(self):
        print("Saliendo del estado: Esquivar")
