import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn import linear_model
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import PredictionErrorDisplay



def grafico1():
    sito="https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"

    dati=pd.read_csv(sito)
    diz_dati={"blue-collar": 9,
            "technician": 5,
            "management": 10,
            "services": 7,
            "retired":4,
            "housemaid": 3,
            "admin.": 8,
            "unemployed":1,
            "entrepreneur": 11,
            "self-employed": 6,
            "student":2,
            "unknown": 0}

    diz_dati2={"yes": 2,
            "no": 1}
    diz_dati3={"yes": 2,
            "no": 1}
    dati["job"]= dati["job"].map(diz_dati)

    dati["housing"]= dati["housing"].map(diz_dati2)
    dati["loan"]=dati["loan"].map(diz_dati3)
    dati = dati.dropna(subset=["housing"])
    dati = dati.dropna(subset=["loan"])

    X=dati[["age","job","cons_conf_idx","cons_price_idx","housing","campaign","loan","duration"]]
    y=dati["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modello=linear_model.LogisticRegression(max_iter=1000).fit(X_train,y_train)


    y_pred=modello.predict(X_train)

    y_test_pred = modello.predict(X_test)




    train_accuracy = accuracy_score(y_train, y_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    matrice=confusion_matrix(y_test, y_test_pred)
    #print(train_accuracy,test_accuracy,matrice)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sì'], yticklabels=['No', 'Sì'])
    plt.xlabel('Predizione')
    plt.ylabel('Reale')
    plt.title('Matrice di Confusione')
    plt.show()

def grafico2():
    sito="https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"

    dati=pd.read_csv(sito)
    diz_dati={"blue-collar": 9,
            "technician": 5,
            "management": 10,
            "services": 7,
            "retired":4,
            "housemaid": 3,
            "admin.": 8,
            "unemployed":1,
            "entrepreneur": 11,
            "self-employed": 6,
            "student":2,
            "unknown": 0}

    diz_dati2={"yes": 2,
            "no": 1}
    
    dati["job"]= dati["job"].map(diz_dati)

    dati["housing"]= dati["housing"].map(diz_dati2)
    
    dati = dati.dropna(subset=["housing"])
    

    X=dati[["age","job","cons_conf_idx","cons_price_idx","housing"]]
    y=dati["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modello=linear_model.LogisticRegression(max_iter=1000).fit(X_train,y_train)


    y_pred=modello.predict(X_train)

    y_test_pred = modello.predict(X_test)




    train_accuracy = accuracy_score(y_train, y_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    matrice=confusion_matrix(y_test, y_test_pred)
    #print(train_accuracy,test_accuracy,matrice)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sì'], yticklabels=['No', 'Sì'])
    plt.xlabel('Predizione')
    plt.ylabel('Reale')
    plt.title('Matrice di Confusione')
    plt.show()

def grafico3():

    sito="https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"

    dati=pd.read_csv(sito)
    diz_dati={"blue-collar": 9,
            "technician": 5,
            "management": 10,
            "services": 7,
            "retired":4,
            "housemaid": 3,
            "admin.": 8,
            "unemployed":1,
            "entrepreneur": 11,
            "self-employed": 6,
            "student":2,
            "unknown": 0}

    diz_dati2={"yes": 2,
            "no": 1}
    diz_dati3={"yes": 2,
            "no": 1}
    dati["job"]= dati["job"].map(diz_dati)



    X=dati[["age","job","cons_conf_idx","cons_price_idx"]]
    y=dati["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modello=linear_model.LogisticRegression(max_iter=1000).fit(X_train,y_train)


    y_pred=modello.predict(X_train)

    y_test_pred = modello.predict(X_test)




    train_accuracy = accuracy_score(y_train, y_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    matrice=confusion_matrix(y_test, y_test_pred)
    #print(train_accuracy,test_accuracy,matrice)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sì'], yticklabels=['No', 'Sì'])
    plt.xlabel('Predizione')
    plt.ylabel('Reale')
    plt.title('Matrice di Confusione')
    plt.show()

def grafico4():
    sito="https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"

    dati=pd.read_csv(sito)
    diz_dati={"blue-collar": 9,
            "technician": 5,
            "management": 10,
            "services": 7,
            "retired":4,
            "housemaid": 3,
            "admin.": 8,
            "unemployed":1,
            "entrepreneur": 11,
            "self-employed": 6,
            "student":2,
            "unknown": 0}

    diz_dati2={"basic.4y": 1,
               "unknown": 0,
               "university.degree": 5,
               "high.school": 4,
               "basic.9y":3,
               "basic.6y": 2,
               "professional.course":


    dati["job"]= dati["job"].map(diz_dati)



    X=dati[["age","job","cons_conf_idx","cons_price_idx"]]
    y=dati["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modello=linear_model.LogisticRegression(max_iter=1000).fit(X_train,y_train)


    y_pred=modello.predict(X_train)

    y_test_pred = modello.predict(X_test)




    train_accuracy = accuracy_score(y_train, y_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    matrice=confusion_matrix(y_test, y_test_pred)
    #print(train_accuracy,test_accuracy,matrice)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sì'], yticklabels=['No', 'Sì'])
    plt.xlabel('Predizione')
    plt.ylabel('Reale')
    plt.title('Matrice di Confusione')
    plt.show()

grafico1()
grafico2()
grafico3()










#print(dati)