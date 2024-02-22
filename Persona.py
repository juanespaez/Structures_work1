import random


class Persona:

    def __init__(self, llegada, id=0, servicio=random.randint(5, 60)):
        # Id consecutivo

        self.__id = id
        self.__llegada = llegada*60
        self.__servicio = servicio * 60
        self.atendido = False
        self.espera = 0

    def obtener_servicio(self):
        return self.__servicio

    def obtener_llegada(self):
        return self.__llegada

    def tiempo_espera(self, tiempo: int):
        self.espera = tiempo - self.__llegada
