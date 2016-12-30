import numpy as np
import matplotlib.pyplot as plt

# number of dogs
greyhounds = 500
labradors = 500

# height in inches
greyhounds_height = 28 + 4 * np.random.randn(greyhounds)
labradors_height = 24 + 4 * np.random.randn(labradors)

plt.hist([greyhounds_height, labradors_height], stacked=True, color=['r', 'b'])
plt.xlabel('height in inches')
plt.ylabel('number of dogs')
plt.show()