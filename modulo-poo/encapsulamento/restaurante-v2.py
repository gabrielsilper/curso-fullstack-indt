# Um restaurante deseja informatizar parte do seu atendimento. Para isso, você deve criar uma classe Restaurante que represente um estabelecimento, aplicando encapsulamento para proteger seus dados.
# Classe Restaurante
# Atributos privados:

#     __nome → nome do restaurante
#     __cardapio → lista de pratos disponíveis (lista de strings)

# Métodos:

#     get_nome() → retorna o nome do restaurante.
#     set_nome(novo_nome) → altera o nome apenas se for uma string não vazia.
#     adicionar_prato(prato) → adiciona um novo prato ao cardápio somente se ainda não existir.
#     listar_cardapio() → exibe todos os pratos disponíveis.
#     atender_cliente(nome_cliente, prato) → verifica se o prato está no cardápio.
#     Se estiver → exibe mensagem confirmando o pedido.
#     Se não estiver → exibe mensagem informando que o prato não existe.

# Desafio ExtraCrie um restaurante chamado “Sabor Caseiro”.
# Adicione 3 pratos diferentes ao cardápio.
# Simule 2 clientes fazendo pedidos, sendo um deles de um prato inexistente.
# Altere o nome do restaurante usando o método set_nome() e exiba novamente o nome com get_nome().


class Restaurante:
    def __init__(self, nome: str, cardapio: list[str] = []):
        self.__nome = nome
        self.__cardapio = cardapio

    def __len__(self):
        return len(self.__cardapio)

    def __str__(self):
        return f"-- Restaurante {self.__nome} --"

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        if len(nome) < 3 :
            print("Precisa ser um nome válido")
            return
        self.__nome = nome

    def adicionar_prato(self, prato: str) -> None:
        if prato in self.__cardapio:
            print("já existe esse prato no cardápio")
            return
        self.__cardapio.append(prato)

    def listar_cardapio(self) -> None:
        print(f"Restaurante tem {len(self)} pratos: ")
        for prato in self.__cardapio:
            print(prato)

    def atender_cliente(self, nome_cliente: str, prato: str):
        if prato in self.__cardapio:
            print(f"Sr(a). {nome_cliente} seu pedido de {prato} está confirmado!")
            return
        print(
            f"Desculpa Sr(a). {nome_cliente}, o prato não está disponível no cardapio"
        )


restaurante = Restaurante("Sabor Caseiro")

restaurante.adicionar_prato("Lasanha")
restaurante.adicionar_prato("Macarronada")
restaurante.adicionar_prato("Torta de Frango")

restaurante.set_nome("Sabor da Vovó")
restaurante.listar_cardapio()

restaurante.atender_cliente("Gabriel", "Lasanha")
restaurante.atender_cliente("Gabriel", "Bife de porco")
