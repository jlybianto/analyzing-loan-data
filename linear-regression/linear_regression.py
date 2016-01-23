# ----------------
# IMPORT PACKAGES
# ----------------

# The pandas package is used to fetch and store data in a DataFrame.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import pandas as pd
import matplotlib.pyplot as plt

# ----------------
# OBTAIN DATA
# ----------------

# Importing data from Amazon AWS
loansData = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")

# ----------------
# PROFILE DATA
# ----------------

# Clean data from columns 'Interest.Rate', 'Loan.Length', 'FICO.Range' into numerical types.
# Convert interest rate from 'xx.xx%' to '0.xxxx'
# Convert length from 'xx months' to 'xx'
# Convert score from categorical 'xxx-yyy' to 'xxx'
loansData['Interest.Rate'] = [round((float(i[:-1]) / 100), 4) for i in loansData['Interest.Rate']]
loansData['Loan.Length'] = [int(month.rstrip(" months")) for month in loansData['Loan.Length']]
loansData['FICO.Range'] = [int((score.split("-"))[0]) for score in loansData['FICO.Range']]

# ----------------
# VISUALIZE DATA
# ----------------

# Generate a histogram of the FICO scores.
plt.figure()
p = loansData['FICO.Range'].hist()
plt.savefig("fico-hist.png")

# Generate a scatter-plot of the data.
plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.savefig("scatterplot-matrix.png")

# ----------------
# MODEL DATA
# ----------------

# Linear Regression Analysis
# The numpy package is for scientific computing and container of generic data (used for generating a continuous distribution)
# The statsmodels is used to find the model coefficients.
import numpy as np
import statsmodels.api as sm

# Use clean data from DataFrame to extract columns.
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']

# Extraction of a column from a DataFrame is returned as a Series data type.
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Stack columns together to create an input matrix.
x = np.column_stack([x1,x2])

# Create the linear model and summarized evaluation of data.
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print f.summary()