from PainelControle import PainelControle
from Equipamento import Equipamento, RoboIndustrial, EsteiraTransporte

if __name__ == "__main__":
    # Simulação de um sistema
    print("----- Simulação Sistema ------")

    # Para um sistema real, precisamos ter primeiro um Painel de Controle
    painel_controle_real = PainelControle()

    # Como todo painel já vem com um setor vermelho, pois existe essa composição
    # E Vamos adicionar equipamentos no setor vermelho, pois o setor e os equipamentos são independentes, já que foi feito usando agregação

    # Primeiro vamos instanciar alguns Equipamentos
    equipamento_prensa = Equipamento(1, "Prensa Elétrica", "Industrial")
    equipamento_robo = RoboIndustrial(2, "Pintura")
    equipamento_esteira = EsteiraTransporte(3, 3)

    # Agora adicionar ao setor vermelhor
    painel_controle_real.get_setor().adicionar_equipamento(equipamento_prensa) 
    painel_controle_real.get_setor().adicionar_equipamento(equipamento_robo) 
    painel_controle_real.get_setor().adicionar_equipamento(equipamento_esteira)

    # Quando iniciamos o dia, ligamos os equipamentos
    equipamento_prensa.ligar()
    equipamento_robo.ligar()
    equipamento_esteira.ligar()

    # Eu como um gestor, quero olhar como estar o setor vermelhor, ver se tudo está indo bem
    # Opa, durante o dia, o robo deu problema e desligamento foi acionado
    equipamento_robo.desligar()

    # Isso foi visto pelo gestor indo no painel de controle e vendo as informações
    painel_controle_real.exibir_informacoes()

    # Então ele chama o reparo desse equipamento urgentemente
    equipamento_robo.acionar_reparo()

    # O técnico então ver o que está acontecendo com o equipamento, mede umas informações, como temperatura e vibração
    equipamento_robo.get_sensor_temperatura().ler_dados()
    equipamento_robo.get_sensor_vibracao().ler_dados()

    # O técnico repara que precisa calibrar os dois sensores para tudo ficar ok
    equipamento_robo.get_sensor_temperatura().calibrar()
    equipamento_robo.get_sensor_vibracao().calibrar()

    # Após a calibração o equipamento pode ser ligado novamente
    equipamento_robo.ligar()

    # O Gestor então ver novamente se tudo está ok
    painel_controle_real.exibir_informacoes()
