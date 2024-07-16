import numpy as np

array=np.linspace(0,10,50)
print(array)

array2=np.random.rand(50)
print(array2)

array_uniti=array + array2
print(array_uniti)
print(np.sum(array_uniti))
print(array_uniti[array_uniti >5])
print(np.sum(array_uniti[array_uniti >5]))