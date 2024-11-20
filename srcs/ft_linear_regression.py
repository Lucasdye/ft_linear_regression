import plotting as plot
import pandas as pd
import numpy as np
import random

def mean_squared_error_custom(y_true, y_pred):
    return np.mean((np.array(y_true) - np.array(y_pred)) ** 2)

def main():
	#---------- Dataset --------------#
	path = "../data/data.csv"
	f = open(path, "r")
	cols_name = f.readline()
	cols_name = cols_name.split(",")
	cols_name = [el.strip() for el in cols_name]
	fig1, ax1 = plot.plt.subplots()
	df = pd.read_csv(path, usecols=cols_name)
	plot.plot(df[cols_name[0]], df[cols_name[1]], cols_name[0], cols_name[1], ax1, "scatter")
	# plot.plt.show()

	#---------- Model ----------------#
	targets = df[cols_name[1]]
	x = df[cols_name[0]]

	a = random.random()
	b = random.random()
	predictions = []

	# MSE
	predictions = a * x + b
	mse = np.mean((predictions - targets) ** 2)
	print(mse)

	
	



if __name__ == "__main__":
	main()
# %%
