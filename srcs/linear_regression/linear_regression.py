import pandas as pd
import numpy as np

def model(x, theta):
	return x.dot(theta)

def cost(x, y, theta):
	m = len(y)
	return (np.sum((model(x, theta) - y) ** 2)) / (2 * m)

def gradient(x, y, theta):
	m = len(y)
	return 1/m * x.T.dot(model(x, theta) - y)
	# return x.T.dot((model(x, theta) - y)) / (1 / m)

def gradient_descent(x, y, theta, lr, turns):
	for i in range(0, turns):
		theta = theta - lr * gradient(x, y, theta)
		print()
	return theta

def retrieve_dataset(path):
	# Retrieving dataset and converting to numpy array
	# path = "../data/data.csv"
	df = pd.read_csv(path)
	df = df.to_numpy()
	return df