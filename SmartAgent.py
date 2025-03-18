from BaseAgent import BaseAgent
import Navigator                    # llamará a Navigator para decidir el movimiento en cada turno.
import PathFinder                   # llamará a PathFinder para saber si hay un camino libre o bloqueado.


class SmartAgent(BaseAgent):

    #constructor
    def __init__(self, id, name):
        super().__init__(id, name)
        self.state = "Explorar"  # Estado inicial del agente
        self.navigator = Navigator()
        self.pathfinder = PathFinder()



    def decide_goal(self, perception):
        PLAYER_X, PLAYER_Y = perception[8], perception[9]
        COMMAND_CENTER_X, COMMAND_CENTER_Y = perception[10], perception[11]

        #SI el cmaino del jugador esta libre, vamos hcaai él
        if self.pathfinder.camino_libre(perception[12], perception[13], PLAYER_X, PLAYER_Y, perception):
            return PLAYER_X, PLAYER_Y
        
        return COMMAND_CENTER_X, COMMAND_CENTER_Y
    

    def update(self, perception):
        AGENT_X, AGENT_Y = perception[12], perception[13]
        GOAL_X, GOAL_Y = self.decide_goal(perception)

        # Verificar si el camino está libre o si hay que tomar otra ruta
        path_clear, alternative_move = self.pathfinder.is_path_clear(AGENT_X, AGENT_Y, GOAL_X, GOAL_Y, perception)

        if path_clear:
            action = self.navigator.decide_movement(AGENT_X, AGENT_Y, GOAL_X, GOAL_Y, perception)
        else:
            action = alternative_move  # Si el camino está bloqueado, usar la mejor alternativa

        return action, False  # False = No disparamos aún










#Revisra si es necesrio.................................................................





#Actualizamos la funcion que va a realizar las acciones
    def update(self, perception):
        #Como nos indica el enunciado extraemos la informacion relevnate dle vector de percepcion
        PLAYER_X, PLAYER_Y = perception[8], perception[9]
        AGENT_X, AGENT_Y = perception[12], perception[13]
        SHELL_NEAR = perception[14]  # Bala cerca
        CAN_FIRE = perception[14]

        #No debe de disparar si hay algun bloque Nodestructible
        #Deberia
        #Definir el nombre de las percepciones para mejorar la lectura

        #Esto de aqui es el Diccionario - - - - - - - - - - - -
        VecindarioArriba = perception[0]
        Dist_VecinArri= perception[4]
        VecindarioAbajo = perception[1]
        Dist_VecinAba = perception[5]
        VecindarioDerecha = perception[2]
        Dist_VecinDere= perception[6]
        VecindarioIzquierda = perception[3]
        Dist_VecinIzq = perception [7]
        #Posicion de el Jugador
        Jugador_P_X = perception [8]
        Jugador_P_Y = perception [9]

        #Posicion de Comand Center
        CommandCenter_X = perception[10]
        CommandCenter_Y = perception [11]
        
        #Posicion de el agente y sus acciones
        Agent_X= perception[12]
        Agent_Y = perception [13]
        Disparar = perception[14]
        Vidas= perception[15]

        #Aqui Finaliza el Diccionario - - - - - - - 
        BloqueIndestructible = VecindarioArriba=1 or VecindarioAbajo=1 or VecindarioDerecha=1 or VecindarioIzquierda=1
        print(f"Estado antes: {self.state}")


        print("Toma de decisiones del agente")
        #Transicion de estados
        if self.state == "Explorar":
            #if perception[0,1,2,3]==4:
                #self.state="Dis++++++parar"
            #self.state="EstadoACambiar"
            self.move(perception)

        elif self.state == "Disparar":
            
            self.state="Estadoa"

        elif self.state=="Orientar":

            self.state="EstadoaAcambiar"
        
        elif self.state=="Esquivar":

            self.state="EstadoACambiar"




        # Las acciones que puede hacer el agente a nivle del movimeinto
        MOVE_UP = 1
        MOVE_DOWN = 2
        MOVE_RIGHT = 3
        MOVE_LEFT = 4
        NOTHING = 0

        # #Logica de movimin¡ento
        # action = NOTHING
        # if PLAYER_X > AGENT_X:
        #     action = MOVE_RIGHT
        # if PLAYER_Y < AGENT_Y:
        #     action = MOVE_LEFT
        # if PLAYER_Y > AGENT_Y:
        #     action = MOVE_DOWN
        # if PLAYER_X < AGENT_X:
        #     action = MOVE_UP

        # return action, False
    

#Definimso la fucnion del movimiento
def move(self, perception):
    
    #Definimos las posiciones
    Jugador_P_X = perception [8]
    Jugador_P_Y = perception [9]
    Agent_X= perception[12]
    Agent_Y = perception [13]

    # Las acciones que puede hacer el agente a nivle del movimeinto
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_RIGHT = 3
    MOVE_LEFT = 4
    NOTHING = 0

    #Realizamos la logica dle movimiento
    action = NOTHING;
    if Jugador_P_X > Agent_X:
        action = MOVE_RIGHT
    if Jugador_P_Y < Agent_Y:
        action = MOVE_LEFT
    if Jugador_P_Y > Agent_Y:
        action = MOVE_DOWN
    if Jugador_P_X < Agent_X:
        action = MOVE_UP
    
    return action, True

    
