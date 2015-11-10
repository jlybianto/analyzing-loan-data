# The pandas package is used to fetch and store data in a DataFrame.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import pandas as pd
import matplotlib.pyplot as plt


# Importing data from Amazon AWS
loansData = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")

# Clean data from columns 'Interest.Rate', 'Loan.Length', 'FICO.Range' into numerical types.
# Convert interest rate from 'xx.xx%' to '0.xxxx'
# Convert length from 'xx months' to 'xx'
# Convert score from categorical 'xxx-yyy' to 'xxx'
loansData['Interest.Rate'] = [round((float(i[:-1]) / 100), 4) for i in loansData['Interest.Rate']]
loansData['Loan.Length'] = [int(month.rstrip(" months")) for month in loansData['Loan.Length']]
loansData['FICO.Range'] = [int((score.split("-"))[0]) for score in loansData['FICO.Range']]

# Generate a histogram of the FICO scores.
plt.figure()
p = loansData['FICO.Range'].hist()
plt.show()

# Generate a scatter-plot of the data.
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))