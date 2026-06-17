import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed_data/cleaned_social_media_data.csv")

# Feature Engineering
df["CTR"] = (df["Link_Clicks"] / df["Impressions"]) * 100

df["Total_Engagement"] = (
    df["Likes"] +
    df["Comments"] +
    df["Shares"] +
    df["Saves"]
)

df["Engagement_Rate"] = (
    df["Total_Engagement"] / df["Reach"]
) * 100

df["Virality_Score"] = (
    df["Shares"] / df["Reach"]
) * 100

df["Follower_Growth"] = (
    df["Followers_After"] -
    df["Followers_Before"]
)

# Save dataset
df.to_csv(
    "data/processed_data/featured_social_media_data.csv",
    index=False
)

print("Feature Engineering Completed Successfully!")
print(df[[
    "CTR",
    "Total_Engagement",
    "Engagement_Rate",
    "Virality_Score",
    "Follower_Growth"
]].head())