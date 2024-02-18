import Agente
import Persona
import Fila


class SimuladorFila:

    def __init__(self, agentes, personas):
        self.agentes = agentes
        self.personas = personas

    def corrersimulacion(self):
        agentes = list()
        for i in range(self.agentes):
            agente = Agente()
            agentes.append(agente)

        for i in range(0, 28800):
            pass
