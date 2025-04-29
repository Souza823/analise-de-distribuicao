import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros
sigma = 0.02           # desvio padrão em kg (20 g)
x_limite = 400         # limite inferior desejado
p = 0.10               # probabilidade desejada abaixo de 400 kg

# Obter z-score associado à cauda inferior de 10%
z = norm.ppf(p)

# Calcular a média necessária
mu = x_limite - z * sigma
print(f"Média ajustada: {mu:.4f} kg")

# Gerar valores para o gráfico
x_vals = np.linspace(399.95, 400.1, 1000)
y_vals = norm.pdf(x_vals, loc=mu, scale=sigma)

# Plotar a distribuição
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, color='blue', label='Distribuição Normal')
plt.fill_between(x_vals, y_vals, where=(x_vals < x_limite), color='red', alpha=0.5, label='10% abaixo de 400 kg')
plt.axvline(x_limite, color='red', linestyle='--', label='Limite: 400 kg')
plt.axvline(mu, color='green', linestyle='--', label=f'Média ajustada: {mu:.4f} kg')

# Personalização do gráfico
plt.title('Distribuição Normal do Peso dos Pacotes')
plt.xlabel('Peso (kg)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
