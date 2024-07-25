"""Utilizzate la linear regression per analizzare il dataframe di esempio
in cui abbiamo le Calorie bruciate in base al peso della persona che fa
esercizio fisico con la montain bike,
allenate l'algoritmo, testatelo e poi realizzate un grafico"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

file="calories.csv"
dati=pd.read_csv(file)

X=dati[["kg"]]
y=dati["calories"]
X_train, X_test, y_train, y_test = train_test_split(X, y)
modello = LinearRegression()
modello.fit(X_test, y_test)
y_pred=modello.predict(X_test)

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)
plt.xticks(())
plt.yticks(())

plt.show()
