import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da distribuição normal
mu = 60        # média (kg)
sigma = 3      # desvio padrão (kg)

# Pontos de interesse
x1 = 55
x2 = 65

# Cálculo das probabilidades
p_menor_55 = norm.cdf(x1, loc=mu, scale=sigma)
p_maior_65 = 1 - norm.cdf(x2, loc=mu, scale=sigma)
p_total = p_menor_55 + p_maior_65

# Exibir resultados
print(f"Probabilidade de X < 55 kg: {p_menor_55:.4f}")
print(f"Probabilidade de X > 65 kg: {p_maior_65:.4f}")
print(f"Total fora do intervalo 55-65 kg: {p_total:.4f}")

# Criar valores para o eixo x
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plotar a curva da distribuição normal
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribuição Normal (μ=60, σ=3)', color='black')

# Sombrear área P(X < 55)
x_fill1 = np.linspace(mu - 4*sigma, x1, 500)
plt.fill_between(x_fill1, norm.pdf(x_fill1, mu, sigma), color='red', alpha=0.5, label='P(X < 55 kg)')

# Sombrear área P(X > 65)
x_fill2 = np.linspace(x2, mu + 4*sigma, 500)
plt.fill_between(x_fill2, norm.pdf(x_fill2, mu, sigma), color='blue', alpha=0.5, label='P(X > 65 kg)')

# Linhas verticais
plt.axvline(x1, color='red', linestyle='--')
plt.axvline(x2, color='blue', linestyle='--')
plt.axvline(mu, color='green', linestyle='--', label='Média (60 kg)')

# Personalização
plt.title('Distribuição Normal do Peso dos Sacos')
plt.xlabel('Peso (kg)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




