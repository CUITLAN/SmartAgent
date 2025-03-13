class Diccionario:
    def __init__(self, perception):
        # Percepción
        self.vecindario_arriba = perception[0]
        self.vecindario_abajo = perception[1]
        self.vecindario_derecha = perception[2]
        self.vecindario_izquierda = perception[3]
        self.dist_vecin_arri = perception[4]
        self.dist_vecin_aba = perception[5]
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
    def veJugador(self):
        return abs(round(self.agent_y, 2) - round(self.jugador_p_y, 2)) <= 2
            
