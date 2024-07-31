import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('Exploration_fraction_results.csv')

exploration_fraction = data['Exploration_Fraction']
time_without_checkpointing = data['Time taken without checkpointing']
time_with_checkpointing = data['Time taken with checkpoints']
num_checkpoints = data['Number of Checkpoints']

x = np.arange(len(exploration_fraction))

fig, ax1 = plt.subplots()

bar_width = 0.35
bar1 = ax1.bar(x - bar_width / 2, time_without_checkpointing, bar_width, label='Time without Checkpointing')
bar2 = ax1.bar(x + bar_width / 2, time_with_checkpointing, bar_width, label='Time with Checkpointing')

ax1.set_xlabel('Exploration Fraction')
ax1.set_ylabel('Time Taken (s)')
ax1.set_title('Time Taken with and without Checkpointing')
ax1.set_xticks(x)
ax1.set_xticklabels(exploration_fraction)

ax1.set_ylim(45000, 52000)

ax2 = ax1.twinx()
ax2.set_ylabel('Number of Checkpoints')
line = ax2.plot(x, num_checkpoints, 'r--', marker='o', label='Number of Checkpoints')

bars_labels = [bar1, bar2]
lines_labels = [line[0]]
all_labels = bars_labels + lines_labels
labels = [l.get_label() for l in all_labels]
ax1.legend(all_labels, labels, loc='upper left', bbox_to_anchor=(1.15, 1), ncol=1)

fig.tight_layout()
plt.subplots_adjust(right=0.75)

plt.show()