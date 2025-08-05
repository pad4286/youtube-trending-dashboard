import pandas as pd
from sqlalchemy import create_engine

# Connect to MySQL
engine = create_engine("mysql+mysqlconnector://tej:NewPassword123!@localhost/youtube_trending")

# Load original data
df = pd.read_sql("SELECT * FROM trending_videos", con=engine)
print(f"✅ Data Loaded: {df.shape}")

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Remove duplicate rows
initial_count = len(df)
df.drop_duplicates(inplace=True)
print(f"\nRemoved {initial_count - len(df)} duplicate rows.")

# Convert dates
df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Save to MySQL in smaller chunks
chunk_size = 20000  # smaller chunk to avoid timeouts
table_name = "trending_videos_cleaned"

# Create empty table first
df.iloc[0:0].to_sql(table_name, con=engine, if_exists='replace', index=False)

# Insert chunks
with engine.begin() as conn:
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i+chunk_size]
        chunk.to_sql(table_name, con=conn, if_exists='append', index=False)
        print(f"Inserted rows {i} to {i+len(chunk)}")

print("✅ Cleaned data uploaded to MySQL successfully!")

