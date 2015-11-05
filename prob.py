# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import matplotlib.pyplot as plt

# Data to be analyzed.
x = [
1, 1, 1, 1, 1, 1, 1, 1, 
2, 2, 2, 3, 4, 4, 4, 4, 
5, 6, 6, 6, 7, 7, 7, 7, 
7, 7, 7, 7, 8, 8, 9, 9
]

# Generate and save a box-plot of the data.
plt.boxplot(x)
plt.savefig("boxplot.png")

# Generate and save a histogram of the data.
plt.histogram(x, histtype='bar')
plt.savefig("histogram.png")