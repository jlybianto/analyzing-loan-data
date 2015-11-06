# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
# The pandas package is used to fetch and store data in a DataFrame.
# The scipy.stats module is for a large number of probability distributions and statistical functions.
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Collection of data from Amazon AWS.
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Data cleaning by removing rows with null values.
loansData.dropna(inplace=True)

# Generate and save a box-plot of the data.
plt.figure()
loansData.boxplot(column='Amount.Requested')
plt.savefig("boxplot-amountrequested.png")

# Generate and save a histogram of the data.
plt.figure()
loansData.hist(column='Amount.Requested')
plt.savefig("hist-amountrequested.png")

# Generate and save a QQ-plot of the data.
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("qqplot-amountrequested.png")