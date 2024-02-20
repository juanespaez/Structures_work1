import Persona


class Agente:

    def __init__(self):
        self.libre = True
        self.ocupacion = 0
        self.liberar = 0

    def atender(self, persona: Persona, tiempo: int) -> None:
        self.ocupacion += persona.obtener_servicio()
        self.liberar = tiempo + persona.obtener_servicio() - 1
        self.libre = False
        persona.atendido = True

    def liberador(self) -> None:
        self.libre = True

    def tiempolibre (self) -> int:
        return 28800 - self.ocupacion

