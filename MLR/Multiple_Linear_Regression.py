#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando as bibliotecas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Importando o dataset

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, : -1].values
y = dataset.iloc[:,-1].values

dataset.head()
#Precisa colocar ".values" porque os argumentos para o método "fit" são do tipo array


# In[3]:


# Tratando dados categóricos

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [3])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X))


# In[4]:


# Dividindo os dados entre treino e teste

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)


# In[5]:


# Treinando um modelo de Regressão Linear Múltipla nos dados de treino

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


# In[6]:


# Prevendo os dados de teste

y_pred = regressor.predict(X_test)
np.set_printoptions(precision =2) # define apenas duas casas decimais quando for printar na tela
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# In[7]:


# Avaliando a performace do modelo

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

