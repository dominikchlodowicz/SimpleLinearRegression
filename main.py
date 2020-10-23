import pandas as pd

df = pd.read_excel('./dane.xlsx')

age_x = df['age X'].iloc[0:len(df['age X']) - 1].tolist()

glucose_level_y = df['glucose level Y'].iloc[0:len(df['glucose level Y']) - 1].tolist()

sum_age_x = sum(age_x)

sum_glucose_level_y = sum(glucose_level_y)

sum_pow_age_x = sum([i**2 for i in age_x])

sum_pow_glucose_level_y = sum([i**2 for i in glucose_level_y])

sum_xy = sum(age_x[i] * glucose_level_y[i] for i in range(len(age_x)))

n_of_elements = len(df['subject']) - 1

a = ((sum_glucose_level_y * sum_pow_age_x) - (sum_age_x * sum_xy)) / \
    ((n_of_elements * sum_pow_age_x) - sum_age_x ** 2)
b = ((n_of_elements * sum_xy) - (sum_age_x * sum_glucose_level_y)) / \
    ((n_of_elements * sum_pow_age_x) - sum_age_x ** 2)

X = 26

Y = a + (b * X)

print(Y)