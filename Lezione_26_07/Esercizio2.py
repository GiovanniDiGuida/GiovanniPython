from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.inspection import DecisionBoundaryDisplay

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 1, :2]
y = y[y != 1]


def plot_training_data_with_decision_boundary(kernel="linear"):
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    modello= svm.SVC(kernel=kernel, gamma=2).fit(X_train, y_train)
    y_pred=modello.predict(X_test)
    print(y_pred)

plot_training_data_with_decision_boundary()