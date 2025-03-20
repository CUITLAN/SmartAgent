import math
class Diccionario:
     #Movimiento
    Arriba = 1
    Abajo= 2
    Derecha = 3
    Izquierda = 4

    def __init__(self, perception):
        # Percepción
        self.vecindario_arriba = perception[0]
        self.vecindario_abajo = perception[1]
        self.vecindario_derecha = perception[2]
        self.vecindario_izquierda = perception[3]
        self.dist_vecin_arri = perception[4]
        self.dist_vecin_aba = perception[5]
        self.dist_vecin_izq = perception[6]
        self.dist_vecin_dere = perception[7]
        self.jugador_p_x = perception[8]
        self.jugador_p_y = perception[9]
        self.command_center_x = perception[10]
        self.command_center_y = perception[11]
        self.agent_x = perception[12]
        self.agent_y = perception[13]
        self.disparar = perception[14]
        self.vidas = perception[15]
   

    def EnemigoEnLinea(self):
        return 4 in [
            self.vecindario_derecha, 
            self.vecindario_izquierda, 
            self.vecindario_abajo, 
            self.vecindario_arriba
        ]
    
    #Esto quiere decir que en el eje y ve al jugador
    #Unkreabable = 1, birck =2, Comand-center 3, Player 4, Shell05
    def veJugadorCercano(self):
        #Si es que lo ve Debe de girar y disparar ya sea al jugador o al agente
        if(
            self.vecindario_derecha == 4 or
            self.vecindario_arriba == 4 or
            self.vecindario_izquierda == 4 or 
            self.vecindario_abajo == 4
        ):
            return
    def veJugadorEnEjeY(self, epsilon=1.5):
        if abs(self.jugador_p_y - self.agent_y) <= epsilon:
            print("Veo un jugador en el EJE Y")
            return True
        return False
    def VeJugadorenEjeX(self, epsilon=1.5):
        if abs(self.jugador_p_x - self.agent_x)<= epsilon:
            print("Veo un jugador en el X")
            return True
        return False
    
    def DeteccionBala(self):
        if (
            self.vecindario_derecha == 5 or
            self.vecindario_izquierda == 5 or
            self.vecindario_abajo == 5 or
            self.vecindario_arriba == 5
        ):
            print("Bala detectada 🚀")
            return True
        return False


    def GirarHaciaBala(self):

        if self.vecindario_derecha == 5 and self.dist_vecin_dere>3:
            print("Detecto que se acerca algo por la derecha")
            print("Me he girado a la derecha")
           
            return 3, True

        elif self.vecindario_izquierda == 5 and self.dist_vecin_izq>3:
            print("Detecto que se acerca algo por la izquierda")
            print("Me he girado a la izquierda")
            return Diccionario.Izquierda, True

        elif self.vecindario_abajo == 5 and self.dist_vecin_aba>3:
            print("Detecto que se acerca algo abajo")
            print("Me he girado hacia abajo")
            return Diccionario.Abajo, True

        elif self.vecindario_arriba == 5 and self.dist_vecin_arri>3:
            print("Detecto que se acerca algo arriba")
            print("Me he girado hacia arriba")
            return Diccionario.Arriba, True

        return 0, False  # No se detectó ninguna bala
    def FijarObjetivo(self):
        
        dist_jugador = math.sqrt((self.jugador_p_x - self.agent_x)**2 +
                                 (self.jugador_p_y - self.agent_y)**2)
        dist_cc = math.sqrt((self.command_center_x - self.agent_x)**2 +
                            (self.command_center_y - self.agent_y)**2)
        
        if dist_jugador <= dist_cc:
            print("Estoy apuntando al Jugador")
            return self.jugador_p_x, self.jugador_p_y, "Jugador"
        else:
            print("Estoy apuntando al Comand Center")
            return self.command_center_x, self.command_center_y, "Command Center"
    
    def moverHaciaObjetivo(self):
        objetivo_x, objetivo_y, objetivo_nombre = self.FijarObjetivo()
        tolerance = 0.2

        dx = objetivo_x - self.agent_x
        dy = objetivo_y - self.agent_y
        abs_dx = abs(dx)
        abs_dy = abs(dy)
        
        # Si el agente está alineado en ambos ejes (dentro de la tolerancia)
        if abs_dx <= tolerance and abs_dy <= tolerance:
            print("Ya llegué al objetivo")
            return 0

        # Si ambos ejes requieren movimiento, alternamos entre ellos.
        if abs_dx > tolerance and abs_dy > tolerance:
            if hasattr(self, 'last_axis') and self.last_axis == 'x':
                self.last_axis = 'y'
                axis = 'y'
            else:
                self.last_axis = 'x'
                axis = 'x'
        else:
            # Si solo un eje tiene diferencia mayor que la tolerancia, se elige ese eje.
            axis = 'x' if abs_dx > tolerance else 'y'
        
        if axis == 'x':
            if dx > 0:
                print(f"Moviéndome a la derecha hacia {objetivo_nombre}")
                return 3  # Derecha
            else:
                print(f"Moviéndome a la izquierda hacia {objetivo_nombre}")
                return 4  # Izquierda
        else:
            if dy > 0:
                print(f"Moviéndome hacia abajo hacia {objetivo_nombre}")
                return 1  # Abajo
            else:
                print(f"Moviéndome hacia arriba hacia {objetivo_nombre}")
                return 2  # Arriba


    def DestruirBloque(self):
        if 2 in [self.vecindario_abajo, self.vecindario_arriba, self.vecindario_derecha, self.vecindario_izquierda]:
            return True
        return False
    
    def BalaEnDistanciaMayor(self, threshold=3):
        if self.vecindario_derecha == 5 and self.dist_vecin_dere > threshold:
            return True
        if self.vecindario_izquierda == 5 and self.dist_vecin_izq > threshold:
             return True
        if self.vecindario_abajo == 5 and self.dist_vecin_aba > threshold:
            return True
        if self.vecindario_arriba == 5 and self.dist_vecin_arri > threshold:
            return True
        return False
