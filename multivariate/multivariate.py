# The pandas package is used to fetch and store data in a DataFrame.
# The numpy package is for scientific computing and container of generic data (used for generating a continuous distribution)
# The statsmodels is used to find the model coefficients.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Import CSV file to a DataFrame
df = pd.read_csv("LoanStats3c.csv", skiprows=1, low_memory=False)

# Clean data from columns 'int_rate', 'annual_inc' into numerical types to model single variable.
df = df[["int_rate", "annual_inc", "home_ownership"]]
df.dropna(inplace=True)

df["int_rate"] = [float(i[:-1]) for i in df["int_rate"]]
df["annual_inc"] = [int(i) for i in df["annual_inc"]]

# Taking the logarithm of annual_inc due to weak correlation
df["log_annual_inc"] = [np.log10(i) for i in df["annual_inc"]]

# Generate a histogram of the Interest Rates, Annual Incomes and Home Ownership.
plt.figure()
df.hist(column="int_rate")
plt.show()

plt.figure()
df.hist(column="annual_inc")
plt.show()

# Model Interest Rate vs. Annual Income
intrate = df["int_rate"]
logannualinc = df["log_annual_inc"]

y = np.matrix(intrate).transpose()
x = np.matrix(logannualinc).transpose()
X = sm.add_constant(x)

model = sm.OLS(y, X).fit()

# Model Interest Rate vs. Annual Income and Home Ownership (without interactions)

# Model Interest Rate vs. Annual Income and Home Ownership (with interactions)