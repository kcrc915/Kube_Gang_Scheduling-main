import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("checkpoint_data.csv")

checkpoint_penalty = data["CheckpointPenalty"].values

static_window = data["StaticWindowDuration"].values
dynamic_window = data["DynamicWindowDuration"].values
dynamic_mpc = data["DynamicMPCDuration"].values
reinforcement_learning = data["RLDuration"].values

static_window_checkpoints = data["StaticWindowCheckpoints"].values
dynamic_window_checkpoints = data["DynamicWindowCheckpoints"].values
dynamic_mpc_checkpoints = data["DynamicMPCCheckpoints"].values
reinforcement_learning_checkpoints = data["RLCheckpoints"].values


fig, ax1 = plt.subplots(figsize=(12, 6))

bar_width = 2
x = np.array(checkpoint_penalty)

ax1.bar(x - bar_width*1.5, static_window, width=bar_width, label="Static Window - Duration", color='blue', alpha=0.7)
ax1.bar(x - bar_width/2, dynamic_window, width=bar_width, label="Dynamic Window - Duration", color='green', alpha=0.7)
ax1.bar(x + bar_width/2, dynamic_mpc, width=bar_width, label="Dynamic MPC - Duration", color='red', alpha=0.7)
ax1.bar(x + bar_width*1.5, reinforcement_learning, width=bar_width, label="RL - Duration", color='black', alpha=0.7)

ax1.set_xlabel("Checkpoint Penalty (s)", fontsize=18)
ax1.set_ylabel("Duration (s)", fontsize=18)
ax1.set_ylim(40000, 65000)

ax2 = ax1.twinx()

ax2.plot(checkpoint_penalty, static_window_checkpoints, marker='o', linestyle='--', color='blue', label="Static Window - Checkpoints")
ax2.plot(checkpoint_penalty, dynamic_window_checkpoints, marker='^', linestyle='--', color='green', label="Dynamic Window - Checkpoints")
ax2.plot(checkpoint_penalty, dynamic_mpc_checkpoints, marker='s', linestyle='--', color='red', label="Dynamic MPC - Checkpoints")
ax2.plot(checkpoint_penalty, reinforcement_learning_checkpoints, marker='d', linestyle='--', color='black', label="RL - Checkpoints")

ax2.set_ylabel("Number of Checkpoints", fontsize=18)
ax2.set_ylim(0, 500)
ax2.set_yticks(np.linspace(0, 500, 6))

ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper center', fontsize=12)

plt.xticks(checkpoint_penalty)
ax1.tick_params(axis='both', labelsize=18)
ax2.tick_params(axis='y', labelsize=18)

plt.tight_layout()
plt.show()
