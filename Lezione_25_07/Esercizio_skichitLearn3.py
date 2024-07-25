
"""Partendo dal dataset a questo link https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression
, utilizzate i dati sulle ore di studio e le ore di sonno per prevedere
quanto queste caratteristiche influiscono sull'indice di prestazione degli studenti.
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

file=("Student_Performance.csv")
dati=pd.read_csv(file)
X=dati[["Hours Studied","Sleep Hours"]]
y=dati["Performance Index"]
X_train, X_test, y_train, y_test = train_test_split(X, y)
modello= LinearRegression().fit(X_train,y_train)
y_pred=modello.predict(X_test)

print(y_pred)

def relazione1():
    plt.scatter(X_test["Hours Studied"], y_test, color="black")
    plt.plot(X_test[["Hours Studied"]], y_pred, color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()

def relazione2():
    plt.scatter(X_test["Sleep Hours"], y_test, color="black")
    plt.plot(X_test["Sleep Hours"], y_pred, color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()

relazione1()
relazione2()
