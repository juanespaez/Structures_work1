import Agente
import Persona
import Fila


class SimuladorFila:

    def __init__(self, agentes: int, fila: Fila):
        self.agentes = agentes
        self.personas = fila

    def corrersimulacion(self):
        agentes = []
        tiempo_espera = []
        for i in range(self.agentes):
            agente = Agente()
            agentes.append(agente)

        for tiempo in range(0, 28800):
            for persona in self.personas:
                if persona.obtener_llegada() <= tiempo:
                    for agente in agentes:
                        if agente.libre == True:
                            agente.atender(persona, tiempo)
                            tiempo_espera.append(persona.espera)
                            self.personas.eliminar()
                        else:
                            if agente.liberar == tiempo:
                                agente.liberador()

                    if persona.atendido == True:
                        pass
                    else:
                        persona.incrementar()
                        break
                else:
                    break

