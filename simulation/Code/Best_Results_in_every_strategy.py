import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming the data is loaded into a pandas DataFrame
data = pd.DataFrame({
    'Strategy': [
        "EXXPO",
        "Static Window(3)",
        "Dynamic Window(7)",
        "Dynamic MPC(3)",
        "Reinforcement Learning(3*10)"
    ],
    'Time taken before checkpointing': [
        65126.48344,
        47880.17876,
        48107.22213,
        46631.26754,
        47133.03209
    ],
    'Time taken with checkpointing': [
        65126.48344,
        49875.17876,
        49331.26754,
        49331.26754,
        49158.03209
    ],
    'Number of Checkpoints': [0, 133, 180, 180, 135]
})

# Extracting columns
strategy = data['Strategy']
time_before_checkpointing = data['Time taken before checkpointing']
time_with_checkpointing = data['Time taken with checkpointing']
num_checkpoints = data['Number of Checkpoints']

# Position of bars
x = np.arange(len(strategy))

# Create the figure and axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.35

# Creating bars for time taken before and after checkpointing
bar1 = ax1.bar(x - bar_width / 2, time_before_checkpointing, bar_width, label='Time before Checkpointing')
bar2 = ax1.bar(x + bar_width / 2, time_with_checkpointing, bar_width, label='Time with Checkpointing')

# Setting labels and title
ax1.set_xlabel('Strategy')
ax1.set_ylabel('Time Taken (s)')
ax1.set_title('Time Taken with and without Checkpointing by Strategy')
ax1.set_xticks(x)
ax1.set_xticklabels(strategy, rotation=15)

# Creating a secondary y-axis for the number of checkpoints
ax2 = ax1.twinx()
ax2.set_ylabel('Number of Checkpoints')
ax2.set_ylim(0, 200)  # Setting the maximum value for the y-axis to 200
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
