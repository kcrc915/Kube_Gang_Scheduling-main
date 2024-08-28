import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV file
data = pd.read_csv('Static_Window_results.csv')

# Extracting columns
strategy = data['Static Window']
time_before_checkpointing = data['Total time taken before checkpointing']
time_with_checkpointing = data['Total time taken after checkpointing']
num_checkpoints = data['Number of checkpoints']

# Position of bars
x = np.arange(len(strategy))

# Create the figure and axes
fig, ax1 = plt.subplots(figsize=(20, 8))

# Bar width
bar_width = 0.35

# Creating bars for time taken before and after checkpointing
bar1 = ax1.bar(x - bar_width / 2, time_before_checkpointing, bar_width, label='Total time without Checkpointing')
bar2 = ax1.bar(x + bar_width / 2, time_with_checkpointing, bar_width, label='Total time without Checkpointing')

# Setting labels and title
ax1.set_xlabel('Static Window')
ax1.set_ylabel('Time Taken (s)')
ax1.set_title('Time Taken with and without Checkpointing for Static Window Strategies')
ax1.set_xticks(x)
ax1.set_xticklabels(strategy, rotation=15)

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
