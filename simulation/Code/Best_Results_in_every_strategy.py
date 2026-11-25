import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming the data is loaded into a pandas DataFrame
data = pd.DataFrame({
    'Strategy': [
        "EXXPO",
        "Static Window",
        "Dynamic Window",
        "Dynamic MPC",
        "Reinforcement Learning"
    ],
    'Time taken before checkpointing': [
        65126.48344,
        47880.17876,
        46981.57966,
        46631.26754,
        47133.03209
    ],
    'Time taken with checkpointing': [
        0,
        49875.17876,
        50011.57966,
        49331.26754,
        49158.03209
    ],
    'Number of Checkpoints': [0, 133, 202, 180, 135]
})

# Extracting columns
strategy = data['Strategy']
time_before_checkpointing = data['Time taken before checkpointing']
time_with_checkpointing = data['Time taken with checkpointing']
num_checkpoints = data['Number of Checkpoints']

# Exclude EXXPO from the checkpoint count
strategy_for_checkpoints = strategy[1:]  # Excluding "EXXPO"
num_checkpoints_for_plot = num_checkpoints[1:]  # Excluding checkpoint count for "EXXPO"

# Position of bars
x = np.arange(len(strategy))

# Create the figure and axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar width
bar_width = 0.35

# Creating bars for time taken before and after checkpointing
bar1 = ax1.bar(x - bar_width / 2, time_before_checkpointing, bar_width, label='Duration without Checkpointing')
bar2 = ax1.bar(x + bar_width / 2, time_with_checkpointing, bar_width, label='Duration with Checkpointing')

# Setting labels and title with increased font size
ax1.set_ylabel('Duration (s)', fontsize=18)
ax1.set_xticks(x)
ax1.set_xticklabels(strategy, rotation=35, ha='right', fontsize=18)  # Modified alignment
ax1.set_ylim(40000, 66000)

# Creating a secondary y-axis for the number of checkpoints
ax2 = ax1.twinx()
ax2.set_ylabel('Number of Checkpoints', fontsize=18)
ax2.set_ylim(100, 400)

# Position of the x-values for the line plot (starting after EXXPO)
x_for_checkpoints = np.arange(1, len(strategy))  # Start from the second strategy

# Plot the line graph for number of checkpoints
line = ax2.plot(x_for_checkpoints, num_checkpoints_for_plot, 'r--', marker='o', label='Number of Checkpoints')

# Combining the labels for the legend
bars_labels = [bar1, bar2]
lines_labels = [line[0]]
all_labels = bars_labels + lines_labels
labels = [l.get_label() for l in all_labels]

# Increased legend font size
ax1.legend(all_labels, labels, loc='upper left', bbox_to_anchor=(0.47, 1), ncol=1, fontsize=14)
# Set tick font sizes
ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax2.tick_params(axis='y', labelsize=18)
ax1.set_yticks(np.linspace(40000, 65000, 6))
ax2.set_yticks(np.linspace(100, 400, 6))





# Adjusting layout
fig.tight_layout()
plt.subplots_adjust(right=0.75)

# Display the plot
plt.savefig("Figure_1.pdf", bbox_inches="tight")

plt.show()
