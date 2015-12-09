# The pandas package is used to fetch and store data in a DataFrame.
import pandas as pd

# Model probabilities of transitioning financial markets.
df = pd.DataFrame(
	{
	"Bear": [0.8, 0.075, 0.25],
	"Bull": [0.15, 0.9, 0.25],	
	"Stagnant": [0.05, 0.025, 0.5]
	}, index=["Bear", "Bull", "Stagnant"])

print df

# Need to convert DataFrame to an array or matrix
# Create a function that will take user input of desired iteration of transition