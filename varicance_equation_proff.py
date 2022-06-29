import numpy as np
import matplotlib.pyplot as plt
import random

# Here we are reading a text which gives us list of values which represents how much water 
# 1000 people takes every day(the data is not real and was generate though random moudle in
# python)
with open('daily_water_intake.txt', 'r') as file:
    values = file.readlines()
    population = [int(value.strip()) for value in values]

# first lets convert the list to numpy array for fast and easy calculation
population_array = np.array(population)
# now lets write a function which would give us the variance
def get_variance(values, divider):
    mean = np.mean(values)
    variance = np.sum(((values - mean)**2))/divider
    return variance


# now lets calculate the population variance
population_variance = get_variance(population_array, len(population_array))
# now lets take the mean of the population
population_mean = np.mean(population)

for i in range(1000):
    sample = np.random.choice(population_array, size=20, replace=False)
    sample_mean = np.mean(sample)
    sample_variance = get_variance(sample, len(sample)-1)
    plt.scatter(sample_mean, sample_variance, color='blue', edgecolor='black')

plt.xlim((0, 10))
plt.ylim(0, 15)

plt.axhline(population_variance, color='black', ls='--')
plt.axvline(population_mean, color='black', ls='--')

plt.grid(True)
plt.show()





