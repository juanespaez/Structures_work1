import random


class Persona:

    contador_id = 0

    def __init__(self, llegada):
        # Id consecutivo
        Persona.contador_id += 1
        self.__id = Persona.contador_id

        self.__llegada = llegada
        self.__servicio = random.randint(300, 3600)
        self.espera = 0

    def obtener_servicio(self):
        return self.__servicio
