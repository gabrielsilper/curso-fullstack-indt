Tema: Sistema de Monitoramento e Controle de Equipamentos Industriais
A empresa TechFactory Systems, especializada em soluções para automação e controle de fábricas, está desenvolvendo um sistema para monitorar e gerenciar equipamentos industriais em tempo real. Esse sistema deverá permitir que engenheiros e técnicos acompanhem o funcionamento de máquinas, visualizem status de operação, realizem manutenções e monitorem sensores instalados nos equipamentos.

Como desenvolvedor Python, você foi designado para criar a estrutura orientada a objetos desse sistema, utilizando os princípios fundamentais da Programação Orientada a Objetos (OOP).

Requisitos
Crie uma classe chamada Equipamento, que represente um equipamento industrial.
Essa classe deve possuir os atributos: id, nome, tipo e status (que indica se o equipamento está “ativo”, “inativo” ou “em manutenção”).
Implemente métodos para ligar, desligar e exibir o status do equipamento, mostrando na tela o nome e a situação atual.
Crie dois objetos dessa classe simulando equipamentos diferentes e mostre o uso dos métodos.

Em seguida, adicione um método construtor (__init__) que inicialize todos os atributos da classe.
Aplique encapsulamento ao atributo status, tornando-o privado, e implemente métodos getters e setters que controlem o valor atribuído, permitindo apenas os estados válidos (“ativo”, “inativo”, “em manutenção”).
Demonstre no código que valores incorretos são rejeitados.

A fábrica possui diferentes tipos de equipamentos com características próprias.
Crie duas subclasses que herdem de Equipamento:

RoboIndustrial, com o atributo adicional capacidade_operacao (por exemplo: “soldagem”, “pintura”);
EsteiraTransporte, com o atributo adicional velocidade (em metros por segundo).

Cada uma dessas subclasses deve sobrescrever o método que exibe o status, acrescentando informações específicas.
Mostre o polimorfismo criando uma lista contendo objetos de ambas as subclasses e chamando o mesmo método de exibição para todos.

A fábrica também é dividida em setores, e cada setor possui vários equipamentos.
Crie uma classe chamada SetorFabrica que possua os atributos nome e uma lista de equipamentos associados.
Implemente os métodos adicionar_equipamento(equipamento) e listar_equipamentos().
Essa relação deve representar agregação, já que os equipamentos podem existir mesmo fora do setor.

Depois, crie uma classe chamada PainelControle, que representa o painel de exibição de um setor da fábrica.
Essa classe deve conter internamente um objeto do tipo SetorFabrica, representando uma composição (o painel depende diretamente do setor para existir).

Implemente o método exibir_informacoes() para mostrar o nome do setor e o status de cada equipamento.
Demonstre a diferença entre agregação e composição através de exemplos e comentários no código.

A empresa também utiliza sensores conectados aos equipamentos para medir dados importantes, como temperatura e vibração.
Para padronizar o uso desses sensores, crie uma classe abstrata chamada Sensor utilizando o módulo abc do Python.
Essa classe deve possuir um atributo nome, um método abstrato ler_dados() e um método concreto calibrar() que exibe a mensagem “Sensor calibrado com sucesso.”

Crie duas classes concretas que implementem essa estrutura:

SensorTemperatura, cujo método ler_dados() retorna um valor aleatório de temperatura (em °C);
SensorVibracao, cujo método ler_dados() retorna um valor aleatório de intensidade de vibração.

Demonstre o uso do polimorfismo criando uma lista de sensores e chamando o método ler_dados() para cada um deles.

Por fim, integre todas as classes desenvolvidas em um pequeno sistema de simulação que representa um setor da fábrica, com alguns equipamentos e sensores.
Cada equipamento deve possuir um ou mais sensores associados, e o painel de controle deve ser capaz de exibir o status atual dos equipamentos e os dados de leitura dos sensores.

A simulação deve representar de forma simples, mas funcional, o comportamento real de um sistema de monitoramento e controle de equipamentos industriais dentro de uma fábrica moderna.