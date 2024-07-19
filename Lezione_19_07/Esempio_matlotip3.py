import matplotlib.pyplot as plt



x = [1, 1, -1, -1, 1]
y = [1, -1, -1, 1, 1]


plt.rcParams['figure.facecolor'] = 'white'
plt.figure()

plt.plot(x, y)

plt.title('Grafico a Linee')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')
#plt.rcParams['figure.facecolor'] = 'black'
#plt.rcParams['figure.figsize'] = [10, 10]  

plt.show()