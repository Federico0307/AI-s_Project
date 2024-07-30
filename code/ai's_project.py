# -*- coding: utf-8 -*-
"""AI's Project.ipynb

Original file is located at https://colab.research.google.com/drive/1IQKWwqjGtLem376BrZ8WQdk7wJ_Ao7du

#Project of Artificial Intelligence

The following code is related to the project realised for the Artificial Intelligence course. The project consists of analysing the prediction of the future cost of present cars from the downloaded dataset (via link: https://www.kaggle.com/datasets/mrsimple07/car-prices-prediction-data)

## Preprocessing
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import metrics

# loading the data from csv file to pandas dataframe
dataset = pd.read_csv('CarPricesPrediction.csv')

# inspecting the first 5 rows of the dataframe
dataset.head()

# checking the number of rows and columns
dataset.shape

# getting some information about the dataset
dataset.info()

# checking the number of missing values
dataset.isnull().sum()

# checking the distribution of categorical data
print(dataset.Condition.value_counts())
#print(dataset.Seller_Type.value_counts())
#print(dataset.Transmission.value_counts())

# encoding "Condition" Column
dataset.replace({'Condition':{'Fair':0,'Good':1,'Excellent':2}},inplace=True)

X = dataset.drop(['Unnamed: 0', 'Make', 'Model', 'Price'], axis=1)
y = dataset['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = None)

"""## Models Training and Prediction"""

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

"""### Linear Regression"""

lr = LinearRegression()
lr.fit(X_train, y_train)

# prediction on Training data
y_train_pred = lr.predict(X_train)

# R squared Error
error_score = metrics.r2_score(y_train, y_train_pred)
print("R squared Error : ", error_score)

plt.scatter(y_train, y_train_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

# prediction on Training data
y_test_pred = lr.predict(X_test)

# R squared Error
error_score = metrics.r2_score(y_test, y_test_pred)
print("R squared Error : ", error_score)

plt.scatter(y_test, y_test_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

"""### Random Forest"""

rf = RandomForestRegressor()
rf.fit(X_train, y_train)

# prediction on Training data
y_train_pred = rf.predict(X_train)

# R squared Error
error_score = metrics.r2_score(y_train, y_train_pred)
print("R squared Error : ", error_score)

plt.scatter(y_train, y_train_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

# prediction on Training data
y_test_pred = rf.predict(X_test)

# R squared Error
error_score = metrics.r2_score(y_test, y_test_pred)
print("R squared Error : ", error_score)

plt.scatter(y_test, y_test_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

"""## Cross-validation"""

from sklearn.model_selection import cross_val_score

"""### Linear Regression"""

model = LinearRegression(n_jobs = 5)
cross_val_results = cross_val_score(model, X, y, cv=5, scoring = 'r2')

print("Results for Linear Regression")
print("*******************************")
print("Cross-validation Results (r2): ", cross_val_results)
print("Mean R2: ", cross_val_results.mean())

"""### Random Forest"""

model = RandomForestRegressor(random_state = None)
cross_val_results = cross_val_score(model, X, y, cv=5, scoring = 'r2')

print("Results for Random Forest")
print("*******************************")
print("Cross-validation Results (r2): ", cross_val_results)
print("Mean R2: ", cross_val_results.mean())
