import Persona


class Agente:

    def __init__(self):
        self.libre = True
        self.ocupacion = 0

    def atender(self, persona: Persona):
        self.ocupacion += persona.obtener_servicio()
        self.libre = False

    def tiempolibre (self):
        return 28800 - self.ocupacion
