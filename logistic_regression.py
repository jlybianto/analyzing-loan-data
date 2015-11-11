# The pandas package is used to fetch and store data in a DataFrame.
# The statsmodels is used to find the model coefficients.
import pandas as pd
import statsmodels.api as sm

# Importing data from Amazon AWS
loansData = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")

# Clean data from columns 'Interest.Rate', 'Loan.Length', 'FICO.Range' into numerical types.
# Convert interest rate from 'xx.xx%' to '0.xxxx'
# Convert length from 'xx months' to 'xx'
# Convert score from categorical 'xxx-yyy' to 'xxx'
loansData['Interest.Rate'] = [round((float(i[:-1]) / 100), 4) for i in loansData['Interest.Rate']]
loansData['Loan.Length'] = [int(month.rstrip(" months")) for month in loansData['Loan.Length']]
loansData['FICO.Range'] = [int((score.split("-"))[0]) for score in loansData['FICO.Range']]