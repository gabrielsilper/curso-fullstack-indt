from Setor import SetorFabrica
from Equipamento import RoboIndustrial, EsteiraTransporte

class PainelControle:
    def __init__(self):
        self.__setor = SetorFabrica("vermelho")

    def get_setor(self):
        return self.__setor

    def exibir_informacoes(self):
        print("Informações do Painel:")
        print("Setor:", self.__setor)
        self.__setor.listar_equipamentos()

if __name__ == "__main__":
    # Simulação de composição na classe PainelControle
    print("----- Simulação 4 ------")
    painel_controle = PainelControle()

    print("Qual o setor do painel:", painel_controle.get_setor())
    # Aqui demonstra que o painel já foi instanciado com um setor, significa que pra ele existir, tinha que ter um setor dentro dele existindo
    # Então ele dependia da existência desse setor
    robo = RoboIndustrial(3, "soldagem")
    esteira = EsteiraTransporte(4, 5)
    painel_controle.get_setor().adicionar_equipamento(robo)
    painel_controle.get_setor().adicionar_equipamento(esteira)

    painel_controle.exibir_informacoes()
    print("------------------------")
