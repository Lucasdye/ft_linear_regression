from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random


def mse_pure(y_true, y_pred):
    return np.mean((np.array(y_true) - np.array(y_pred)) ** 2)

def main():
	#---------- Dataset --------------#
	
	path = "../data/data.csv"
	df = pd.read_csv(path)
	print(df)
	x, y = make_regression(n_samples=100, n_features=1)
	plt.scatter(x, y, c="red")
	plt.show()


	
	



if __name__ == "__main__":
	main()
# %%
