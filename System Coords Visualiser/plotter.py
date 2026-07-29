import pandas as pd
import plotly.express as px

# 1. Load your data (Replace with your actual file path)
# Assumes a CSV file with columns named 'x', 'y', and 'z'
df = pd.read_csv("coords.csv")

# 2. Create interactive 3D scatter plot
fig = px.scatter_3d(df, x='x', y='y', z='z', text='Owner',
                    title='MAIN FAM windows',
                    labels={'x': 'X Axis', 'y': 'Y Axis', 'z': 'Z Axis'},
                    range_x=[-2048,2047],
                    range_y=[-128,127],
                    range_z=[-2048,2047])

# 3. Adjust marker size for clarity (since you only have 135 points)
fig.update_traces(marker=dict(size=5, line=dict(width=1, color='DarkSlateGrey')))
# fig.update_xaxes(range=[-2048,2047])
# fig.update_yaxes(range=[-128,127])

# 4. Open in your web browser
fig.show()