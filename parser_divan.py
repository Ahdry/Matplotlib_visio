import csv

prices = [
    28990,15990,17990,7990,49990,67990,26990,54990,9990,62990,19990,57990,54990,10990,22990,59990,27990,
    64990,19990,173970,12990,109990,22990,66990,7990,17990,78980,42990,64990,24990,56990,31990,59990,
    163970,66990,68990,47990,39990,79990,69990,69990,47990,32990,83990,26990,4590,59990,38990
]

with open("sofa_prices.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["price_rub"])
    for p in prices:
        writer.writerow([p])

import os

import pandas as pd
df = pd.read_csv('sofa_prices.csv')
print(df.head())

print("Текущая рабочая директория:", os.getcwd())
print("Содержимое папки:", os.listdir())

try:
    df = pd.read_csv('sofa_prices.csv')
    print(df.head())
except Exception as e:
    print("ОШИБКА:", e)


import matplotlib.pyplot as plt

df = pd.read_csv('sofa_prices.csv')

prices = df['price_rub']

mean = prices.mean()

plt.figure(figsize=(10,6))
plt.hist(prices, bins=15, color='skyblue', edgecolor='black', alpha=0.8)
plt.axvline(mean, color='red', linestyle='--', label=f'Средняя цена: {int(mean):,} руб.')
plt.title('Гистограмма цен на диваны (divan.ru, Кемерово)')
plt.xlabel('Цена, руб.')
plt.ylabel('Количество')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
