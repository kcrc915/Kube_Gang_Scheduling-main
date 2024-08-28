import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('heatmaps2.csv')

# Convert 'Total' column to numeric, coercing errors to NaN
data['Total'] = pd.to_numeric(data['Total'], errors='coerce')

# Drop rows where 'Total' is NaN
data = data.dropna(subset=['Total'])

# Filter data to only include specified Window size and Action ranges
window_order = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10']
action_order = ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']

data_filtered = data[(data['Window size'].isin(window_order)) &
                     (data['Action'].isin(action_order))]

# Sort the data by the specified order
data_filtered['Window size'] = pd.Categorical(data_filtered['Window size'], categories=window_order, ordered=True)
data_filtered['Action'] = pd.Categorical(data_filtered['Action'], categories=action_order, ordered=True)

# Create the pivot table for the heatmap
heatmap_data = data_filtered.pivot(index='Window size', columns='Action', values='Total')

# Reverse the order of the rows to have the least duration at the top
heatmap_data = heatmap_data.iloc[::-1]

# Plot the heatmap without annotations
sns.heatmap(heatmap_data, cmap='YlGnBu', cbar_kws={'label': 'Total Duration'})
plt.title('Total Duration by Action and Window Size')
plt.show()
