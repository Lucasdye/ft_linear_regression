from matplotlib import pyplot as plt
import pandas as pd

def plot(x: list[int | float], y: list[int | float], label_x: str, label_y: str, ax: plt.Axes, mode: str):
	# Plot the data on the provided axes and set labels
	ax.set_xlabel(label_x)
	ax.set_ylabel(label_y)
	if (mode == "scatter"):
		ax.scatter(x, y, color="red", s=10, zorder=5)
	elif (mode == "line"):
		ax.plot(x, y)
		ax.scatter(x, y, color="red", s=10, zorder=5)


 
