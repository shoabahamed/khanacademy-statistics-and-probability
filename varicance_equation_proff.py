import numpy as np
import matplotlib.pyplot as plt
import random
# Here we are reading a text which gives us list of values which represents age 
# 5000 people (the data is not real and was generate though random moudle in
# python)

with open('daily_water_intake.txt', 'r') as file:
    values = file.readlines()
    population = [int(value.strip()) for value in values]

# first lets convert the list to numpy array for fast and easy calculation
population_array = np.array(population)
# population_array = np.array(population)
# now lets write a function which would give us the variance
def get_variance(values, divider):
    mean = np.mean(values)
    variance = np.sum(((values - mean)**2))/divider
    return variance


# now lets calculate the population variance
population_variance = get_variance(population_array, len(population_array))
# now lets take the mean of the population
population_mean = np.mean(population)

for i in range(20, 500):
    # size = random.randint(50, 500)
    size = 20
    sample = np.random.choice(population_array, size=i, replace=False)
    sample_mean = np.mean(sample)
    sample_variance = get_variance(sample, len(sample))
    size += 1

    if i > 200:
        color = 'blue'
    else: 
        color = 'red'

    plt.scatter(sample_mean, sample_variance, color=color, edgecolor='black')


plt.xlim((15, 80))
plt.ylim(200, 500)

plt.axhline(population_variance, color='black', ls='--')
plt.axvline(population_mean, color='black', ls='--')

plt.grid(True)
plt.show()





