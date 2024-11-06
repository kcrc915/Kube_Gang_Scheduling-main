import pandas as pd
import matplotlib.pyplot as plt

# File name for the second dataset
file_path = 'data/Number of tasks Vs Number of Checkpoints.csv'

# Read data from the CSV file
data = pd.read_csv(file_path)

# Extract strategies and tasks
strategies = data['Strategy']
tasks = data.columns[1:]  # All columns except the first one (Strategy)
values = data.iloc[:, 1:].values  # Values excluding the Strategy column

# Plotting
plt.figure(figsize=(10, 6))
for strategy, value in zip(strategies, values):
    plt.plot(tasks, value, marker='o', label=strategy)

# Adding labels and title
plt.xlabel('Number of Tasks')
plt.ylabel('Number of Checkpoints')
plt.title('Number of Tasks Vs Number of Checkpoints')
plt.legend()
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Show the plot
plt.tight_layout()
plt.show()
