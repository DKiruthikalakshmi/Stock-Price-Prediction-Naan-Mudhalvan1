# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WLsJihlrXLbbluZ2rvLk9lZV6uyMmu_c
"""

import pandas as pd
df = pd.read_csv('MSFT.csv')

df.info()

cols = ['Date','Open']
df = df.drop(cols, axis=1)

df.info()

df = df.dropna()

df.info()

dummies = []
cols = ['High', 'Low']
for col in cols:
   dummies.append(pd.get_dummies(df[col]))

MSFT_dummies = pd.concat(dummies, axis=1)

df = pd.concat((df,MSFT_dummies), axis=1)

df = df.drop(['High','Low'], axis=1)

df.info()

df['Close'] = df['Close'].interpolate()

df.info()

X = df.values
y = df['Adj Close'].values

import numpy as np

X = np.delete(X, 1, axis=1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Commented out IPython magic to ensure Python compatibility.
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

data=pd.read_csv('MSFT.csv')

training_set=data.iloc[:,1:2].values

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
scaled_training_set=scaler.fit_transform(training_set)
scaled_training_set

x_train=[]
y_train=[]
for i in range(60,1258):
  x_train.append(scaled_training_set[i-60:i,0])
  y_train.append(scaled_training_set[i,0])
x_train=np.array(x_train)
y_train=np.array(y_train)

print(x_train.shape)

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout

regressor=Sequential()
regressor.add(LSTM(units=50,return_sequences=True,input_shape=(X_train,shape[1],1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50,return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50,return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=1))

regressor.compile(optimizer='adam',loss='mean_squared_error')
regressor.fit(X_train,y_train,epochs=10,batch_size=32)