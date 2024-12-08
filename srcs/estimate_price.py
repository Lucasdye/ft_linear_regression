import sys as system
import numpy as np
from params import params 
from linear_regression import linear_regression as ln
 
def waiting_for_input():
    """
    Summary:
    Blocks the program until the user enters text
    """
    str = ""
    while str == "" or str.isdigit() is False:
        str = input("Enter a mileage: ")
    return (str)


def main():
    input = waiting_for_input()
    input = int(input)

    # creating feature matrix
    x = np.array(input)
    x = np.hstack((x, np.ones(1)))

    # creating parameters matrix
    theta = np.hstack((np.array(params.theta1), np.array(params.theta0))).reshape(2, 1)
    print(theta)

    # Result
    print(ln.model(x, theta))


if __name__ == "__main__":
    main()