# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
# The pandas package is used to fetch and store data in a DataFrame.
import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')