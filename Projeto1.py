import numpy as np

# Definindo o número de amostras
n_samples = 100

# Gerando dados fictícios
np.random.seed(42)  # Para reprodutibilidade
heights = np.random.normal(loc=170, scale=10, size=n_samples)  # Alturas em cm
weights = np.random.normal(loc=70, scale=15, size=n_samples)  # Pesos em kg
ages = np.random.randint(18, 65, size=n_samples)  # Idades entre 18 e 65 anos

# Consolidando em uma matriz de dados
data = np.column_stack((heights, weights, ages))

# Exibindo os primeiros 5 registros para verificação
print("Altura | Peso | Idade")
print(data[:5])

# Cálculos estatísticos para altura
mean_height = np.mean(heights)
median_height = np.median(heights)
std_dev_height = np.std(heights)
variance_height = np.var(heights)

# Exibindo os resultados
print(f"Média das Alturas: {mean_height:.2f} cm")
print(f"Mediana das Alturas: {median_height:.2f} cm")
print(f"Desvio Padrão das Alturas: {std_dev_height:.2f} cm")
print(f"Variância das Alturas: {variance_height:.2f} cm")

# Correlação entre altura e peso
correlation_height_weight = np.corrcoef(heights, weights)[0, 1]
print(f"Correlação entre Altura e Peso: {correlation_height_weight:.2f}")

import matplotlib.pyplot as plt

# Histograma das alturas
plt.figure(figsize=(10, 6))
plt.hist(heights, bins=15, color='skyblue', edgecolor='black')
plt.title('Distribuição de Alturas')
plt.xlabel('Altura (cm)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Scatter plot entre altura e peso
plt.figure(figsize=(10, 6))
plt.scatter(heights, weights, color='green')
plt.title('Altura vs Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.grid(True)
plt.show()

# Boxplot das alturas
plt.figure(figsize=(8, 6))
plt.boxplot(heights, patch_artist=True)
plt.title('Boxplot das Alturas')
plt.ylabel('Altura (cm)')
plt.grid(True)
plt.show()