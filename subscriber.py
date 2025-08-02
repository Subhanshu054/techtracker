# subscriber.py
import json
import os
import streamlit as st

DATA_FILE = "subscribers.json"
TOPICS = [
    "DevOps", "AI/ML", "Python", "Cloud Computing",
    "Web Development", "Web3", "Data Engineering", "Cybersecurity"
]

def save_subscription(email, selected_topics):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[email] = selected_topics

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_all_subscriptions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def subscription_form():
    with st.expander("📬 Subscribe to Tech Digest"):
        email = st.text_input("Your Email")
        selected_topics = st.multiselect("Pick your favorite topics:", TOPICS)

        if st.button("Subscribe"):
            if email and selected_topics:
                save_subscription(email, selected_topics)
                st.success("✅ You're subscribed!")
            else:
                st.error("Please enter your email and select at least one topic.")

def display_subscriber_recommendations(fetch_fn, api_key):
    subs = get_all_subscriptions()
    if not subs:
        st.info("No subscriptions yet.")
        return

    for email, topics in subs.items():
        st.markdown(f"### 📧 {email}")
        for topic in topics:
            st.markdown(f"#### 🔹 {topic}")
            results = fetch_fn(topic, api_key)
            for video in results[:3]:
                st.markdown(f"- 🔗 [{video['title']}]({video['url']})  \n  👤 {video['channel']} | 🕒 {video['published']}")
