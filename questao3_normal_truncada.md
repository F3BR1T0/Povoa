## 🎯 Questão 3 – 1. Simulação de Distribuições Contínuas (Normal Truncada)
1. Definição dos Parâmetros

A variável aleatória X representa valores monetários.

    Distribuição Base: Normal (N(μ,σ2)).

    Média (μ): R$ 500,00 (Valor central da maioria das transações)

    Desvio Padrão (σ): R$ 100,00 (Variabilidade razoável)

    Limites de Truncamento:

       Mínimo Inferior (Linf​): R$ 100,00 (Um valor mínimo razoável para a transação)

       Máximo Superior (Lsup​): R$ 800,00 (Um valor máximo para a transação)

A distribuição é N(500,1002) truncada no intervalo [100,800].

------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Questão 3 – 4. Construção e Interpretação do Histograma

O histograma deve mostrar a distribuição da frequência dos valores simulados.
Interpretação:

    O formato do histograma se assemelha a uma curva em sino (característica da Normal), mas é cortado abruptamente nos limites de R$ 100,00 e R$ 800,00, confirmando o truncamento.

    A maior concentração de valores ocorre perto da Média (μ=500), mostrando que a maioria das transações tem esse valor.

    A Média Simulada (e a Mediana, se a distribuição não for muito assimétrica) deve ser próxima de 500.

    A Variância Simulada será menor que a variância teórica (1002=10000) da distribuição Normal sem truncamento, pois o truncamento remove os valores extremos, diminuindo a dispersão.
