import matplotlib.pyplot as plt

file_path='data\checkpoint_penalty_data.csv'
# Read data from CSV
data = pd.read_csv(file_path)

# Extracting data from the CSV file
checkpoint_penalty = data["Checkpoint Penalty"]
static_window_duration = data["Static Window - Duration"]
dynamic_window_duration = data["Dynamic Window - Duration"]
dynamic_mpc_duration = data["Dynamic MPC - Duration"]
reinforcement_learning_duration = data["Reinforcement Learning - Duration"]
static_window_checkpoints = data["Static Window - Checkpoints"]
dynamic_window_checkpoints = data["Dynamic Window - Checkpoints"]
dynamic_mpc_checkpoints = data["Dynamic MPC - Checkpoints"]
reinforcement_learning_checkpoints = data["Reinforcement Learning - Checkpoints"]

# Create a plot with two y-axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot total duration on the left y-axis
ax1.plot(checkpoint_penalty, static_window_duration, label="Static Window - Duration", marker='o')
ax1.plot(checkpoint_penalty, dynamic_window_duration, label="Dynamic Window - Duration", marker='o')
ax1.plot(checkpoint_penalty, dynamic_mpc_duration, label="Dynamic MPC - Duration", marker='o')
ax1.plot(checkpoint_penalty, reinforcement_learning_duration, label="Reinforcement Learning - Duration", marker='o')
ax1.set_xlabel("Checkpoint Penalty (s)")
ax1.set_ylabel("Total Duration (s)")
ax1.set_ylim(0, 60000)
ax1.legend(loc="upper left")
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Create a second y-axis for number of checkpoints
ax2 = ax1.twinx()
ax2.plot(checkpoint_penalty, static_window_checkpoints, label="Static Window - Checkpoints", marker='x', linestyle='--', color='gray')
ax2.plot(checkpoint_penalty, dynamic_window_checkpoints, label="Dynamic Window - Checkpoints", marker='x', linestyle='--', color='black')
ax2.plot(checkpoint_penalty, dynamic_mpc_checkpoints, label="Dynamic MPC - Checkpoints", marker='x', linestyle='--', color='brown')
ax2.plot(checkpoint_penalty, reinforcement_learning_checkpoints, label="Reinforcement Learning - Checkpoints", marker='x', linestyle='--', color='purple')
ax2.set_ylabel("Number of Checkpoints")
ax2.set_ylim(0, 400)
ax2.legend(loc="upper right")

# Show plot
plt.title("Checkpoint Penalty: Total Duration vs Number of Checkpoints")
plt.tight_layout()
plt.show()
