from LGymClient import agentLoop
from SmartAgent import SmartAgent
from BaseAgent import BaseAgent

print("Comienza el funcionamiento del agente")
agent = SmartAgent("1","Isma")
agentLoop(agent,False)