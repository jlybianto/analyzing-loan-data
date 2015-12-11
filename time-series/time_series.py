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
issue_d_time = df["issue_d"].groupby(df.index).count()

# Generate a plot of the loans issued in each month.
plt.figure()
issue_d_time.plot()
plt.gca().grid(True)
plt.ylabel("Loan Count")
plt.title("Number of Loans Issued versus Time in Months")
plt.show()

# Generate Auto-Correlation Function (ACF) plot.
plt.figure()
sm.graphics.tsa.plot_acf(issue_d_time)
plt.ylabel("Auto-Correlation")
plt.xlabel("Lag")
plt.title("Auto-Correlation Function")
plt.show()

# Generate Partial Auto-Correlation Function (PACF) plot.
plt.figure()
sm.graphics.tsa.plot_pacf(issue_d_time)
plt.ylabel("Auto-Correlation")
plt.xlabel("Lag")
plt.title("Partial Auto-Correlation Function")
plt.show()

# ARIMA model assumes that the time-series is stationary.
# This means that the mean, variance and autocorrelation does not change overtime.
# The generated ACF / PACF plots are not stationary and a differenced series is needed.
issue_d_dif = []
for n in range(len(issue_d_time) - 1):
	dif = issue_d_time[len(issue_d_time) - 1 - n] - issue_d_time[len(issue_d_time) - 2 - n]
	issue_d_dif = [dif] + issue_d_dif

issue_d_dif = pd.Series(issue_d_dif)

# Generate a plot of the difference of loans issued in each month.
plt.figure()
issue_d_dif.plot()
plt.gca().grid(True)
plt.ylabel("Differenced Loan Count")
plt.title("Differenced Number of Loans Issued versus Time in Months")
plt.show()

# Generate Auto-Correlation Function (ACF) plot.
plt.figure()
sm.graphics.tsa.plot_acf(issue_d_dif)
plt.ylabel("Auto-Correlation")
plt.xlabel("Lag")
plt.title("Differenced Auto-Correlation Function")
plt.show()

# Generate Partial Auto-Correlation Function (PACF) plot.
plt.figure()
sm.graphics.tsa.plot_pacf(issue_d_dif)
plt.ylabel("Auto-Correlation")
plt.xlabel("Lag")
plt.title("Differenced Partial Auto-Correlation Function")
plt.show()

# Conclusion
print "There seems to be seasonality from the ACF plot."