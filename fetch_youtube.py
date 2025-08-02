from googleapiclient.discovery import build
from datetime import datetime, timezone

def fetch_youtube_videos(query, api_key, max_results=10, min_views=1000):
    youtube = build("youtube", "v3", developerKey=api_key)

    # Step 1: Search videos
    search_response = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=max_results,
        order="relevance",
        type="video"
    ).execute()

    video_ids = [item["id"]["videoId"] for item in search_response["items"]]

    # Step 2: Get video statistics
    stats_response = youtube.videos().list(
        part="snippet,statistics",
        id=",".join(video_ids)
    ).execute()

    videos = []
    for item in stats_response["items"]:
        stats = item.get("statistics", {})
        snippet = item.get("snippet", {})

        try:
            views = int(stats.get("viewCount", 0))
            likes = int(stats.get("likeCount", 0))
            comments = int(stats.get("commentCount", 0))
        except ValueError:
            continue

        if views < min_views:
            continue

        # Calculate age in days
        published = snippet.get("publishedAt", "")
        published_date = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        age_days = max(1, (datetime.now(timezone.utc) - published_date).days)

        # Scoring formula: more weight to likes and comments, less to old content
        score = (views + 10 * likes + 5 * comments) / age_days

        videos.append({
            "title": snippet["title"],
            "channel": snippet["channelTitle"],
            "published": published,
            "url": f"https://youtube.com/watch?v={item['id']}",
            "views": views,
            "likes": likes,
            "comments": comments,
            "score": score
        })

    # Sort by score descending
    videos.sort(key=lambda x: x["score"], reverse=True)
    return videos
