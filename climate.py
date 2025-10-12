# Abinash Patti
# Creating data and showing basic info

import numpy as np

# Create a 12x3 array of monthly temperatures of 3 cities
# Values of temperature between -5 and 35
arr_temps = np.random.uniform(-5, 35, size=(12,3))

# Display the shape, dtype, overall mean
print("Shape: ", arr_temps.shape)
print("Dtype: ", arr_temps.dtype)
print("Overall mean: ", arr_temps.mean())

# Average temp per city - axis=0 for mean along rows
arr_temps_city_avg = np.array(arr_temps.mean(axis=0))
print("\nAverage temperature by city: ", np.round(arr_temps_city_avg, 1))

# Average temp per month - axis=1 for mean along columns
arr_temps_month_avg = np.array(arr_temps.mean(axis=1))
print("\nAverage temperature by month: ", np.round(arr_temps_month_avg, 1))