from matplotlib import pyplot as plt # plotting
import pandas as pd # datafram manipulation

def plt_line(x: list[int], y: list[int | float], label_x: str, label_y: str, ax: plt.Axes):
    # Plot the data on the provided axes and set labels
    ax.plot(x, y)
    ax.set_xlabel(label_x)
    ax.set_ylabel(label_y)
    ax.scatter(x, y, color="red", zorder=5)

def plt_scatter(x: list[int], y: list[int | float], label_x: str, label_y: str, ax: plt.Axes):
    # Plot the data on the provided axes and set labels
    ax.set_xlabel(label_x)
    ax.set_ylabel(label_y)
    ax.scatter(x, y, color="blue", zorder=1)

def plt_dtf(path: str, ax: plt.Axes, columns: tuple, mode: str):
    df = pd.read_csv(path, usecols=list(columns))
    if mode == "line":
        plt_line(df.columns[0]. df.columns[1], ax)
    elif mode == "scatter":
        plt_scatter(df.km, df.price, columns[0], columns[1], ax)