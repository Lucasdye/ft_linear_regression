import plotting 


def main():
    csv_path = "/home/lu/Coding/ft_linear_regression/data.csv"
    fig1, ax1 = plotting.plt.subplots()
    plotting.plt_dtf(csv_path, ax1, ("km", "price"),  "scatter")
    plotting.plt.show()


if __name__ == "__main__":
    main()