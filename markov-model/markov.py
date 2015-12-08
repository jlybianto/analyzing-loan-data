# The pandas package is used to fetch and store data in a DataFrame.
import pandas as pd

# Model probabilities of transitioning financial markets.
df = pd.DataFrame(
	{
	"Bull": [0.9, 0.075, 0.025],
	"Bear": [0.15, 0.8, 0.05],
	"Stagnant": [0.25, 0.25, 0.5]
	}, index=["Bull", "Bear", "Stagnant"])

print df