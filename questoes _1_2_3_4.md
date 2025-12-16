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
