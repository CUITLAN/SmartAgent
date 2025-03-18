#Clase para decidir como moverse hacai el objetivo
class Navigator:

    #def __init__(self):
    #    pass

    #Nos encargamso de determinar la dirección del movimiento segun el objetivo
    def decide_mov(self, agent_x, agent_y, goal_x, goal_y, perception):
        #Derecha libre
        if goal_x > agent_x  and perception[2] == 0:
            return 3
        # Izquierda libre
        if goal_x < agent_x and perception[3] == 0:
            return 4
        #Abajo libre
        if goal_y > agent_y and perception[1] == 0:
            return 2
        #Arriba libre
        if goal_y < agent_y and perception[0] == 0:
            return 1
        
        return 0

