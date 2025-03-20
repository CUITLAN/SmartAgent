#from Diccionario import Diccionario  # Convertimos percepciones en diccionario
from BaseAgent import BaseAgent
from States.Disparar import Disparar
from States.Explorar import Explorar
from States.Esquivar import Esquivar
from States.Orientar import Orientar
from StateMachine import StateMachine

class SmartAgent(BaseAgent):
    def __init__(self, id, name):
        super().__init__(id, name)

        # Diccionario de estados
        Estados = {
            "Disparar": Disparar("Disparar"),
            "Explorar": Explorar("Explorar"),
            "Esquivar": Esquivar("Esquivar"),
            "Orientar": Orientar("Orientar")
        }

        # Máquina de estados con estado inicial "Explorar"
        self.stateMachine = StateMachine("SmartAgent", Estados, "Explorar")

    def Start(self):
        print(f"Inicio del agente {self.name}")
        self.stateMachine.Start()

    # Método para actualizar la percepción y tomar decisiones
    def Update(self, perception):
        action, PuedeDisparar= self.stateMachine.Update(perception)  
        return action, PuedeDisparar


    def End(self, win):
        super().End(win)
        self.stateMachine.End()
