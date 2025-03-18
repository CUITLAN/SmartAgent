#Evaluamos si el camino hacia el objetivo esta libre
class PathFider:

    def alternativa(self, agent_x, agent_y, perception):
        if perception[2] == 0:
            return 3
        if perception[3] == 0:
            return 4
        if perception[1] == 0:
            return 2
        if perception[0] == 0:
            return 1
        return 0



    def camino_libre(self, agnet_x, agent_y, goal_x, goal_y, percpetion):
        if  (goal_x > agnet_x and percpetion[2]==1) or \
            (goal_x < agnet_x and percpetion[3]==1) or \
            (goal_y > agent_y and percpetion[1]==1) or \
            (goal_y < agent_y and percpetion[0]==1):
            return False, self.alternativa(agnet_x, agent_y, percpetion)
        #En este caso ek camino esta libre, no hace falta buscar alterntaiva
        return True, None