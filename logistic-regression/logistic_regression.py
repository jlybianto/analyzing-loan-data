# The pandas package is used to fetch and store data in a DataFrame.
# The statsmodels is used to find the model coefficients.
import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

# Importing data from Amazon AWS
loansData = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")

# Clean data from columns 'Interest.Rate', 'Loan.Length', 'FICO.Range' into numerical types.
# Convert interest rate from 'xx.xx%' to 'xx.xx'
loansData['Interest.Rate'] = [round(float(i[:-1]), 2) for i in loansData['Interest.Rate']]
# Convert length from 'xx months' to 'xx'
loansData['Loan.Length'] = [int(month.rstrip(" months")) for month in loansData['Loan.Length']]
# Convert range to score from by picking the lower end 'xxx-yyy' to 'xxx'
loansData['FICO.Score'] = [int((score.split("-"))[0]) for score in loansData['FICO.Range']]

# Convert interest rate to boolean (T/F) figures. (0) when the rate is less than 12.00% and (1) otherwise.
loansData['Int.Rate.Bool'] = [0 if i < 12.00 else 1 for i in loansData['Interest.Rate']]

# Add a column with constant intercept of 1.0 for statsmodels compatibility.
loansData['Intercept'] = 1

# Create a list of column names of independent variables.
ind_vars = ['FICO.Score', 'Amount.Requested', 'Intercept']

# Define the logistic regression model
logit = sm.Logit(loansData['Int.Rate.Bool'], loansData[ind_vars])

# Fit the model
f = logit.fit()
coeff = f.params

# Obtain user input independent variables FICO score and loan amount
fico = int(raw_input("Enter FICO Score: "))
loan = int(raw_input("Enter loan amount: "))

# Define a function that results a probability for the given FICO score and loan amount.
def logistic_function(fico, loan, coeff):
	p = 1 / (1 + np.exp( (fico * coeff[0]) + (loan * coeff[1]) + coeff[2] ))
	return p

# Define a function to predict the approval given then FICO score and loan amount
# Assume 70% probability is required to get the loan approved.
def predict_approval(fico, loan, coeff):
	p = logistic_function(fico, loan, coeff)
	print("Your calculated probability is: " + str(round(p, 3)))
	print("Assuming a minimum of 0.700 is required to get the loan approved.")
	if p >= 0.70:
		print("Your loan request will be approved.")
	else:
		print("Sorry, the loan request will not be approved.")

# Execute function to predict approval
predict_approval(fico, loan, coeff)

# Show figure of the generated logistic function
plt.figure()
x = np.arange(550, 950, 1)
y = 1 / (1 + np.exp( (x * coeff[0]) + (loan * coeff[1]) + coeff[2] ))
plt.plot(x, y)
plt.xlabel("FICO Score")
plt.ylabel("Probability")
plt.title("Logistic Function of Approving Loan with < 12% Interest Rate")
plt.legend(["Loan $" + str(loan)], loc="upper left")
plt.show()