#!/usr/bin/env python
# coding: utf-8

# Modules
# In[1]:
from linear_regression import linear_regression as ln
from params import params
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import importlib

##

print("hello")

## 

# Dataset
# In[2]:
df = ln.retrieve_dataset(params.data_path)

# In[3]:
# Isolating targets and feature into lists
feature = df[:, 0] # km 
target = df[:, 1] # price

# In[4]:
# Normalizing shapes
x = feature.reshape(feature.shape[0], 1)
y = target.reshape(target.shape[0], 1)
nx = np.zeros(len(x), dtype=float).reshape(-1, 1)


# In[5]:
# Normalizing values between 0 and 1 (prevents float underflow)
xmin = np.min(x)
xmax = np.max(x)
for i in range(len(x)):
	nx[i] = (x[i] - xmin) / (xmax - xmin)


# In[6]:
# Adding bias column to X
X = np.hstack((nx, np.ones(nx.shape)))


# In[7]:
# Creating theta vector from random values
theta = np.random.randn(2, 1)


# In[8]:
# Defining theta
res = ln.gradient_descent(X, y, theta, lr=params.lr, turns=params.turns)
predictions = ln.model(X, res["theta"])


# In[9]:
# Plotting linear regression
plt.scatter(feature, y)
plt.xlabel("Mileage (km)")
plt.ylabel("Price")
plt.plot(feature, predictions)
plt.savefig(fname=params.stats_path + "linear_regression")
plt.clf()


# In[29]:
# Plotting cost function results
plt.plot(range(1, len(res["costs"]) + 1) ,res["costs"])
plt.xlabel("turns")
plt.ylabel("cost")
plt.savefig(fname=params.stats_path + "cost_function_res")
plt.clf()


# In[ ]:

# Write down the new theta in params.py
with open("/home/lu/Coding/ft_linear_regression_git/srcs/params/params.py", "r") as f:
    content = f.read()
    if str(res['theta'][1]) not in content and str(res['theta'][0]) not in content:
        with open("/home/lu/Coding/ft_linear_regression_git/srcs/params/params.py", "a") as f:
            f.write(f"theta0 = {res['theta'][1]}\n")
            f.write(f"theta1 = {res['theta'][0]}\n")

