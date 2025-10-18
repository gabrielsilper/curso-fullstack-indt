from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    @abstractmethod
    def ler_dados(self):
        pass

    def calibrar(self):
        print(f"{self.__nome} calibrado com sucesso!")


class SensorTemperatura(Sensor):
    def __init__(self):
        super().__init__("Sensor de Temperatura")

    def ler_dados(self):
        temperatura = random.randint(0, 45)
        return f"Temperatura {temperatura}ºC"


class SensorVibracao(Sensor):
    def __init__(self):
        super().__init__("Sensor de Vibração")

    def ler_dados(self):
        vibracao = random.randint(0, 500)
        return f"Vibração {vibracao} Hz"

if __name__ == "__main__":
    # Simulação das classes concretas provindas da classe abstrata Sensor
    print("----- Simulação 5 ------")
    sensor_temp = SensorTemperatura()
    sensor_vibr = SensorVibracao()

    lista_sensores_simulacao = [sensor_temp, sensor_vibr]


    # Fiz um função para usar como paramêtro classes que são feitas a partir da classe abstrata Sensor
    def exibir_informacao_sensores(sensor: Sensor):
        print(f"Informação do {sensor.get_nome()} : {sensor.ler_dados()}")


    print("Demonstração do polimorfismo dos sensores:")
    for sensor in lista_sensores_simulacao:
        exibir_informacao_sensores(sensor)
    print("------------------------")
