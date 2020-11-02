import math as m
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def abline(x, y, slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals)
    plt.show()

# plt.xticks(x, my_xticks)
# plt.yticks(np.arange(y.min(), y.max(), 0.005))
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
        return 'Seems like there\'s no information about type of data, please supply information to (population_or_sample)' \
               ' parameter'
    slope = (pearson_r_numerator / pearson_r_divisor) * (variance_y / variance_x)
    y_intercept = avg_y - (slope * avg_x)
    plt.plot(x, (slope * x) + y_intercept)


linear_regression('Age', 'Glucose level', 'sample', './data.xlsx')
# def linear_regression(x, y, xlsx_file, csv_file):
#     df = pd.read_excel('./dane.xlsx')
#
#     age_x = df['age X'].iloc[0:len(df['age X']) - 1].tolist()
#
#     glucose_level_y = df['glucose level Y'].iloc[0:len(df['glucose level Y']) - 1].tolist()
#
#     sum_age_x = sum(age_x)
#
#     sum_glucose_level_y = sum(glucose_level_y)
#
#     sum_pow_age_x = sum([i**2 for i in age_x])
#
#     # sum_pow_glucose_level_y = sum([i**2 for i in glucose_level_y])
#
#     sum_xy = sum(age_x[i] * glucose_level_y[i] for i in range(len(age_x)))
#
#     n_of_elements = len(df['subject']) - 1
#
#     a = ((sum_glucose_level_y * sum_pow_age_x) - (sum_age_x * sum_xy)) / \
#         ((n_of_elements * sum_pow_age_x) - sum_age_x ** 2)
#
#     b = ((n_of_elements * sum_xy) - (sum_age_x * sum_glucose_level_y)) / \
#         ((n_of_elements * sum_pow_age_x) - sum_age_x ** 2)
#
#     # Y = a + (b * X)
#
#     print(age_x, glucose_level_y)
#
#     plt.plot(age_x, glucose_level_y)
#     plt.xlabel('Ages(x)')
#     plt.ylabel('Glucose level(y)')
#     plt.title('Glucose level and age regression')
#     plt.show()
#
