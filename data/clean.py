import sys
sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd
import re

df = pd.read_csv("data/medicines.csv")

# Rename columns
df = df.rename(columns={
    "name": "medicine_name",
    "manufacturer_name": "company"
})

# Keep only required columns
df = df[[
    "medicine_name",
    "company",
    "short_composition1",
    "short_composition2"
]]

# Drop missing medicine names
df = df.dropna(subset=["medicine_name"])

# Fill missing values
df["company"] = df["company"].fillna("unknown")
df["short_composition1"] = df["short_composition1"].fillna("")
df["short_composition2"] = df["short_composition2"].fillna("")

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["medicine_name"] = df["medicine_name"].apply(clean_text)
df["company"] = df["company"].apply(clean_text)

# 🔥 IMPORTANT: Remove dosage for better matching
df["clean_name"] = df["medicine_name"].str.replace(r'\d+mg|\d+ml', '', regex=True)
df["clean_name"] = df["clean_name"].str.strip()

# Remove duplicates
df = df.drop_duplicates(subset=["clean_name"])

# Reset index
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("data/medicines_cleaned.csv", index=False)

print("✅ Cleaned dataset saved!")
print(df.head())
print("Total rows:", len(df))