import numpy as np
import matplotlib.pyplot as plt

"""x = [0.2, 0.8, 0.5]
y = [0.2, 0.2, 0.7]"""
x = np.random.rand(50)
y = np.random.rand(50)
colori=["blue","red","yellow","yellow","black","green"]
plt.figure()
plt.scatter(x, y, color=np.random.choice(colori, len(x)))
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()