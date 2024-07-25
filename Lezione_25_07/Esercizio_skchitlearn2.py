"""Utilizzate la linear regression per analizzare il dataframe
di esempio con Fabbisogno calorico giornaliero di un uomo
in base alla sua età, allenate l'algoritmo,
testatelo e poi realizzate un grafico."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

file="fabbisogno calorico.csv"
dati=pd.read_csv(file)
X=dati[["età"]]
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