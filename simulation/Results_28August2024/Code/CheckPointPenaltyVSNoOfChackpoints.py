import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data_checkpoints = pd.read_csv('CheckPointPenaltyVSNoOfChackpoints.csv')

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot each column against 'Checkpoint Penalty'
plt.plot(data_checkpoints['Checkpoint Penalty'], data_checkpoints['Best Static Window'], label='Best Static Window', marker='o')
plt.plot(data_checkpoints['Checkpoint Penalty'], data_checkpoints['Best DynamicMPC'], label='Best Dynamic MPC', marker='o')
plt.plot(data_checkpoints['Checkpoint Penalty'], data_checkpoints['Best Dynamic Window'], label='Best Dynamic Window', marker='o')
plt.plot(data_checkpoints['Checkpoint Penalty'], data_checkpoints['Best RL'], label='Best RL', marker='o')

# Set x-ticks to include every 5 units from 5 to 100
plt.xticks(range(5, 105, 5))

# Set y-axis limits
plt.ylim(0, 350)  # Adjust the y-axis range based on the data

# Add labels and title
plt.xlabel('Checkpoint Penalty')
plt.ylabel('Number of Checkpoints')
plt.title('Checkpoint Penalty vs. Number of Checkpoints for Different Strategies')

# Show the legend
plt.legend()

# Show the grid for better readability
plt.grid(True)

# Show the plot
plt.show()
