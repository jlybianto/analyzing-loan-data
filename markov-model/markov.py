# The pandas package is used to fetch and store data in a DataFrame.
# The numpy package is for scientific computing and container of generic data (used for generating a continuous distribution).
import pandas as pd
import numpy as np

# Model probabilities of transitioning financial markets.
df = pd.DataFrame(
	{
	"Bear": [0.8, 0.075, 0.25],
	"Bull": [0.15, 0.9, 0.25],	
	"Stagnant": [0.05, 0.025, 0.5]
	}, index=["Bear", "Bull", "Stagnant"])

print ""
print "Initial state of financial markets Markov model:"
print ""
print df
print ""

# Convert DataFrame to an array or matrix for computations.
m = np.mat(df)

# Create a function that will take user input of desired iteration of transition.
count = int(raw_input("Insert number of transitions: "))
if count == 0:
	print "No transitions"
else:
	m = m ** (int(count) + 1)
	m = pd.DataFrame(m, index=["Bear", "Bull", "Stagnant"], columns=["Bear", "Bull", "Stagnant"])
	print ""
	print "State of financial markets Markov model after " + str(count) + " transitions:"
	print ""
	print m