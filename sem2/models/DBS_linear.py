import pandas as pd
import os

print(os.getcwd())
df = pd.read_csv("DBS_SingDollar.csv")
X = df.loc[:,["SGD"]]
Y = df.loc[:,["DBS"]]

from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X,Y)
pred = model.predict(X)
print(pred)

from sklearn.metrics import mean_squared_error
rmse = mean_squared_error(Y,pred)**0.5

from joblib import dump
dump(model,'DBS_linear')

from joblib import load
model = load('DBS_linear')

X = [[1.4]]
pred = model.predict(X)
print(pred)