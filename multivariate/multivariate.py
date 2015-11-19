# The pandas package is used to fetch and store data in a DataFrame.
# The numpy package is for scientific computing and container of generic data (used for generating a continuous distribution)
# The statsmodels is used to find the model coefficients.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Import CSV file to a DataFrame
df = pd.read_csv("LoanStats3c.csv", skiprows=1)

# Clean data from columns 'int_rate', 'annual_inc' into numerical types to model single variable.

# Model Interest Rate vs. Annual Income

# Model Interest Rate vs. Annual Income and Home Ownership (without interactions)

# Model Interest Rate vs. Annual Income and Home Ownership (with interactions)