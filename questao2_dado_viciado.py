# questao2_dado_viciado.py
import numpy as np

N_LANCAMENTOS = 500000 
FACES = np.arange(1, 7)
PROB_NAO_UNIFORME = np.array([0.05, 0.10, 0.15, 0.20, 0.35, 0.15]) # Distribuição proposta

# 2. Implementação do Simulador
resultados_viciados = np.random.choice(FACES, size=N_LANCAMENTOS, p=PROB_NAO_UNIFORME)

# 3. Estimação Empírica
frequencias_viciadas = np.bincount(resultados_viciados)[1:]
prob_empirica_viciada = frequencias_viciadas / N_LANCAMENTOS
soma_empirica = np.sum(prob_empirica_viciada)

print("--- Q2: Simulação de Dado Viciado (N={}) ---".format(N_LANCAMENTOS))
print("Face | P(Teórica) | P(Empírica) | Diferença")
print("-----|------------|-------------|-----------")
for i in range(6):
    face = FACES[i]
    p_teor = PROB_NAO_UNIFORME[i]
    p_emp = prob_empirica_viciada[i]
    diff = abs(p_emp - p_teor)
    print(f" {face}   | {p_teor:.4f}     | {p_emp:.4f}     | {diff:.4f}")

print("\nSoma das Probabilidades Estimadas: {:.10f}".format(soma_empirica))
