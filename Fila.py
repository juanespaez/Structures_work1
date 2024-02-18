class Fila:

    def __init__(self, personas):
        self.personas = personas

    def eliminar(self):
        self.personas.pop(0)
