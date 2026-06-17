import pandas as pd

df = pd.read_csv(
    "data/processed_data/ai_enhanced_social_media_data.csv"
)

recommendations = []

# Best platform
best_platform = (
    df.groupby("Platform")["Engagement_Rate"]
    .mean()
    .idxmax()
)

recommendations.append(
    f"Focus more on {best_platform} as it shows the highest engagement."
)

# Best posting hour
df["Post_Hour"] = pd.to_datetime(
    df["Post_Time"],
    format="%H:%M"
).dt.hour

best_hour = (
    df.groupby("Post_Hour")["Reach"]
    .mean()
    .idxmax()
)

recommendations.append(
    f"Post around {best_hour}:00 for maximum reach."
)

# Hashtag recommendation
avg_ctr = df["CTR"].mean()

if avg_ctr < 5:
    recommendations.append(
        "Increase hashtag usage to improve CTR."
    )

# Educational vs Promotional
theme = (
    df.groupby("Content_Theme")["Engagement_Rate"]
    .mean()
    .idxmax()
)

recommendations.append(
    f"Increase {theme} content as it performs best."
)

print("\nAI RECOMMENDATIONS\n")

for i, rec in enumerate(recommendations, start=1):
    print(f"{i}. {rec}")