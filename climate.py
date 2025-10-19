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

# Display the shape, dtype, overall mean

# Average temp per city - axis=0 for mean along rows

# Average temp per month - axis=1 for mean along columns

# Hottest and coldest temperature for each city - maximum and minimum along each column (axis=0)

# Temperature range for each city - subtract min temp from max temp (elementwise operations)

# Single hottest and single coldest temperature throughout all cities and their indexes

# Hottest and coldest month overall - using average monthly temp array
