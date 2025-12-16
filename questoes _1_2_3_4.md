

------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🎯 Questão 4 – 1. Método de Monte Carlo Aplicado (Fundo de Empréstimos)

1. Modelagem e 2. Hipóteses do Modelo

Variável Chave: O número de clientes atendidos (C).

Hipóteses:

    Capital Inicial (K0​): Fixo e conhecido (ex: R$ 50.000,00).

    Valor do Empréstimo (E): Variável aleatória (ex: Distribuição Uniforme no intervalo [1.000, 5.000]).

    Processo: Os empréstimos são concedidos sequencialmente, subtraindo o valor do capital remanescente. O processo para quando Knovo​<0.

    Independência: Cada empréstimo é independente do anterior.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Questão 4 – 3. Estimação do Número Esperado de Clientes

O Método de Monte Carlo consiste em repetir a simulação muitas vezes e calcular a média dos resultados.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Questão 4 – 4. Análise da Variabilidade e Limitações

    Variabilidade: O Desvio Padrão (dp_clientes) indica a variabilidade. Se o DP for alto, significa que em algumas simulações o fundo atendeu muito mais clientes do que em outras (devido à sorte de serem sorteados muitos empréstimos pequenos). Se o DP for baixo, os resultados são mais consistentes.

    Limitações do Modelo:

        Uniformidade Simples: O modelo pressupõe que o valor do empréstimo segue uma distribuição uniforme simples, o que é irreal. Na prática, seria uma distribuição mais complexa (e.g., Log-Normal).

        Não Considera Risco/Taxas: O modelo não considera inadimplência, taxas de juros ou a reposição do capital, tornando-o um cenário muito simplificado de "esgotamento" e não um modelo financeiro completo.

        Capital Residual: O processo é simples: para quando não houver dinheiro. Ele não considera o capital residual que pode sobrar (e que é menor que o Emin​), sendo um custo de oportunidade (dinheiro não usado).
