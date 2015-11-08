# The pandas package is used to fetch and store data in a DataFrame.
import pandas as pd

# Importing data from Amazon AWS
loansData = pd.read_csv("https://spark-public.s3.amazon.com/dataanalysis/loansData.csv")