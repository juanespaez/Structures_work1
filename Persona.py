import random


class Persona:

    contador_id = 0

    def __init__(self, llegada):
        # Id consecutivo
        Persona.contador_id += 1
        self.__id = Persona.contador_id
        self.__llegada = llegada
        self.__servicio = random.randint(300, 3600)
        self.atendido = False
        self.espera = 0

    def obtener_servicio(self):
        return self.__servicio

    def obtener_llegada(self):
        return self.__llegada

    def incrementar(self):
        self.espera += 1
