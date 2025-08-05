YouTube is one of the largest content platforms, and trending videos can provide insights into:
Popular categories by country
View, like, and comment trends
Channel performance
Country-wise trending behavior
This project processes YouTube trending video datasets, cleans the data, and generates visual insights and dashboards

📊 Features
Clean and preprocess raw YouTube datasets
Analyze:
Most popular video categories per country
Like-to-dislike ratios (if data available)
Videos with highest engagement
Country-level trends
Generate:
Interactive dashboards
CSV/Excel reports for insights
📦 Installation & Setup
Clone the repository

bash
Copy
Edit
git clone https://github.com/<your-username>/youtube-trending-dashboard.git
cd youtube-trending-dashboard
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
(Optional) Setup Git LFS for large files

bash
Copy
Edit
git lfs install
git lfs pull
⚡ Usage
1️⃣ Data Cleaning & Analysis
Open the Jupyter Notebook:

bash
Copy
Edit
jupyter notebook notebooks/youtube_analysis.ipynb
Run the notebook to clean and analyze datasets

Generate CSV/Excel reports if needed

2️⃣ Launch Dashboard
If using Streamlit:

bash
Copy
Edit
cd dashboard
streamlit run app.py
Visit http://localhost:8501 in your browser to explore the dashboard.

📊 Example Insights
Top 5 Most Popular Video Categories in India
Average Views & Likes by Category
Most Engaging Channels by Country
Global Trending Comparisons

📜 Dataset Source
The dataset is from Kaggle - YouTube Trending Video Dataset
It contains daily records of top trending YouTube videos for multiple countries.

🚀 Technologies Used
Python (Pandas, NumPy, Matplotlib, Seaborn)
SQL (Data Queries & Aggregations)
Jupyter Notebook
Streamlit / Dash for Dashboard
Git LFS for Large Dataset Management
