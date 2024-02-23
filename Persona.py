import random


class Persona:

    contador_id = 0

    def __init__(self, llegada: int, id=None, servicio=random.randint(5, 60)):
        # Id consecutivo
        if id is not None:
            self.__id = id
            Persona.contador_id = max(Persona.contador_id, id)
        else:
            Persona.contador_id += 1
            self.__id = Persona.contador_id

        self.__llegada = llegada*60
        self.__servicio = servicio * 60
        self.atendido = False
        self.espera = 0

    def obtener_servicio(self) -> int:
        return self.__servicio

    def obtener_llegada(self) -> int:
        return self.__llegada

    def tiempo_espera(self, tiempo: int) -> None:
        self.espera = tiempo - self.__llegada

    def __str__(self) -> str:
        return "Id: " + str(self.__id)+" ; " + "llegada: " + str(self.__llegada)+" ; " + "Servicio: " + str(self.__servicio)
