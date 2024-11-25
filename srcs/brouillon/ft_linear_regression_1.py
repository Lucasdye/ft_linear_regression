import srcs.brouillon.plotting as plot
import pandas as pd
import numpy as np
import random

def mse_pure(y_true, y_pred):
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
	price = df[cols_name[1]].tolist()
	km = df[cols_name[0]].tolist()
	print(km)
	print(price)

	# a = random.random()
	# b = random.random()
	fig_cost, ax_cost = plot.plt.subplots()
	lst_mse = []
	b = 0
	arange = np.arange(0.04526, 0.04530, 0.000001)
	for a in arange:
		predictions = [float(a) * x + b for x in km]
		print(mse_pure(price, predictions))
		lst_mse.append(mse_pure(price, predictions))
	plot.plot(arange, lst_mse, "a", "mse", ax_cost, "line")
	plot.plt.show()
	# MSE
	# predictions = a * x + b
	# mse = np.mean((predictions - price) ** 2)
	# print(mse)

	
	



if __name__ == "__main__":
	main()
# %%
