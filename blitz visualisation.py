import pandas as pd
import matplotlib.pyplot as plt

# Load your cleaned data into a DataFrame
data = {
    'Name': ['Magnus Carlsen', 'Ian Nepomniachtchi', 'Ding Liren', 'Alireza Firouzja', 'Anish Giri'],
    'Classical': [2852.0, 2795.0, 2788.0, 2785.0, 2768.0],
    'Rapid': [2839.0, 2761.0, 2829.0, 2745.0, 2714.0],
    'Blitz': [2852.0, 2781.0, 2787.0, 2904.0, 2807.0]
}
df = pd.DataFrame(data)

# Define the colors and sizes for each type of rating
colors = {'Classical': 'blue', 'Rapid': 'green', 'Blitz': 'red'}
sizes = {'Classical': 300, 'Rapid': 150, 'Blitz': 50}

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data
for rating_type in ['Classical', 'Rapid', 'Blitz']:
    ax.scatter(df['Name'], df[rating_type], 
               color=colors[rating_type], 
               s=sizes[rating_type], 
               label=rating_type, 
               alpha=0.6, edgecolors='w', linewidth=0.5)

# Set the labels and title
ax.set_xlabel('Player Names')
ax.set_ylabel('Rating Points')
ax.set_title('Chess Player Ratings by Type')
ax.legend(title='Rating Type')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()