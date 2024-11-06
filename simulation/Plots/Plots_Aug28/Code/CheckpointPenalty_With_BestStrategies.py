import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('Strategies_with_Best_results.csv')

# Plot the data
plt.figure(figsize=(10, 6))

# Plot each column against 'Checkpoint_penalty'
plt.plot(data['Checkpoint_penalty'], data[' BestStatic Window'], label='Best Static Window', marker='o')
plt.plot(data['Checkpoint_penalty'], data[' Best DynamicMPC'], label='Best Dynamic MPC', marker='o')
plt.plot(data['Checkpoint_penalty'], data[' Best Dynamic Window'], label='Best Dynamic Window', marker='o')
plt.plot(data['Checkpoint_penalty'], data[' Best RL'], label='Best RL', marker='o')
plt.xticks(range(5, 105, 5))
plt.ylim(40000, 65000)

# Add labels and title
plt.xlabel('Checkpoint Penalty')
plt.ylabel('Time')
plt.title('Checkpoint Penalty vs. Time for Different Strategies')

# Show the legend
plt.legend()

# Show the plot
#plt.grid(True)
plt.show()
