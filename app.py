import streamlit as st
from fetch_youtube import fetch_youtube_videos
from subscriber import subscription_form, display_subscriber_recommendations

st.set_page_config(page_title="Tech Tracker", layout="wide")
st.title("📡 Here is what's happening in tech")

# 🔐 Secrets
YOUTUBE_API_KEY = 'AIzaSyAwx9KHo2UVG3teA5lHngNAPURqppcVhVk'
# REDDIT_ID = st.secrets["REDDIT_ID"]
# REDDIT_SECRET = st.secrets["REDDIT_SECRET"]
# REDDIT_AGENT = "tech-tracker-agent"

tab1, tab2 = st.tabs(["🔍 Explore Topics", "📬 Subscriptions"])

with tab1:
    query = st.text_input("Search YouTube for...", value="DevOps tools 2025")
    if query:
        st.subheader("📺 Recommended YouTube Videos")
        for video in fetch_youtube_videos(query, YOUTUBE_API_KEY):
            st.markdown(f"🔗 [{video['title']}]({video['url']})  \n🧑 {video['channel']} | 🕒 {video['published']}")

# st.subheader("🧵 Reddit /r/technology")
# for post in fetch_reddit_posts(REDDIT_ID, REDDIT_SECRET, REDDIT_AGENT):
#     st.markdown(f"🔗 [{post['title']}]({post['url']}) (👍 {post['score']})")

# st.subheader("📢 Hacker News")
# for item in fetch_hackernews_stories():
#     st.markdown(f"🔗 [{item['title']}]({item['url']})")
