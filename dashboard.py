import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# ---------------------------
# 1. Load Cleaned Data from MySQL
# ---------------------------
engine = create_engine("mysql+mysqlconnector://tej:NewPassword123!@localhost/youtube_trending")
df = pd.read_sql("SELECT * FROM trending_videos_cleaned", con=engine)

# Convert trending_date to datetime if not already
df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce')

# ---------------------------
# 2. Prepare Data for Visualizations
# ---------------------------

# Top 10 Channels by Video Count
top_channels = df['channel_title'].value_counts().head(10).reset_index()
top_channels.columns = ['channel_title', 'video_count']

# Category Distribution
category_dist = df['category_id'].value_counts().reset_index()
category_dist.columns = ['category_id', 'count']

# Views Over Time
views_over_time = df.groupby('trending_date')['views'].sum().reset_index()

# ---------------------------
# 3. Create Dash App Layout
# ---------------------------
app = Dash(__name__)

app.layout = html.Div([
    html.H1("📊 YouTube Trending Videos Dashboard", style={'textAlign': 'center'}),
    html.Hr(),

    html.H2("Top 10 Channels by Trending Videos"),
    dcc.Graph(
        figure=px.bar(top_channels, x='channel_title', y='video_count', title='Top 10 Channels')
    ),

    html.H2("Distribution of Trending Categories"),
    dcc.Graph(
        figure=px.pie(category_dist, names='category_id', values='count', title='Category Distribution')
    ),

    html.H2("Total Views Over Time"),
    dcc.Graph(
        figure=px.line(views_over_time, x='trending_date', y='views', title='Total Views Over Time')
    ),

    html.H2("Interactive: Top Videos by Category"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': str(cat), 'value': cat} for cat in df['category_id'].unique()],
        value=df['category_id'].unique()[0]
    ),
    dcc.Graph(id='category-graph')
])

# ---------------------------
# 4. Callbacks for Interactivity
# ---------------------------
@app.callback(
    Output('category-graph', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_graph(selected_cat):
    filtered_df = df[df['category_id'] == selected_cat]
    top_videos = filtered_df.sort_values(by='views', ascending=False).head(10)
    fig = px.bar(
        top_videos,
        x='title',
        y='views',
        title=f'Top 10 Videos in Category {selected_cat}',
        labels={'views': 'Views', 'title': 'Video Title'}
    )
    return fig

# ---------------------------
# 5. Run the App
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
