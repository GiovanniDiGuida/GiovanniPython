import numpy as np
import random

array= np.random.randint(10,50,20)
print(array)

print(array[0:11])

print(array[-5:])

print(array[5:15])

indice=[2]
print(array[indice])

indice2=[5,6,7,8,9,10]
array[indice2]=99
print(array)


