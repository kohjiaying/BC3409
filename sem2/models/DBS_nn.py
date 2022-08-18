import pandas as pd
import os

print(os.getcwd())
df = pd.read_csv("DBS_SingDollar.csv")
X = df.loc[:,["SGD"]]
Y = df["DBS"] 

from sklearn.neural_network import MLPRegressor
#hidden layer 1 is 3 neurons and hidden layer 2 is 4 neurons
MLPmodel = MLPRegressor(solver="lbfgs", hidden_layer_sizes=(3,4)) 
MLPmodel.fit(X,Y)

from joblib import dump
dump(MLPmodel,'DBS_MLP')