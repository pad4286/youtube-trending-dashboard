import pandas as pd
import glob

# Step 1: Get all CSV file paths
files = glob.glob("C:/Users/Tejal/Downloads/youtube_data/*.csv")  # Change path if needed

all_dfs = []

for file in files:
    try:
        df = pd.read_csv(file, encoding='utf-8')  # First try utf-8
    except UnicodeDecodeError:
        df = pd.read_csv(file, encoding='latin1')  # Fallback if utf-8 fails
    all_dfs.append(df)

# Step 2: Combine all CSV files into one DataFrame
combined_df = pd.concat(all_dfs, ignore_index=True)

# Step 3: Save the combined data
combined_df.to_csv("C:/Users/Tejal/Downloads/youtube_data/combined_youtube_trending.csv", index=False, encoding='utf-8')

print("✅ Combined CSV saved successfully!")
