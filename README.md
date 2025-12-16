### **Nota:** o nome próprio `Povoa` para o diretório em questão foi usado apenas para homenagem interna. Proibido o uso para fins monetários ou comerciais.   
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prova de Estatística 

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

## 🚀 Como Executar (Execução via Visual Studio)

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
## 📁 Estrutura do Repositório (Execução via Google Colab)

Como o projeto será executado no Google Colab, a entrega deve ser feita em formato de Notebooks (.ipynb), onde o código e as explicações coexistem.

| Arquivo (Notebook) | Descrição |
| :--- | :--- |
| **`questao1_dado_honesto.ipynb`** | Simulação de variável discreta (dado justo) e Lei dos Grandes Números. |
| **`questao2_dado_viciado.ipynb`** | Proposta e estimação de distribuição não uniforme. |
| **`questao3_normal_truncada.ipynb`** | Simulação e análise de estatísticas de uma distribuição contínua truncada. |
| **`questao4_monte_carlo.ipynb`** | Aplicação do Método de Monte Carlo para estimativa de clientes atendidos. |
| **`questao5_analise_final (sem execução)`** | Análise comparativa e discussão dos resultados e erros obtidos nas questões anteriores. |
| `README.md` | Este arquivo, com explicação da abordagem e execução. |

* **Nota:** Converter o arquivo `.py` para `.ipynb` antes da execução no GOOGLE COLAB.

## 🚀 Como Executar no Google Colab

Como o ambiente é o Google Colab (Notebooks Jupyter), a execução é interativa e simplificada.

1.  **Configuração do Ambiente:**
    * O Colab já vem com as bibliotecas **NumPy** e **Matplotlib** instaladas por padrão, então não é necessário rodar `pip install`. Se for necessário, a instalação deve ser feita na primeira célula do notebook (`!pip install biblioteca`).

2.  **Abertura e Execução:**
    * **Método 1 (Upload):** Faça o upload dos arquivos `.ipynb` diretamente para o seu Google Drive ou para a sessão do Colab.
    * **Método 2 (GitHub):** Se o repositório estiver no GitHub, o Notebook pode ser aberto diretamente na interface do Colab através da URL (por exemplo, `colab.research.google.com/github/...`).

3.  **Processo:**
    * Abra o Notebook da questão desejada (e.g., `questao1_dado_honesto.ipynb`).
    * Execute cada célula sequencialmente, clicando no botão de *play* ao lado da célula ou usando `Shift + Enter`.
    * Os resultados (tabelas e gráficos) aparecerão diretamente abaixo das células de código correspondentes, sem a necessidade de um terminal externo.
