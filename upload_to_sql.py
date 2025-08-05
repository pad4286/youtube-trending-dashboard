import pandas as pd
from sqlalchemy import create_engine

# MySQL credentials
username = "tej"
password = "NewPassword123!"  # your MySQL password
host = "localhost"
database = "youtube_trending"

# Step 1: Create SQLAlchemy connection
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# Step 2: Read CSV
df = pd.read_csv("US_youtube_trending_data.csv")  # CSV must be in this folder

# Step 3: Upload to MySQL
df.to_sql("trending_videos", engine, if_exists="replace", index=False)

print("✅ Data uploaded successfully to youtube_trending.trending_videos!")
