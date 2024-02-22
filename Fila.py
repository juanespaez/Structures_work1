import Persona


class Fila:

    def __init__(self, personas: list[Persona]):
        self.personas = personas

    def eliminar(self):
        if len(self.personas) > 0:
            self.personas.pop(0)
        else:
            raise IndexError("La fila esta vacia")
