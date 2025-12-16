# Povoa
Estatística

# Projeto de Simulação Estatística e Probabilidade

Este projeto aplica simulação computacional (Método de Monte Carlo e amostragem) para modelar e analisar diferentes variáveis aleatórias. O foco é na comparação entre resultados empíricos e teóricos e na discussão da Lei dos Grandes Números.

## 🎯 Abordagem Adotada

Utilizei a biblioteca **NumPy** para geração eficiente de números pseudo-aleatórios e a **Matplotlib** para visualização (Histogramas).

* **Simulação Discreta (Q1 e Q2):** Uso da função `np.random.choice()` para simular lançamentos com probabilidades especificadas.
* **Simulação Contínua (Q3):** Uso de `np.random.normal()` seguido de uma técnica de **filtragem** para implementar o truncamento da distribuição.
* **Monte Carlo (Q4):** Repetição de um processo aleatório (concessão de empréstimos) múltiplas vezes para estimar uma expectativa (número médio de clientes).

## ⚙️ Hipóteses de Modelagem

1.  **Aleatoriedade:** Os geradores de números pseudo-aleatórios (PRNGs) do NumPy são considerados de alta qualidade e suficientes para representar a aleatoriedade dos fenômenos estudados.
2.  **i.i.d.:** Todas as simulações assumem eventos independentes e identicamente distribuídos (i.i.d.).
3.  **Q4 (Empréstimos):** O valor do empréstimo segue uma Distribuição Uniforme, e o capital é consumido até que não seja possível cobrir o próximo empréstimo.

## 🚀 Como Executar

1.  **Requisitos:** Python 3.x, NumPy, Matplotlib.
2.  **Instalação:**
    ```bash
    pip install numpy matplotlib
    ```
3.  **Execução:**
    Para rodar a simulação de cada questão:
    ```bash
    python src/questao1_dado_honesto.py
    # Repetir para os demais scripts
    ```
