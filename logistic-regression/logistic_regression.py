# The pandas package is used to fetch and store data in a DataFrame.
# The statsmodels is used to find the model coefficients.
import pandas as pd
import statsmodels.api as sm

# Importing data from Amazon AWS
loansData = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")

# Clean data from columns 'Interest.Rate', 'Loan.Length', 'FICO.Range' into numerical types.
# Convert interest rate from 'xx.xx%' to 'xx.xx'
# Convert length from 'xx months' to 'xx'
# Convert score from categorical 'xxx-yyy' to 'xxx'
loansData['Interest.Rate'] = [round(float(i[:-1]), 2) for i in loansData['Interest.Rate']]
loansData['Loan.Length'] = [int(month.rstrip(" months")) for month in loansData['Loan.Length']]
loansData['FICO.Range'] = [int((score.split("-"))[0]) for score in loansData['FICO.Range']]

# Convert interest rate to boolean (T/F) figures. (0) when the rate is less than 12.00% and (1) otherwise.
loansData['Int.Rate.Bool'] = [0 if i < 12.00 else 1 for i in loansData['Interest.Rate']]

# Add a column with constant intercept of 1.0 for statsmodels compatibility.
loansData['Intercept'] = 1

# Create a list of column names of independent variables.