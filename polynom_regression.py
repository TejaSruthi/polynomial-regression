# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:23:52 2019

@author: vhs
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#loading the dataset
datset = pd.read_csv('Position_Salaries.csv')
x = datset.iloc[:,1:-1].values
y = datset.iloc[:,-1].values

# fittng the linear regression to dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)

#fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)

#visualizing the linear regressioon
plt.scatter(x, y, color = 'red')
plt.plot(x,lin_reg.predict(x), color= 'blue')
plt.title('Truth or bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#visualizing the Polynomial Regression
x_small_points = np.arange(min(x), max(x), 0.1)
x_small_points = x_small_points.reshape((len(x_small_points), 1))
plt.scatter(x, y ,color = 'red')
plt.plot(x_small_points, lin_reg_2.predict(poly_reg.fit_transform(x_small_points)), color = 'blue')
plt.title('Truth or bluff(Polynomial regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#predicting a new result with linear regression
lin_reg.predict(np.array([6.5]).reshape(1,1))

#predicting a new result with polynomial regression
lin_reg_2.predict(poly_reg.fit_transform(np.array([6.5]).reshape(1,1)))