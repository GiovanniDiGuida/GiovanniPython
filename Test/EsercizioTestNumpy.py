import numpy as np

temperature=np.random.randint(10, 30, 24)
print(temperature)
temperatura_media = np.mean(temperature)
temperatura_minima = np.min(temperature)
temperatura_massima = np.max(temperature)
print(temperatura_media)
print(temperatura_massima)
print(temperatura_minima)

aumento=0.2*7
temperatura_probabile=temperatura_media+aumento
print(temperatura_probabile)