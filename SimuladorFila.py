import Agente
import Fila
import Persona


class SimuladorFila:

    def __init__(self, agentes: int, personas: list[Persona.Persona], tsim=480):
        self.agentes = agentes
        self.personas = personas
        self.tsim = tsim*60
        self.__tiempo_espera = []
        self.__Ocupacion = []

    def getPromedioEspera(self) -> float:
        return (sum(self.__tiempo_espera) / len(self.__tiempo_espera))/60

    def getPromedioOcupacion(self) -> float:
        return ((sum(self.__Ocupacion) / self.tsim)/len(self.__Ocupacion))*100

    def correrSimulation(self) -> None:
        agentes = [Agente.Agente() for _ in range(self.agentes)]
        personas = Fila.Fila(self.personas)
        tiempo = 0
        num_personas = len(self.personas)
        while tiempo <= self.tsim and num_personas > 0:
            for persona in personas.personas:
                if persona.obtener_llegada() <= tiempo:
                    for agente in agentes:
                        if agente.libre:
                            agente.atender(persona, tiempo)
                            persona.tiempo_espera(tiempo)
                            self.__tiempo_espera.append(persona.espera)
                            personas.eliminar()
                            num_personas -= 1
                            break  # Continuar con la siguiente persona

                        elif agente.liberar == tiempo:
                            agente.atender(persona, tiempo)
                            persona.tiempo_espera(tiempo)
                            self.__tiempo_espera.append(persona.espera)
                            personas.eliminar()
                            num_personas -= 1
                            break  # Continuar con la siguiente persona

                    if not persona.atendido:
                        tiempo += 1  # Incrementar el tiempo si ninguna persona fue atendida
                    break  # Salir del bucle for persona
            else:
                tiempo += 1  # Incrementar el tiempo si no hay personas listas para ser atendidas

        for agente in agentes:
            self.__Ocupacion.append(agente.ocupacion)





