# The collections module implements specialized container data types (eg. Counter dict subclass for counting hashable objects)
# The numpy package is for scientific computing and container of generic data (used for generating a continuous distribution)
# The scipy.stats module is for a large number of probability distributions and statistical functions.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import collections
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Data to be analyzed.
x = [
1, 1, 1, 1, 1, 1, 1, 1, 
2, 2, 2, 3, 4, 4, 4, 4, 
5, 6, 6, 6, 7, 7, 7, 7, 
7, 7, 7, 7, 8, 8, 9, 9
]

# Calculation and output of frequency data.
c = collections.Counter(x)
count_sum = sum(c.values())
for k, v in c.iteritems():
	print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum) + "."

# Generate and save a box-plot of the data.
plt.boxplot(x)
plt.savefig("boxplot.png")

# Generate and save a histogram of the data.
plt.histogram(x, histtype='bar')
plt.savefig("histogram.png")

# Generate and save a QQ-plot of the data.
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("normalqq.png")

test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("uniformqq.png")