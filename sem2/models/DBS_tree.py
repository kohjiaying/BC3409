import pandas as pd
import os

print(os.getcwd())
df = pd.read_csv("DBS_SingDollar.csv")
X = df.loc[:,["SGD"]]
Y = df.loc[:,["DBS"]]

from sklearn import tree
treeModel = tree.DecisionTreeRegressor() #regressor because continuous
treeModel.fit(X,Y)

from joblib import dump
dump(treeModel,'DBS_tree')