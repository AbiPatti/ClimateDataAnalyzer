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
arr_temps_city_avg = arr_temps.mean(axis=0)
print("\nAverage temperature by city: ", np.round(arr_temps_city_avg, 1))

# Average temp per month - axis=1 for mean along columns
arr_temps_month_avg = arr_temps.mean(axis=1)
print("\nAverage temperature by month: ", np.round(arr_temps_month_avg, 1))

# Hottest and coldest temperature for each city - maximum and minimum along each column (axis=0)
arr_temps_hottest = arr_temps.max(axis=0)
arr_temps_coldest = arr_temps.min(axis=0)
print("\nHottest temperatures by city: ", arr_temps_hottest)
print("Coldest temperatures by city: ", arr_temps_coldest)

# Temperature range for each city - subtract min temp from max temp (elementwise operations)
arr_temp_range_city = arr_temps_hottest - arr_temps_coldest
print("\nTemperature range by city: ", arr_temp_range_city)

# Single hottest and single coldest temperature throughout all cities and their indexes
hottest_temp = arr_temps.max()
coldest_temp = arr_temps.min()
index_hottest_temp = np.where(arr_temps == hottest_temp)
index_coldest_temp = np.where(arr_temps== coldest_temp)
print(f"\nHottest overall temperature: {hottest_temp} at index: {index_hottest_temp}")
print(f"Coldest overall temperature: {coldest_temp} at index: {index_coldest_temp}")

# Hottest and coldest month overall - using average monthly temp array
index_hottest_month = np.argmax(arr_temps_month_avg)
index_coldest_month = np.argmin(arr_temps_month_avg)
print(f"\nHottest month: Month {index_hottest_month + 1} with temperature of {arr_temps_month_avg[index_hottest_month]}")
print(f"\nColdest month: Month {index_coldest_month + 1} with temperature of {arr_temps_month_avg[index_coldest_month]}")