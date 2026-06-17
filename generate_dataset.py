import pandas as pd
import random
from datetime import datetime, timedelta

platforms = ["Instagram", "LinkedIn", "Facebook", "YouTube"]
post_types = ["Image", "Video", "Carousel", "Reel", "Text"]
content_themes = ["Educational", "Promotional", "Industry News", "Motivational", "Product Launch"]
campaigns = ["Summer Campaign", "Brand Awareness", "Lead Generation", "Engagement Drive", "Organic"]

data = []

start_date = datetime(2024, 1, 1)

for i in range(5000):

    followers_before = random.randint(1000, 100000)

    likes = random.randint(50, 5000)
    comments = random.randint(5, 500)
    shares = random.randint(1, 300)
    saves = random.randint(1, 500)

    followers_after = followers_before + random.randint(-20, 200)

    post_date = start_date + timedelta(days=random.randint(0, 730))

    data.append({
        "Post_ID": f"P{i+1}",
        "Platform": random.choice(platforms),
        "Post_Date": post_date.strftime("%Y-%m-%d"),
        "Post_Time": f"{random.randint(0,23):02}:{random.randint(0,59):02}",
        "Post_Type": random.choice(post_types),
        "Content_Theme": random.choice(content_themes),
        "Caption": f"Sample social media post caption {i+1}",
        "Hashtags": "#marketing #socialmedia #AI",
        "Impressions": random.randint(1000, 100000),
        "Reach": random.randint(500, 80000),
        "Likes": likes,
        "Comments": comments,
        "Shares": shares,
        "Saves": saves,
        "Profile_Visits": random.randint(10, 2000),
        "Link_Clicks": random.randint(0, 1000),
        "Followers_Before": followers_before,
        "Followers_After": followers_after,
        "Campaign_Name": random.choice(campaigns)
    })

df = pd.DataFrame(data)

df.to_csv("social_media_data_5000.csv", index=False)

print("Dataset with 5000 rows created successfully!")
print(df.head())