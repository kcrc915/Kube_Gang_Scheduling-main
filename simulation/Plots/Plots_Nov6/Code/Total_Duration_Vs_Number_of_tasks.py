import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
file_path = 'Number of tasks Vs Total Duration.csv'
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
plt.xlabel('Tasks')
plt.ylabel('Total Duration')
plt.title('Total Duration Comparison Across Strategies')
plt.legend()
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Show the plot
plt.tight_layout()
plt.show()
