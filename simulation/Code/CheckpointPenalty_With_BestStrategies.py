import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Strategies_with_Best_results.csv')

plt.figure(figsize=(10, 6))

plt.plot(data['Checkpoint_penalty'], data[' BestStatic Window'], label='Best Static Window', marker='o')
plt.plot(data['Checkpoint_penalty'], data[' Best DynamicMPC'], label='Best Dynamic MPC', marker='o')
plt.plot(data['Checkpoint_penalty'], data[' Best Dynamic Window'], label='Best Dynamic Window', marker='o')
plt.plot(data['Checkpoint_penalty'], data[' Best RL'], label='Best RL', marker='o')
plt.xticks(range(5, 105, 5))
plt.ylim(40000, 65000)

plt.xlabel('Checkpoint Penalty')
plt.ylabel('Time')
plt.title('Checkpoint Penalty vs. Time for Different Strategies')

plt.legend()

#plt.grid(True)
plt.show()
