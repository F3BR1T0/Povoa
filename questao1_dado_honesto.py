# questao1_dado_honesto.py
import numpy as np

N_LANCAMENTOS = 1000000 # 10^6 lançamentos
FACES = np.arange(1, 7)
PROB_TEORICA = np.full(6, 1/6)

# 1. & 2. Simulação
resultados = np.random.choice(FACES, size=N_LANCAMENTOS, p=PROB_TEORICA)

# Estimando a distribuição empírica
# np.bincount conta as ocorrências de cada valor. [1:] ignora a contagem do valor 0.
frequencias = np.bincount(resultados)[1:] 
prob_empirica = frequencias / N_LANCAMENTOS

print("--- Q1: Simulação de Dado Honesto (N={}) ---".format(N_LANCAMENTOS))

# 3. Comparação dos Resultados
print("Face | P(Teórica) | P(Empírica) | Diferença Absoluta")
print("-----|------------|-------------|--------------------")
for i in range(6):
    face = FACES[i]
    p_teor = PROB_TEORICA[i]
    p_emp = prob_empirica[i]
    diff = abs(p_emp - p_teor)
    print(f" {face}   | {p_teor:.6f} | {p_emp:.6f} | {diff:.6f}")
