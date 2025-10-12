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