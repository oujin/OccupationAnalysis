import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


salaries = []
max_level = 0
with open('data/salaries.txt', 'r', encoding='utf-8') as f:
    # e.g. "1k-2k 100"
    line = f.readline()
    while line:
        items = line.split()
        interval = items[0].replace('k', '').replace('K', '').split('-')
        begin, end = int(interval[0]), int(interval[1])
        for i in range(begin, end):
            salaries += [i] * int(items[1])
            max_level = max(max_level, end)
        line = f.readline()

_, bins, _ = plt.hist(salaries,
                      bins=max_level,
                      density=True,
                      facecolor="blue",
                      edgecolor="black",
                      alpha=0.3)
mu = np.mean(salaries)
sigma = np.std(salaries)
y = norm.pdf(bins, mu, sigma)
# print(mu-sigma, sigma, mu, mu+sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('salaries(k)')
plt.title('hist about salaries')
plt.show()
