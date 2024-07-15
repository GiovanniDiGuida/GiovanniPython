import numpy as np


arr= np.array([1,2,3,4,5])
print(arr)

# Creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

#print("Forma dell'array:", arr.shape)
#print("Somma degli elementi:", arr.sum())
#print("Media degli elementi:", arr.mean())
#print("Valore massimo:", arr.max())  
#print("Indice del valore massimo:", arr.argmax())
arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype) 

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)