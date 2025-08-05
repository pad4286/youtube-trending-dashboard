import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Connect to MySQL
engine = create_engine("mysql+mysqlconnector://tej:NewPassword123!@localhost/youtube_trending")

# Load cleaned data
df = pd.read_sql("SELECT * FROM trending_videos_cleaned", con=engine)
print("✅ Data Loaded for Analysis:", df.shape)

# 1. Top 5 most viewed videos
top_videos = df.sort_values(by='views', ascending=False).head(5)
print("\nTop 5 Most Viewed Videos:")
print(top_videos[['title', 'channel_title', 'views']])

# 2. Channels with most trending appearances
top_channels = df['channel_title'].value_counts().head(10)
print("\nTop 10 Channels by Appearances:")
print(top_channels)

# 3. Basic Visualization - Top 10 Channels
plt.figure(figsize=(10,5))
top_channels.plot(kind='bar')
plt.title("Top 10 Channels by Appearances in Trending")
plt.xlabel("Channel")
plt.ylabel("Appearances")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
