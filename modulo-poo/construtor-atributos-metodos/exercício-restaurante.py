# Um restaurante deseja informatizar parte do seu atendimento. Para isso, você deve criar uma classe Restaurante que represente um estabelecimento.
# Atributos:
# nome (nome do restaurante)
# cardapio (lista de pratos disponíveis)


# Métodos:
# adicionar_prato(prato): adiciona um novo prato ao cardápio.
# listar_cardapio(): exibe todos os pratos disponíveis.
# atender_cliente(nome_cliente, prato): verifica se o prato está no cardápio.
# Se estiver, exibir mensagem confirmando o pedido.
# Se não estiver, exibir mensagem informando que o prato não existe.
# Desafio extra:
# Crie um restaurante chamado “Sabor Caseiro”.
# Adicione 3 pratos diferentes ao cardápio.
# Simule 2 clientes fazendo pedidos, sendo um deles de um prato que não está no cardápio.


class Restaurante:
    def __init__(self, nome: str, cardapio: list[str] = []):
        self.nome = nome
        self.cardapio = cardapio

    def __len__(self):
        return len(self.cardapio)

    def __str__(self):
        return f"-- Restaurante {self.nome} --"

    def adicionar_prato(self, prato: str) -> None:
        self.cardapio.append(prato)

    def listar_cardapio(self) -> None:
        print(self)
        print(f"Restaurante tem {len(self)} pratos: ")
        for prato in self.cardapio:
            print(prato)
        
    def atender_cliente(self, nome_cliente: str, prato: str):
        if prato in self.cardapio:
            print(f"Sr(a). {nome_cliente} seu pedido de {prato} está confirmado!")
            return
        print(f"Desculpa Sr(a). {nome_cliente}, o prato não está no cardapio, pedido não confirmado")

restaurante = Restaurante("Sabor Caseiro")

restaurante.adicionar_prato("Lasanha")
restaurante.adicionar_prato("Macarronada")
restaurante.adicionar_prato("Torta de Frango")

restaurante.listar_cardapio()

restaurante.atender_cliente("Gabriel", "Lasanha")
restaurante.atender_cliente("Gabriel", "Bife de porco")
