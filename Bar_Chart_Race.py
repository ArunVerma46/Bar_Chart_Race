import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Sample data (replace with your own)
data = {
    'Country': ['USA', 'China', 'India', 'Brazil', 'Germany'],
    '2010': [300, 200, 150, 100, 80],
    '2011': [305, 210, 160, 105, 82],
    '2012': [310, 225, 170, 110, 85],
    '2013': [315, 240, 180, 115, 88],
    '2014': [320, 250, 195, 120, 90]
}
df = pd.DataFrame(data).set_index('Country')

fig, ax = plt.subplots(figsize=(10, 6))

def draw_barchart(year):
    ax.clear()
    d = df[year].sort_values(ascending=True)
    ax.barh(d.index, d.values, color=[random.choice(['#6a0589', '#f2510f', '#0f72f2', '#12b500']) for _ in d])
    ax.set_title(f'Bar Chart Race - Year {year}', fontsize=20)
    ax.set_xlabel('Value')
    ax.set_ylabel('Country')
    ax.tick_params(labelsize=12)
    plt.tight_layout()

ani = animation.FuncAnimation(
    fig, draw_barchart, frames=df.columns, interval=1000)

plt.show()
