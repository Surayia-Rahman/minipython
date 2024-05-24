#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor


# In[18]:


# generate synthetic data for regression
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis = 0)
y = np.sin(X).ravel()
y += 0.1 * (0.5 - np.random.rand(80))


# create an NLP regressor model
mlp_regressor = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=1)

#train the model
mlp_regressor.fit(X,y)

#generate predictions on new data points
x_new = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_pred = mlp_regressor.predict(x_new)

#plot the training data and regression predictions
plt.scatter(X, y, color='black', label='Training data')
plt.plot(x_new, y_pred, color='red', label ='MLP Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('MLP Regression')
plt.show()


# In[ ]:




