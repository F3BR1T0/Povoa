# questao4_monte_carlo.py
import numpy as np

# 2. Parâmetros (Hipóteses)
K0 = 100000.0  # Capital Inicial
E_MIN = 1000.0 # Valor Mínimo do Empréstimo
E_MAX = 10000.0 # Valor Máximo do Empréstimo
N_SIMULACOES = 20000 # Número de experimentos Monte Carlo

# 1. Função de Modelagem (Um único experimento)
def simular_fundo(capital_inicial, e_min, e_max):
    capital_atual = capital_inicial
    clientes_atendidos = 0
    
    while True:
        # Sorteia o valor do próximo empréstimo
        emprestimo = np.random.uniform(low=e_min, high=e_max)
        
        # Verifica se o capital pode cobrir
        if capital_atual >= emprestimo:
            capital_atual -= emprestimo
            clientes_atendidos += 1
        else:
            # Não é possível atender o próximo cliente. Fundo esgotado (para empréstimos viáveis).
            break 
            
    return clientes_atendidos

# 3. Estimação por Simulação (Monte Carlo)
resultados_montecarlo = [simular_fundo(K0, E_MIN, E_MAX) for _ in range(N_SIMULACOES)]

num_esperado_clientes = np.mean(resultados_montecarlo)
dp_clientes = np.std(resultados_montecarlo)

print("--- Q4: Método de Monte Carlo (Fundo de Empréstimos) ---")
print("Capital Inicial: R$ {}".format(K0))
print("Número Esperado de Clientes Atendidos: {:.2f}".format(num_esperado_clientes))
print("Desvio Padrão (Variabilidade): {:.2f}".format(dp_clientes))
