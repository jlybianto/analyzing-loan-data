# The pandas package is used to fetch and store data in a DataFrame.
# The numpy package is for scientific computing and container of generic data (used for generating a continuous distribution)
# The statsmodels is used to find the model coefficients.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Import CSV file to a DataFrame
df = pd.read_csv("LoanStats3b.csv", skiprows=1, low_memory=False)

# Clean data by dropping empty entities, setting monthly period as index and grouping by month.
df = df.dropna(subset=["issue_d"])
index = pd.PeriodIndex(df.issue_d, freq="M") # M for Month
df = df.set_index(index)
issue_d_timeseries = df["issue_d"].groupby(df.index).count()

# Generate a plot of the loans issued in each month.
plt.figure()
issue_d_timeseries.plot()
plt.gca().grid(True)
plt.ylabel("Loan Count")
plt.title("Number of Loans Issued versus Time in Months")
plt.show()

# Generate Auto-Correlation Function (ACF) plot.
plt.figure()
sm.graphics.tsa.plot_acf(issue_d_timeseries)
plt.ylabel("Auto-Correlation")
plt.xlabel("Lag")
plt.title("Auto-Correlation Function")
plt.show()

# Generate Partial Auto-Correlation Function (PACF) plot.
plt.figure()
sm.graphics.tsa.plot_pacf(issue_d_timeseries)
plt.ylabel("Auto-Correlation")
plt.xlabel("Lag")
plt.title("Partial Auto-Correlation Function")
plt.show()

# Conclusion
print "There seems to be seasonality from the ACF plot."