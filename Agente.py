import Persona


class Agente:

    def __init__(self):
        self.tlibre = 0
        self.ocupacion = 0
        self.libre = True
        self.liberar = 0

    def atender(self, persona: Persona, tiempo: int) -> None:
        self.ocupacion += persona.obtener_servicio()
        self.liberar = tiempo + persona.obtener_servicio()
        self.libre = False
        persona.atendido = True

    def liberador(self) -> None:
        self.libre = True

    def tiempolibre(self, tiempo: int) -> None:
        self.tlibre = tiempo - self.ocupacion

    def __str__(self) -> str:
        return "tiempo libre: " + str(self.tlibre) + " ; Ocupacion" + str(self.ocupacion)
