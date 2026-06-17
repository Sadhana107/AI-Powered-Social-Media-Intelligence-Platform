import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(
    "data/processed_data/ai_enhanced_social_media_data.csv"
)

# Viral Target
df["Viral"] = (
    df["Virality_Score"] > 5
).astype(int)

# Encode
le_platform = LabelEncoder()
le_theme = LabelEncoder()
le_type = LabelEncoder()

df["Platform"] = le_platform.fit_transform(df["Platform"])
df["Content_Theme"] = le_theme.fit_transform(df["Content_Theme"])
df["Post_Type"] = le_type.fit_transform(df["Post_Type"])

df["Post_Hour"] = pd.to_datetime(
    df["Post_Time"],
    format="%H:%M"
).dt.hour

X = df[
    [
        "Platform",
        "Content_Theme",
        "Post_Type",
        "Post_Hour",
        "Sentiment_Score"
    ]
]

y = df["Viral"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(
    "Accuracy:",
    accuracy_score(y_test, predictions)
)
import joblib

joblib.dump(
    model,
    "models/virality_prediction.pkl"
)

print("Virality model saved!")