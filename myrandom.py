import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)
y = np.random.rand(5)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.7, s=80)
plt.title('Диаграмма рассеяния для 5 случайных пар (numpy.random.rand)')
plt.xlabel('X — Случайные значения')
plt.ylabel('Y — Случайные значения')
plt.grid(alpha=0.3)
plt.show()
