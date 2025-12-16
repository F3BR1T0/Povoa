

## 🎯 Questão 5 – 1. Análise Estatística e Interpretação
1. Comparação Simulação e Teoria

<img width="927" height="212" alt="tabela" src="https://github.com/user-attachments/assets/0cfb5494-f15a-4f5c-a93e-0d0641335890" />

🎯 Questão 5 – 2. Fontes de Erro

    Erro Estatístico (Amostral): É a diferença inerente entre a amostra (simulação finita N) e a população (distribuição teórica infinita). É a razão pela qual P(Empírica) <> =P(Teórica) mesmo em Q1. É o erro que diminui com o aumento de N.

    Erro Computacional:

        Pseudo-aleatoriedade: O computador usa um algoritmo (PRNG) para gerar números que parecem aleatórios, mas são determinísticos. Se o período do gerador for curto ou se houver viés no algoritmo, isso introduz erro.

        Arredondamento/Ponto Flutuante: Erros minúsculos (e.g., ϵ) que ocorrem quando o computador representa números reais (1/6 <> =0.16666666666666666).

🎯 Questão 5 – 3. Impacto do Aumento do Número de Simulações (N)

O aumento do número de simulações (N) aumenta a precisão dos resultados por causa da Lei dos Grandes Números (LGN):

    Diminuição do Erro Amostral: A LGN garante que a média empírica converge para o valor esperado teórico. Quanto maior N, mais próxima estará a estimativa, reduzindo o erro amostral.

    Maior Estabilidade: O resultado se torna menos sensível a flutuações aleatórias de curto prazo. As estimativas (médias, probabilidades) se tornam mais estáveis (o Desvio Padrão da Média diminui).

🎯 Questão 5 – 4. Papel da Simulação Computacional em Problemas Reais

A simulação computacional (como Monte Carlo) é crucial para problemas reais onde o cálculo analítico é difícil ou impossível.

    Exemplos Reais:

        Finanças: Precificação de opções e derivativos complexos. (Q4 é um exemplo simplificado disso).

        Engenharia: Avaliação de confiabilidade e risco em sistemas complexos (e.g., falha de componentes).

        Saúde: Modelagem de epidemias (espalhamento de doenças) ou ensaios clínicos com resultados aleatórios.

    Função: Ela permite que se experimente cenários (o "o que aconteceria se...") em um ambiente virtual, testando a robustez de modelos e obtendo estimativas confiáveis de quantidades que dependem de variáveis aleatórias complexas. É uma ferramenta fundamental para tomada de decisões sob incerteza.
