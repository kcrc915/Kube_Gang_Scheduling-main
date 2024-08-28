import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV file
data = pd.read_csv('Dynamic_Window_results.csv')

# Extracting columns
window_size = data['Horizon size']
duration_without_penalty = data['Duration without Checkpoint Penalty']
total_duration = data['Total Duration']
num_checkpoints = data['Number of Checkpoints']

# Position of bars
x = np.arange(len(window_size))

# Create the figure and axes
fig, ax1 = plt.subplots(figsize=(12, 7))

# Bar width
bar_width = 0.35

# Creating bars for duration without penalty and total duration
bar1 = ax1.bar(x - bar_width / 2, duration_without_penalty, bar_width, label='Duration without Checkpoint Penalty')
bar2 = ax1.bar(x + bar_width / 2, total_duration, bar_width, label='Total Duration')

# Setting labels and title
ax1.set_xlabel('Horizon size')
ax1.set_ylabel('Duration (s)')
ax1.set_title('Duration with and without Checkpoint Penalty by Window Size')
ax1.set_xticks(x)
ax1.set_xticklabels(window_size, rotation=15)
ax1.set_ylim(40000, 60000)  # Setting the y-axis range from 40000 to 60000

# Creating a secondary y-axis for the number of checkpoints
ax2 = ax1.twinx()
ax2.set_ylabel('Number of Checkpoints')
ax2.set_ylim(0, 400)  # Setting the maximum value for the y-axis to 200
line = ax2.plot(x, num_checkpoints, 'r--', marker='o', label='Number of Checkpoints')

# Combining the labels for the legend
bars_labels = [bar1, bar2]
lines_labels = [line[0]]
all_labels = bars_labels + lines_labels
labels = [l.get_label() for l in all_labels]
ax1.legend(all_labels, labels, loc='upper left', bbox_to_anchor=(1.15, 1), ncol=1)

# Adjusting layout
fig.tight_layout()
plt.subplots_adjust(right=0.75)

# Display the plot
plt.show()
