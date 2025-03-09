#Aqui definieremos el diccionario

def Diccionario(perception):
    """Convierte el vector de percepción en un diccionario con nombres más legibles."""
    return {
        "VecindarioArriba": perception[0],
        "VecindarioAbajo": perception[1],
        "VecindarioDerecha": perception[2],
        "VecindarioIzquierda": perception[3],
        "Dist_VecinArri": perception[4],
        "Dist_VecinAba": perception[5],
        "Dist_VecinDere": perception[6],
        "Dist_VecinIzq": perception[7],
        "Jugador_P_X": perception[8],
        "Jugador_P_Y": perception[9],
        "CommandCenter_X": perception[10],
        "CommandCenter_Y": perception[11],
        "Agent_X": perception[12],
        "Agent_Y": perception[13],
        "Disparar": perception[14],
        "Vidas": perception[15]
    }
