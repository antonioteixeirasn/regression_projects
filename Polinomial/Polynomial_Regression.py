#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando as bibliotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Importando o dataset

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values


# In[3]:


# Separando os dados entre treino e teste

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[4]:


# Treinando o modelo de Regressão Polinomial

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X_train) # essa linha é para "normalizar" os dados de entrada
regressor = LinearRegression()
regressor.fit(X_poly, y_train)


# In[5]:


# Prevendo os resultados de teste

y_pred = regressor.predict(poly_reg.transform(X_test))
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# In[6]:


# Avaliando a performace do modelo

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

