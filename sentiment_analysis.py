import pandas as pd
import re
from textblob import TextBlob

# Load dataset
df = pd.read_csv("data/processed_data/featured_social_media_data.csv")

# -----------------------------
# Sentiment Analysis
# -----------------------------
def sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

df["Sentiment_Score"] = df["Caption"].apply(sentiment)

# -----------------------------
# AI Content Quality Score
# -----------------------------
def content_score(row):

    score = 0

    # Sentiment (25)
    if row["Sentiment_Score"] > 0:
        score += 25

    # CTA Present (25)
    cta_words = [
        "click",
        "learn",
        "join",
        "register",
        "buy",
        "enroll",
        "download",
        "try now"
    ]

    if any(word in str(row["Caption"]).lower() for word in cta_words):
        score += 25

    # Hashtags (20)
    hashtag_count = str(row["Hashtags"]).count("#")

    if hashtag_count >= 3:
        score += 20

    # Caption Length (15)
    if len(str(row["Caption"])) > 50:
        score += 15

    # Emoji Usage (15)
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF]+",
        flags=re.UNICODE
    )

    if emoji_pattern.search(str(row["Caption"])):
        score += 15

    return score

df["AI_Content_Score"] = df.apply(content_score, axis=1)

# -----------------------------
# Content Classification
# -----------------------------
def classify_content(text):

    text = str(text).lower()

    if any(word in text for word in ["tip", "tips", "guide", "tutorial", "learn"]):
        return "Educational"

    elif any(word in text for word in ["offer", "sale", "discount", "buy", "register"]):
        return "Promotional"

    elif any(word in text for word in ["motivation", "success", "inspire", "dream"]):
        return "Motivational"

    elif any(word in text for word in ["news", "update", "trend", "industry"]):
        return "Industry News"

    else:
        return "Customer Story"

df["Predicted_Content_Type"] = df["Caption"].apply(classify_content)

# Save output
df.to_csv(
    "data/processed_data/ai_enhanced_social_media_data.csv",
    index=False
)

print("AI Feature Engineering Completed Successfully!")
print(df[[
    "Sentiment_Score",
    "AI_Content_Score",
    "Predicted_Content_Type"
]].head())