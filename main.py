import math as m
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def data_handling(xlsx_file, X, Y, x_max):
    df = pd.read_excel(xlsx_file)
    x = df[X].iloc[0:len(df[X])].tolist()
    y = df[Y].iloc[0:len(df[Y])].tolist()
    domain = np.array([min(x), x_max]) if x_max != 0 else np.array([min(x), max(x)])
    return x, y, domain


def linear_regression(data, population_or_sample):
    x = data[0]
    y = data[1]
    avg_x = sum(x)/len(x)
    avg_y = sum(y)/len(y)
    pearson_r_numerator = sum([(x[i] - avg_x) * (y[i] - avg_y) for i in range(len(x))])
    pearson_r_divisor = m.sqrt(sum([(x[i] - avg_x) ** 2 for i in range(len(x))])
                               * sum([(y[i] - avg_y) ** 2 for i in range(len(y))]))
    if population_or_sample == 'population':
        variance_x = m.sqrt(sum([(x[i] - avg_x) ** 2 for i in range(len(x))]) / len(x))
        variance_y = m.sqrt(sum([(y[i] - avg_y) ** 2 for i in range(len(y))]) / len(y))
    else:
        variance_x = m.sqrt(sum([(x[i] - avg_x) ** 2 for i in range(len(x))]) / len(x) - 1)
        variance_y = m.sqrt(sum([(y[i] - avg_y) ** 2 for i in range(len(y))]) / len(y) - 1)
    slope = (pearson_r_numerator / pearson_r_divisor) * (variance_y / variance_x)
    y_intercept = avg_y - (slope * avg_x)
    return slope, y_intercept


def regression(domain, slope, y_intercept):
    return (slope * domain) + y_intercept


def plot_handling(data, model, x_label, y_label, title):
    plt.plot(data[0], data[1], "o")
    plt.plot(data[2], regression(data[2], model[0], model[1]))
    plt.grid(True)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def main(xlsx_file, X, Y, x_max, population_or_sample, title):
    data = data_handling(xlsx_file, X, Y, x_max)
    plot_handling(data, linear_regression(data, population_or_sample), X, Y, title)


main('./data.xlsx', 'Age', 'Glucose level', 100, 'population', 'Glucose level compared to age of patient')