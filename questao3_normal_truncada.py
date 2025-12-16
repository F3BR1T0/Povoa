# questao3_normal_truncada.py
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
MEDIA = 1500.0
DP = 300.0
L_INF = 500.0
L_SUP = 2000.0
N_AMOSTRAS = 10000

# 2. Simulação com Truncamento (Filtragem)
# Geramos um número extra de amostras (e.g., o dobro) para garantir N_AMOSTRAS após o filtro.
amostras_brutas = np.random.normal(loc=MEDIA, scale=DP, size=int(N_AMOSTRAS * 2))

# Aplicando o truncamento
amostras_truncadas = amostras_brutas[
    (amostras_brutas >= L_INF) & 
    (amostras_brutas <= L_SUP)
][:N_AMOSTRAS] # Seleciona apenas as N_AMOSTRAS necessárias

# 3. Estatísticas Descritivas
media_simulada = np.mean(amostras_truncadas)
mediana_simulada = np.median(amostras_truncadas)
variancia_simulada = np.var(amostras_truncadas)

print("--- Q3: Estatísticas Descritivas (Normal Truncada) ---")
print("Média Simulada: {:.2f}".format(media_simulada))
print("Mediana Simulada: {:.2f}".format(mediana_simulada))
print("Variância Simulada: {:.2f}".format(variancia_simulada))
print("Desvio Padrão Simulada: {:.2f}".format(np.std(amostras_truncadas)))

# Preparação para o Histograma (Ponto 4)
plt.figure(figsize=(9, 5))
plt.hist(amostras_truncadas, bins=30, density=True, color='lightcoral', edgecolor='black', alpha=0.7)
plt.axvline(media_simulada, color='blue', linestyle='dashed', linewidth=1, label=f'Média: {media_simulada:.2f}')
plt.xlim(L_INF, L_SUP)
