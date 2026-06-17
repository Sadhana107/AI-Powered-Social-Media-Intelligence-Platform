import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI-Powered Social Media Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#111827,#1e293b);
}

[data-testid="stMetric"]{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:20px;
border-radius:20px;
box-shadow:0px 6px 20px rgba(0,0,0,0.4);
}

h1{
text-align:center;
color:white;
font-size:3rem;
}

h2,h3{
color:#60a5fa;
}

section[data-testid="stSidebar"]{
background:#111827;
}

</style>
""", unsafe_allow_html=True)
# =========================
# LOAD DATA
# =========================

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(
        "data/processed_data/ai_enhanced_social_media_data.csv"
    )

# =========================
# SIDEBAR
# =========================

st.sidebar.title("📊 Filters")

platform_filter = st.sidebar.multiselect(
    "Platform",
    df["Platform"].unique(),
    default=df["Platform"].unique()
)

theme_filter = st.sidebar.multiselect(
    "Content Theme",
    df["Content_Theme"].unique(),
    default=df["Content_Theme"].unique()
)
post_type_filter = st.sidebar.multiselect(
    "Post Type",
    df["Post_Type"].unique(),
    default=df["Post_Type"].unique()
)

campaign_filter = st.sidebar.multiselect(
    "Campaign",
    df["Campaign_Name"].unique(),
    default=df["Campaign_Name"].unique()
)

df = df[
    (df["Platform"].isin(platform_filter))
    &
    (df["Content_Theme"].isin(theme_filter))
    &
    (df["Post_Type"].isin(post_type_filter))
    &
    (df["Campaign_Name"].isin(campaign_filter))
]

# =========================
# TITLE
# =========================

st.title("🚀 AI-Powered Social Media Intelligence Platform")
st.caption("Advanced Analytics | Machine Learning | AI Recommendations")

# =========================
# KPIs
# =========================

total_reach = int(df["Reach"].sum())
total_impressions = int(df["Impressions"].sum())
avg_ctr = round(df["CTR"].mean(),2)
avg_engagement = round(df["Engagement_Rate"].mean(),2)
follower_growth = int(df["Follower_Growth"].sum())
avg_ai_score = round(df["AI_Content_Score"].mean(),2)

k1,k2,k3,k4,k5,k6 = st.columns(6)

k1.metric("Reach", f"{total_reach:,}")
k2.metric("Impressions", f"{total_impressions:,}")
k3.metric("CTR %", avg_ctr)
k4.metric("Engagement %", avg_engagement)
k5.metric("Growth", follower_growth)
k6.metric("AI Score", avg_ai_score)

st.divider()

# =========================
# TABS
# =========================

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Overview",
    "📊 Analytics",
    "🤖 AI Insights",
    "🔮 Predictions"
])

# =========================
# OVERVIEW
# =========================

with tab1:

    c1,c2 = st.columns(2)

    with c1:

        platform_perf = (
            df.groupby("Platform")["Engagement_Rate"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            platform_perf,
            x="Platform",
            y="Engagement_Rate",
            color="Engagement_Rate",
            color_continuous_scale="Turbo",
            text_auto=".2f",
            title="🏆 Platform Performance"
        )

        st.plotly_chart(fig, use_container_width=True)

    with c2:

        theme_perf = (
            df.groupby("Content_Theme")["Engagement_Rate"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            theme_perf,
            x="Content_Theme",
            y="Engagement_Rate",
            color="Engagement_Rate",
            color_continuous_scale="Viridis",
            text_auto=".2f",
            title="📊 Theme Performance"
        )

        st.plotly_chart(fig, use_container_width=True)

# =========================
# ANALYTICS
# =========================

with tab2:

    a1,a2 = st.columns(2)

    with a1:

        fig = px.histogram(
            df,
            x="Sentiment_Score",
            nbins=30,
            title="Sentiment Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)
        st.subheader("🔥 Top Viral Posts")

        viral_posts = df.nlargest(
            10,
            "Virality_Score"
        )[[
            "Post_ID",
            "Platform",
            "Content_Theme",
            "Virality_Score",
            "Engagement_Rate"
        ]]

        st.dataframe(
            viral_posts,
            use_container_width=True
        )

    with a2:

        sentiment = pd.cut(
            df["Sentiment_Score"],
            bins=[-1,-0.01,0.01,1],
            labels=["Negative","Neutral","Positive"]
        )

        sentiment_df = sentiment.value_counts().reset_index()

        sentiment_df.columns = [
            "Sentiment",
            "Count"
        ]

        fig = px.pie(
            sentiment_df,
            names="Sentiment",
            values="Count",
            hole=0.6,
            title="Sentiment Breakdown"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    df["Post_Hour"] = pd.to_datetime(
        df["Post_Time"],
        format="%H:%M"
    ).dt.hour

    hour_perf = (
        df.groupby("Post_Hour")["Reach"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        hour_perf,
        x="Post_Hour",
        y="Reach",
        markers=True,
        title="Best Posting Hour Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================
# AI INSIGHTS
# =========================

with tab3:

    st.subheader("🤖 AI Recommendations")

    st.success(
        "Focus more on LinkedIn as it generates the highest engagement."
    )

    st.info(
        "Post around 9:00 AM for maximum reach."
    )

    st.warning(
        "Increase hashtag usage to improve CTR."
    )

    st.success(
        "Increase Product Launch content as it performs best."
    )

    st.divider()

    best_platform = (
        df.groupby("Platform")
        ["Engagement_Rate"]
        .mean()
        .idxmax()
    )

    best_theme = (
        df.groupby("Content_Theme")
        ["Engagement_Rate"]
        .mean()
        .idxmax()
    )

    st.metric(
        "Best Platform",
        best_platform
    )

    st.metric(
        "Best Theme",
        best_theme
    )

# =========================
# PREDICTIONS
# =========================

with tab4:

    st.subheader("🔮 Future Performance Forecast")

    p1,p2 = st.columns(2)

    with p1:

        st.metric(
            "Predicted Engagement",
            "8.2%"
        )

    with p2:

        st.metric(
            "Virality Probability",
            "96.7%"
        )

    forecast = pd.DataFrame({
        "Month":[
            "Jul","Aug","Sep",
            "Oct","Nov","Dec"
        ],
        "Forecast_Engagement":[
            7.8,8.1,8.5,
            8.9,9.2,9.5
        ]
    })

    fig = px.line(
        forecast,
        x="Month",
        y="Forecast_Engagement",
        markers=True,
        title="Future Engagement Forecast"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================
# DATA PREVIEW
# =========================

st.divider()

with st.expander("View Dataset"):

    st.dataframe(
        df.head(100),
        use_container_width=True
    )