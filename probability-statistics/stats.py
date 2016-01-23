# ----------------
# IMPORT PACKAGES
# ----------------

# The pandas package is used to fetch and store data in a DataFrame.
# The scipy package is used for statistical methods.
import pandas as pd
from scipy import stats

# ----------------
# OBTAIN DATA
# ----------------

# Data collected from http://lib.stat.cmu.edu/DASL/Datafiles/AlcoholandTobacco.html
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

# ----------------
# PROFILE DATA
# ----------------

# Data to be organized into a list of lists.
data = data.split("\n")
data = [i.split(",") for i in data]

# Load data into a pandas DataFrame.
column_names = data[0]
data_rows = data[1:]
df = pd.DataFrame(data_rows, columns=column_names)

# Conversion of data type so that it can be calculated.
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# ----------------
# ANALYZE DATA
# ----------------

# Analyze the data in terms of central tendency and variability.
alc_mean = round(df['Alcohol'].mean(), 2)
alc_medi = round(df['Alcohol'].median(), 2)
alc_mode = round(stats.mode(df['Alcohol'])[0][0], 2)

tob_mean = round(df['Tobacco'].mean(), 2)
tob_medi = round(df['Tobacco'].median(), 2)
tob_mode = round(stats.mode(df['Tobacco'])[0][0], 2)

alc_ran = round(max(df['Alcohol']) - min(df['Alcohol']), 2)
alc_std = round(df['Alcohol'].std(), 2)
alc_var = round(df['Alcohol'].var(), 2)

tob_ran = round(max(df['Tobacco']) - min(df['Tobacco']), 2)
tob_std = round(df['Tobacco'].std(), 2)
tob_var = round(df['Tobacco'].var(), 2)

# Print output of script.
print "Statistics of average weekly household spending on alcohol and tobacco products in British pounds across eleven regions:\n"
print "The mean for the Alcohol and Tobacco dataset is {} and {}.".format(str(alc_mean), str(tob_mean))
print "The median for the Alcohol and Tobacco dataset is {} and {}.".format(str(alc_medi), str(tob_medi))
print "The mode for the Alcohol and Tobacco dataset is {} and {}.".format(str(alc_mode), str(tob_mode))
print "The range for the Alcohol and Tobacco dataset is {} and {}.".format(str(alc_ran), str(tob_ran))
print "The variance for the Alcohol and Tobacco dataset is {} and {}.".format(str(alc_var), str(tob_var))
print "The standard deviation for the Alcohol and Tobacco dataset is {} and {}.".format(str(alc_std), str(tob_std))