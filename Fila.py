import Persona


class Fila:

    def __init__(self, personas: list[Persona]):
        self.personas = personas

    def eliminar(self) -> None:
        if len(self.personas) > 0:
            self.personas.pop(0)
        else:
            raise IndexError("La fila esta vacia")

    def __str__(self) -> str:
        fila_str = "Fila:\n"
        for persona in self.personas:
            fila_str += str(persona) + "\n"
        return fila_str

