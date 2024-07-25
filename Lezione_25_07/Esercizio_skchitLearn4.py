"""Partendo dal dataset a questo link https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction , utilizzate i dati sugli anni delle case e la
distanza dalla stazione metro per prevedere quanto queste caratteristiche influiscono sul costo delle case."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import PredictionErrorDisplay



file=("Real Estate.csv")
dati=pd.read_csv(file)
X=dati[["X2 house age","X3 distance to the nearest MRT station"]]
y=dati["Y house price of unit area"]

X_train, X_test, y_train, y_test = train_test_split(X, y)
modello= LinearRegression().fit(X_train,y_train)
y_pred=modello.predict(X_test)

def errore():
    display = PredictionErrorDisplay(y_true=y_test, y_pred=y_pred)
    display.plot()
    plt.xticks(())
    plt.yticks(())
    plt.show()

def relazione1():
    plt.scatter(X_test["X2 house age"], y_test, color="black")
    plt.plot(X_test[["X2 house age"]], y_pred, color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()

def relazione2():
    plt.scatter(X_test["X3 distance to the nearest MRT station"], y_test, color="black")
    plt.plot(X_test["X3 distance to the nearest MRT station"], y_pred, color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()

errore()
relazione1()
relazione2()

