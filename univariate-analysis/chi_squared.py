# The scipy.stats module is for a large number of probability distributions and statistical functions.
# The collections module implements specialized container data types (eg. Counter dict subclass for counting hashable objects)
# The pandas package is used to fetch and store data in a DataFrame.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import scipy.stats as stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

# Collection of data from Amazon AWS.
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Data cleaning by removing rows with null values.
loansData.dropna(inplace=True)

# Calculation and analyses of data.
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# Generate and show a bar graph of the data.
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

# Perform a Chi-Squared test to validate distribution of data.
chi, p = stats.chisquare(freq.values())

# Print output of script.
print "There are " + str(len(freq)) + " unique number of open credit lines in the data."
print "The highest number of open credit lines in the data is " + str(int(max(freq))) + "."
print "The most frequent number of open credit lines is " + str(int(max(freq, key=freq.get))) + "."
print "The chi-squared value is " + str("%.3f" % chi) + " and the p-value is " + str("%.3f" % p) + "."

if p < 0.05:
	print "Because the p-value is less than 0.05, the null hypothesis is rejected."
else:
	print "Because the p-value is greater than 0.05, the null hypothesis failed to be rejected."