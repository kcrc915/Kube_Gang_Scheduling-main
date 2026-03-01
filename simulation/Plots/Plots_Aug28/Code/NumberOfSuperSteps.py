import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("simulation_length_data.csv")

simulation_lengths = data["SimulationLength"].values

static = data["StaticDuration"].values
dynamic_window = data["DynamicWindowDuration"].values
dynamic_mpc = data["DynamicMPCDuration"].values
rl = data["RLDuration"].values

line_static = data["StaticCheckpoints"].values
line_dynamic_window = data["DynamicWindowCheckpoints"].values
line_dynamic_mpc = data["DynamicMPCCheckpoints"].values
line_rl = data["RLCheckpoints"].values

bar_width = 0.2
x = np.arange(len(simulation_lengths))

fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()


ax1.bar(x - bar_width * 1.5, static, bar_width,
        label='Static Window - Duration', color='blue', alpha=0.7)

ax1.bar(x - bar_width * 0.5, dynamic_window, bar_width,
        label='Dynamic Window - Duration', color='green', alpha=0.7)

ax1.bar(x + bar_width * 0.5, dynamic_mpc, bar_width,
        label='Dynamic MPC - Duration', color='red', alpha=0.7)

ax1.bar(x + bar_width * 1.5, rl, bar_width,
        label='RL - Duration', color='black', alpha=0.7)


ax2.plot(x, line_static, marker='o', linestyle='--',
         color='blue', label='Static Window - Checkpoints')

ax2.plot(x, line_dynamic_window, marker='^', linestyle='--',
         color='green', label='Dynamic Window - Checkpoints')

ax2.plot(x, line_dynamic_mpc, marker='s', linestyle='--',
         color='red', label='Dynamic MPC - Checkpoints')

ax2.plot(x, line_rl, marker='d', linestyle='--',
         color='black', label='RL - Checkpoints')


ax1.set_xlabel('Number of Superstep(s)', fontsize=18)
ax1.set_ylabel('Duration (s)', fontsize=18)
ax1.set_ylim(0, 120000)

ax1.set_xticks(x)
ax1.set_xticklabels(simulation_lengths)

ax2.set_ylabel('Number of Checkpoints', fontsize=18)
ax2.set_ylim(0, 800)

ax2.set_yticks(np.linspace(0, 800, 6))
ax1.set_yticks(np.linspace(0, 120000, 6))

ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax2.tick_params(axis='y', labelsize=18)

ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper center', fontsize=12)

plt.tight_layout()
plt.show()
