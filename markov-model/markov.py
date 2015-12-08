# The pandas package is used to fetch and store data in a DataFrame.
import pandas as pd

# Model probabilities of transitioning financial markets.
df = pd.DataFrame(
	{
	"Bear": [0.8, 0.15, 0.05],
	"Bull": [0.075, 0.9, 0.025],	
	"Stagnant": [0.25, 0.25, 0.5]
	}, index=["Bear", "Bull", "Stagnant"])

print df