#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando bibliotecas

import pandas as pd
import numpy as np
import tensorflow as tf

tf.__version__


# In[2]:


# Importando o dataset

dataset = pd.read_csv("cracow_apartments.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[3]:


# Separando os dados em treino e teste

# Código que separa os dados entre treino e teste. 80-20%, respectivamente
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[4]:


# Construindo a Rede Neural

ann = tf.keras.models.Sequential() # inicia a rede neural
ann.add(tf.keras.layers.Dense(units = 10, activation = 'relu')) # Adiciona a camada de entrada e a primeira camada escondida
ann.add(tf.keras.layers.Dense(units = 10, activation = 'relu')) # Adiciona mais uma camada escondida com 10 neurônios
ann.add(tf.keras.layers.Dense(units = 1)) # Adicionando a camada de saída
# Não se coloca a função de ativação pois estamos fazendo uma regressão!!!

ann.compile(optimizer = 'adam', loss = 'mean_squared_error') # Compila o modelo


# In[5]:


# Treinando a Rede Neural como modelo de Regressão

ann.fit(X_train, y_train, batch_size = 32, epochs = 1000)


# In[6]:


# Prevendo o resultado dos testes

y_pred = ann.predict(X_test)
np.set_printoptions(precision= 2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# In[7]:


# Avaliando o modelo

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

