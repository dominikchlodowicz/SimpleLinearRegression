import math as m
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# def abline(x, y, slope, intercept):
#     """Plot a line from slope and intercept"""
#     axes = plt.gca()
#     x_vals = np.array(axes.get_xlim())
#     y_vals = intercept + slope * x_vals
#     plt.plot(x_vals, y_vals)
#     plt.show()

def regression(domain, slope, y_intercept):
    return (slope * domain) + y_intercept

def linear_regression(X, Y, x_max,population_or_sample='population',  xlsx_file=''):
    df = pd.read_excel(xlsx_file)
    x = df[X].iloc[0:len(df[X])].tolist()
    y = df[Y].iloc[0:len(df[Y])].tolist()
    avg_x = sum(x)/len(x)
    avg_y = sum(y)/len(y)
    pearson_r_numerator = sum([(x[i] - avg_x) * (y[i] - avg_y) for i in range(len(x))])
    pearson_r_divisor = m.sqrt(sum([(x[i] - avg_x) ** 2 for i in range(len(x))]) * sum([(y[i] - avg_y) ** 2 for i in range(len(y))]))

    if population_or_sample == 'population':
        variance_x = m.sqrt(sum([(x[i] - avg_x) ** 2 for i in range(len(x))]) / len(x))
        variance_y = m.sqrt(sum([(y[i] - avg_y) ** 2 for i in range(len(y))]) / len(y))
    elif population_or_sample == 'sample':
        variance_x = m.sqrt(sum([(x[i] - avg_x) ** 2 for i in range(len(x))]) / len(x) - 1)
        variance_y = m.sqrt(sum([(y[i] - avg_y) ** 2 for i in range(len(y))]) / len(y) - 1)
    else:
        return 'Seems like there\'s no information about type of data, please supply information to ' \
               '(population_or_sample) parameter'

    slope = (pearson_r_numerator / pearson_r_divisor) * (variance_y / variance_x)
    y_intercept = avg_y - (slope * avg_x)
    domain = np.array([min(x), x_max])
    plt.plot(x, y, "o")
    plt.plot(domain, regression(domain, slope, y_intercept))
    plt.show()



linear_regression('Age', 'Glucose level', 100, 'sample', './data.xlsx')

