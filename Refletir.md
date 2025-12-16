🎯 Questão 1 – Simulação de Variáveis Aleatórias Discretas (Dado Honesto)
1. Implementação do Simulador (Código - questao1.py)

A distribuição teórica de um dado honesto é uniforme: P(X=x)=1/6 para x∈{1,2,3,4,5,6}.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Questão 1 – 4. Discussão sobre a Lei dos Grandes Números (LGN)

A Lei dos Grandes Números diz que, à medida que o número de repetições de um experimento aleatório aumenta (no caso, N→∞), a média das frequências observadas (probabilidade empírica) converge para o valor esperado (probabilidade teórica).

    Convergência Observada: Como N=106 é um número muito grande, observamos que a diferença entre a probabilidade empírica e a teórica (1/6 ≈0.166667) é muito pequena (geralmente na ordem de 10−4 a 10−5).

    Interpretação: A simulação demonstra a LGN. A frequência relativa de cada face se estabiliza e se aproxima do valor teórico de 1/6, confirmando que, para um grande número de ensaios, a estimativa empírica é uma boa aproximação da probabilidade real.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Questão 2 – Dado Não Uniforme e Probabilidade Condicional
1. Distribuição de Probabilidade Não Uniforme

Vou propor uma distribuição que favorece faces baixas e a face 6.

    Faces: {1,2,3,4,5,6}

    Probabilidades (Pi​):

        P1​=0.20 (Mais provável)

        P2​=0.15

        P3​=0.10

        P4​=0.10

        P5​=0.05 (Menos provável)

        P6​=0.40 (Muito mais provável)

Verificação: ∑Pi​=0.20+0.15+0.10+0.10+0.05+0.40=1.00. Válida!

------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Questão 2 – 4. Consistência da Soma das Probabilidades

A soma das probabilidades teóricas é 1.00 (por construção).

A soma das probabilidades estimadas empiricamente é:
i=1∑6​P(Empıˊricai​)=i=1∑6​NFrequeˆnciai​​=N∑i=16​Frequeˆnciai​​=NN​=1.00

    Consistência: A soma das probabilidades estimadas é sempre 1.0 (ou muito, muito próxima, dependendo de arredondamentos computacionais), porque a soma das frequências observadas de todos os resultados possíveis deve ser, por definição, igual ao número total de lançamentos (N).

    Possíveis Desvios: O único "desvio" seria se o código tivesse algum erro de contagem ou se usássemos arredondamentos grosseiros ao imprimir o resultado. No cálculo interno (sem arredondamento), a soma é exatamente 1.0.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

