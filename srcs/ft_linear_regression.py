import plotting as plot
import pandas as pd
import numpy as np
import random

fig_cost, ax_cost = plot.plt.subplots()

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
	# Model's parameters
	a = 0.450
	b = 100

	# Listing target and feature values
	target_price = df[cols_name[1]].tolist()
	feat_km = df[cols_name[0]].tolist()

	# Vectors
	vcPrice = np.array([target_price])
	vcPrice = vcPrice.transpose()
	print(vcPrice)
	vcX = np.array([feat_km, [1] * len(feat_km)])
	vcX = vcX.transpose()
	vcTh = np.array([[a], [b]])

	print(f"vcX shape {vcX.shape}")
	print(f"vcTh shape {vcTh.shape}")
	start_range = 0
	end_range = 0
	step_range = 0
	lst_vcCost = []
	
	for a in np.arange(start_range, end_range, step):
		vcTh[0, 0] = a
		predictions = vcX @ vcTh 
		error = predictions - vcPrice
		squared_error = error ** 2
		cost = squared_error.sum() / (2 * vcX.shape[0])
		lst_vcCost.append(cost) 
	
	vcCost = np.array([lst_vcCost])
	print(vcCost.transpose())

	# plot.plot(np.arange(0.04449, 0.04450, 0.000001), lst_vcCost, "a", "mse", ax_cost, "line")
	# plot.plt.show()
	# test = np.array([[1, 1], [0, 0]])
	# print(test)
	# print("COST")
	# cost = np.array(lst_vcCost)
	# print(cost)c
	
	


	# MSE
	# predictions = a * x + b
	# mse = np.mean((predictions - price) ** 2)
	# print(mse)

	
	



if __name__ == "__main__":
	main()
# %%
