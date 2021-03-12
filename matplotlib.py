# Problem 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 2 * np.pi / max(times)))
Max = [39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25]
Min = [21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18]
months = list(range(0,12))
res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      Max, [20, 10, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      Min, [-40, 20, 0])
days = np.linspace(0, 12, num=365)
plt.plot(months, Max, 'ro', months, Min, 'bo', days, yearly_temps(days, *res_min), 'b-', days, yearly_temps(days, *res_max), 'r-')

# Problem 2
url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
from collections import Counter
dict(Counter(titanic['sex']))
plt.pie(dict(Counter(titanic['sex'])).values(),labels = dict(Counter(titanic['sex'])).keys())

# Problem 3
plt.scatter(titanic['age'], titanic['fare'])