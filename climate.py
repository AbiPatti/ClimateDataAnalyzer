# Abinash Patti
# Creating data and showing basic info

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create a dictionary of 3 cities and each city has a dictionary containing temperatures by month
dict_temps = {

    "New York": {
        "Jan": 0, "Feb": 2, "Mar": 6, "Apr": 12, "May": 17, "Jun": 22,
        "Jul": 25, "Aug": 24, "Sep": 21, "Oct": 14, "Nov": 9, "Dec": 4
    },

    "London": {
        "Jan": 5, "Feb": 5, "Mar": 7, "Apr": 10, "May": 14, "Jun": 17,
        "Jul": 19, "Aug": 19, "Sep": 16, "Oct": 12, "Nov": 8, "Dec": 6
    },

    "Tokyo": {
        "Jan": 5, "Feb": 6, "Mar": 9, "Apr": 15, "May": 20, "Jun": 23,
        "Jul": 26, "Aug": 27, "Sep": 24, "Oct": 18, "Nov": 12, "Dec": 8
    }
}

# Convert data into a DataFrame
df_temps = pd.DataFrame(dict_temps)

# Display the DataFrame, shape, dtype, overall mean
print(df_temps)
print(df_temps.shape)
print(df_temps.dtypes)
print("\nOverall mean: ", df_temps.stack().mean().round(2))

# Save DataFrame as csv
df_temps.to_csv("temperatures.csv")

# Average temp per city - axis=0 for mean along rows
print("\nAverage temperature per city: ")
print(df_temps.mean(0))

# Average temp per month - axis=1 for mean along columns
print("\nAverage temperature per month: ")
print(df_temps.mean(1))

# Hottest and coldest temperature for each city - maximum and minimum along each column (axis=0)
print("\nHottest temperature for each city: ")
print(df_temps.max(0))
print("\nColdest temperature for each city: ")
print(df_temps.min(0))

# Temperature range for each city - subtract min temp from max temp (elementwise operations)
print("\nTemperature range for each city: ")
print(df_temps.max(0) - df_temps.min(0))

# Single hottest and single coldest temperature throughout all cities
print("\nSingle hottest temperature along all cities: ")
print(df_temps.stack().max(0))
print("\nSingle coldest temperature along all cities: ")
print(df_temps.stack().min(0))

# Hottest and coldest month overall - using average monthly temp array
print("\nHottest month overall: ")
monthly_max = df_temps.max(1)
hottest_temp = monthly_max.max()
hottest_month = df_temps.loc[monthly_max == hottest_temp]
print(hottest_month)

print("\nColdest month overall: ")
monthly_min = df_temps.min(1)
coldest_temp = monthly_min.min()
coldest_month = df_temps.loc[monthly_min == coldest_temp]
print(coldest_month)

# --- PLOTTING ---

# Create a line plot for all cities
plt.plot(df_temps.index, df_temps["New York"], label="New York")
plt.plot(df_temps.index, df_temps["London"], label="London")
plt.plot(df_temps.index, df_temps["Tokyo"], label="Tokyo")

# Add labels and title
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Average Temperatures in 3 Cities")

# Add legend to identify each line
plt.legend()

# Show the plot
plt.show()