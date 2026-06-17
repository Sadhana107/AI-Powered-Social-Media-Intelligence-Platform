import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(
    "data/processed_data/ai_enhanced_social_media_data.csv"
)

# Encode categorical columns
le_platform = LabelEncoder()
le_theme = LabelEncoder()
le_type = LabelEncoder()

df["Platform"] = le_platform.fit_transform(df["Platform"])
df["Content_Theme"] = le_theme.fit_transform(df["Content_Theme"])
df["Post_Type"] = le_type.fit_transform(df["Post_Type"])

# Convert Post_Time to Hour
df["Post_Hour"] = pd.to_datetime(
    df["Post_Time"],
    format="%H:%M"
).dt.hour

# Features
X = df[
    [
        "Platform",
        "Content_Theme",
        "Post_Type",
        "Post_Hour",
        "Sentiment_Score"
    ]
]

# Target
y = df["Engagement_Rate"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

print("\nModel Performance")
print("MAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

print("\nSample Predictions")
for i in range(5):
    print(
        f"Actual: {y_test.iloc[i]:.2f}% | Predicted: {predictions[i]:.2f}%"
    )
import joblib

joblib.dump(
    model,
    "models/engagement_prediction.pkl"
)

print("Engagement model saved!")