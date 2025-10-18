from Sensor import SensorTemperatura, SensorVibracao

ATIVO = "ativo"
INATIVO = "inativo"
EM_MANUTENCAO = "em manutenção"

class Equipamento:
    def __init__(self, id, nome, tipo):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.__status = INATIVO
        # atributos para demonstrar o funcionamento real do sistema, e aqui mais um exemplo de composição
        self.__sensor_temp = SensorTemperatura()
        self.__sensor_vibr = SensorVibracao()

    def __str__(self):
        return f"Equipamento[ID = {self.id},Nome = {self.nome}, Tipo = {self.tipo}], Status = {self.__status}"

    def ligar(self):
        self.set_status(ATIVO)
        print(f"O Equipamento {self.nome} foi ligado(a)")

    def desligar(self):
        self.set_status(INATIVO)
        print(f"O Equipamento {self.nome} foi desligado(a)")

    def exibir_status(self):
        print(f"O Equipamento {self.nome} está {self.__status}")

    def get_status(self) -> str:
        return self.__status

    def set_status(self, status):
        lista_status = [ATIVO, INATIVO, EM_MANUTENCAO]
        if status not in lista_status:
            print(
                f"Error: O status informado não existe! Status do Equipamento {self.nome} não foi alterado."
            )
            return
        self.__status = status
        print(f"Status do Equipamento {self.nome} atualizado para {self.__status}")

    # Métodos para pegar os sensores para a demonstração real, get pois tem encapsulamento
    def get_sensor_temperatura(self):
        return self.__sensor_temp
    
    def get_sensor_vibracao(self):
        return self.__sensor_vibr
    
    # Metódo para colocar em manutenção para a demonstração real
    def acionar_reparo(self):
        self.set_status(EM_MANUTENCAO)
        print(f"O Equipamento está sendo reparado")

class RoboIndustrial(Equipamento):
    def __init__(self, id, capacidade_operacao):
        super().__init__(id, "Robo Industrial", "Industrial")
        self.__capacidade_operacao = capacidade_operacao

    def exibir_status(self):
        print(
            f"Equipamento: {self.nome} | Status: {self.get_emoji_status()} | Capacidade: {self.__capacidade_operacao}"
        )

    def get_emoji_status(self):
        # Queria usar as constantes nos cases, mas o Pylance lança um erro
        match self.get_status():
            case "ativo":
                return "🟢"
            case "inativo":
                return "🔴"
            case "em manutenção":
                return "🟡"


class EsteiraTransporte(Equipamento):
    def __init__(self, id, velocidade):
        super().__init__(id, "Esteira Transporte", "Industrial")
        self.__velocidade = velocidade

    def exibir_status(self):
        print(
            f"A Esteira está com status {self.get_status()}, e está na velocidade {self.__velocidade}"
        )

if __name__ == "__main__":
# Simulação de duas instancias da classe Equipamento para demonstração dos métodos
    print("----- Simulação 1 ------")
    equipamento1 = Equipamento(1, "Fresadora", "Industrial")
    equipamento2 = Equipamento(2, "Ferro de passar", "Doméstico")

    equipamento1.ligar()
    equipamento2.ligar()

    equipamento1.desligar()

    equipamento1.exibir_status()
    equipamento2.exibir_status()

    equipamento1.set_status("falhando")
    equipamento2.set_status("em manutenção")

    print("Uso do get do status por conta do encapsulamento:", equipamento2.get_status())
    print("------------------------")

    # Simulação das duas subclasses que herdam de Equipamento
    print("----- Simulação 2 ------")
    robo = RoboIndustrial(3, "soldagem")
    esteira = EsteiraTransporte(4, 5)

    robo.set_status(EM_MANUTENCAO)
    esteira.ligar()

    lista_equipamentos_simulacao: Equipamento = [equipamento1, equipamento2, robo, esteira]


    def exibir_status_equipamento(equipamento: Equipamento):
        equipamento.exibir_status()


    print("Demonstração do polimorfismo dos equipamentos:")
    for equipamento in lista_equipamentos_simulacao:
        exibir_status_equipamento(equipamento)
    print("------------------------")
