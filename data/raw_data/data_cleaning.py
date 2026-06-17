import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("social_media_data_5000.csv")

# Check data
print(df.info())

# Null values
print(df.isnull().sum())

# Remove null values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Convert date
df["Post_Date"] = pd.to_datetime(df["Post_Date"])

# Standardize platform names
df["Platform"] = df["Platform"].replace({
    "insta": "Instagram",
    "IG": "Instagram",
    "instagram": "Instagram",
    "fb": "Facebook",
    "YT": "YouTube",
    "linkedin": "LinkedIn"
})

# Save cleaned file
df.to_csv("../processed_data/cleaned_social_media_data.csv", index=False)

print("Data cleaning completed successfully!")