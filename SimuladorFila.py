import Agente
import Fila


class SimuladorFila:

    def __init__(self, agentes: int, personas: list, tsim=480):
        self.agentes = agentes
        self.personas = personas
        self.tsim = tsim*60
        self.__tiempo_espera = []
        self.__Ocupacion = []

    def getPromedioEspera(self):
        return (sum(self.__tiempo_espera) / len(self.__tiempo_espera))/60

    def getPromedioOcupacion(self):
        return ((sum(self.__Ocupacion) / self.tsim)/len(self.__Ocupacion))*100

    def correrSimulation(self):
        agentes = [Agente.Agente() for _ in range(self.agentes)]
        tiempo = 0
        num_personas = len(self.personas)
        while tiempo <= self.tsim and num_personas > 0:
            persona_atendida = False
            for persona in self.personas:
                if persona.obtener_llegada() <= tiempo:
                    for agente in agentes:
                        if agente.libre:
                            agente.atender(persona, tiempo)
                            persona.tiempo_espera(tiempo)
                            self.__tiempo_espera.append(persona.espera)
                            self.personas.remove(persona)
                            num_personas -= 1
                            persona_atendida = True
                            break  # Continuar con la siguiente persona

                        elif agente.liberar == tiempo:
                            agente.atender(persona, tiempo)
                            persona.tiempo_espera(tiempo)
                            self.__tiempo_espera.append(persona.espera)
                            self.personas.remove(persona)
                            num_personas -= 1
                            persona_atendida = True
                            break  # Continuar con la siguiente persona

                    if not persona_atendida:
                        tiempo += 1  # Incrementar el tiempo si ninguna persona fue atendida
                    break  # Salir del bucle for persona
            else:
                tiempo += 1  # Incrementar el tiempo si no hay personas listas para ser atendidas

        for agente in agentes:
            self.__Ocupacion.append(agente.ocupacion)





