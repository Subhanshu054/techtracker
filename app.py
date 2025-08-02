import streamlit as st
from fetch_youtube import fetch_youtube_videos
from subscriber import subscription_form, display_subscriber_recommendations

st.set_page_config(page_title="Tech Tracker", layout="wide")
st.title("📡 Here is what's happening in tech")

YOUTUBE_API_KEY = 'AIzaSyAwx9KHo2UVG3teA5lHngNAPURqppcVhVk'

tab1, tab2 = st.tabs(["🔍 Explore Topics", "📬 Subscriptions"])

with tab1:
    query = st.text_input("Search YouTube for...", value="DevOps tools 2025")
    if query:
        st.subheader("📺 Recommended YouTube Videos")
        for video in fetch_youtube_videos(query, YOUTUBE_API_KEY):
            st.markdown(f"🔗 [{video['title']}]({video['url']})  \n🧑 {video['channel']} | 🕒 {video['published']}")

with tab2:
    subscription_form()
    st.subheader("📌 Topic-wise Recommendations")
    display_subscriber_recommendations(fetch_youtube_videos, YOUTUBE_API_KEY)
