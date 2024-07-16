"""Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape,
genera un array casuale e calcola la somma degli elementi."""


import numpy as np

array = np.linspace(0, 1, 12)
print(array)
print(np.sum(array))
array_nuovo=array.reshape(3,4)
print(array_nuovo)
array2=np.random.rand(3,4)
print(array2)
print(np.sum(array2))



