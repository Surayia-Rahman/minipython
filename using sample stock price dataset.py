#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# In[8]:


# load a sample stock price dataset (replace with your own dataset)
# Here, we generate a synthetic dataset for demonstration
np.random.seed(0)
months = np.arange(1, 101)
amount = 100 + 2 * months + np.random.normal(0, 5, 100)
data = pd.DataFrame({'Months': months, 'Amount': amount})

#split the data into features (X) and target (y)
X = data[['Months']]
y = data['Amount']

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# create an MLP regressor model
mlp_regressor = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=1)

#train the model
mlp_regressor.fit(X_train, y_train)

# generate predictions on the test set
y_pred = mlp_regressor.predict(X_test)

# calculate and print the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:2f}')

# plot the actual and predicted stock prices
plt.scatter(X_test, y_test, color='black', label='Actual Prices')
plt.plot(X_test, y_pred, color='red', label='Predicted Prices')
plt.xlabel('Months')
plt.ylabel('Amount')
plt.legend()
plt.title('Stock price prediction')
plt.show()



# In[ ]:





# In[ ]:




