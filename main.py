import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000

# Генерация данных
data = np.random.normal(mean, std_dev, num_samples)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, color='skyblue', edgecolor='black', alpha=0.7)

plt.axvline(mean, color='red', linestyle='--', linewidth=2, label='Среднее')
plt.axvline(mean + std_dev, color='green', linestyle='--', linewidth=2, label='+1 std')
plt.axvline(mean - std_dev, color='green', linestyle='--', linewidth=2, label='-1 std')

plt.title('Гистограмма нормального распределения (mean=0, std=1)', fontsize=14)
plt.xlabel('Значение', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
