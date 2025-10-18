from Equipamento import Equipamento, RoboIndustrial, EsteiraTransporte


class SetorFabrica:
    def __init__(self, nome, lista_equipamento: list[Equipamento] = []):
        self.__nome = nome
        self.__lista_equipamento = lista_equipamento

    def __len__(self):
        return len(self.__lista_equipamento)

    def __str__(self):
        return f"Setor[Nome = {self.__nome}, Qtd. Equipamentos = {len(self)}]"

    def adicionar_equipamento(self, equipamento: Equipamento):
        self.__lista_equipamento.append(equipamento)

    def listar_equipamentos(self):
        print(f"Listagem de equipamento do setor {self.__nome}:")
        for equipamento in self.__lista_equipamento:
            print(equipamento)

if __name__ == "__main__":
    # Simulação de agregação na classe SetorFabrica
    # Aqui adicionar uma lista com equipamento que já existiam, então são independentes
    print("----- Simulação 3 ------")
    equipamento1 = Equipamento(1, "Fresadora", "Industrial")
    robo = RoboIndustrial(3, "soldagem")
    esteira = EsteiraTransporte(4, 5)

    setorAzul = SetorFabrica("Setor Azul", [equipamento1])

    setorAzul.adicionar_equipamento(robo)
    setorAzul.adicionar_equipamento(esteira)

    setorAzul.listar_equipamentos()
    print("------------------------")
