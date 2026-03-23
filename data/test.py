import pandas as pd

df = pd.read_csv("data/medicines_cleaned.csv")

print(df.sample(5))