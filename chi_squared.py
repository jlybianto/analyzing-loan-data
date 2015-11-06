# The scipy.stats module is for a large number of probability distributions and statistical functions.
# The collections module implements specialized container data types (eg. Counter dict subclass for counting hashable objects)
# The pandas package is used to fetch and store data in a DataFrame.
import scipy.stats as stats
import collections
import pandas as pd

# Collection of data from Amazon AWS.
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Data cleaning by removing rows with null values.
loansData.dropna(inplace=True)