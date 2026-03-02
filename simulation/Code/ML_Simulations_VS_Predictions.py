import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("prediction_scatter_data.csv")

markers = {
    'Static Window': 'o',
    'Dynamic Window': '^',
    'Dynamic MPC': 's',
    'RL': 'd'
}

colors = {
    'Static Window': '#0000FF',
    'Dynamic Window': 'tab:green',
    'Dynamic MPC': 'tab:red',
    'RL': 'black'
}

fig, ax = plt.subplots(figsize=(12, 9))

handles_dict = {}

for strategy in df["Strategy"].unique():
    subset = df[df["Strategy"] == strategy]
    
    scatter = ax.scatter(
        subset["SimulatedDuration"],
        subset["PredictedDuration"],
        marker=markers[strategy],
        color=colors[strategy],
        s=100,
        label=strategy
    )
    
    handles_dict[strategy] = scatter

min_val = min(df["SimulatedDuration"].min(), df["PredictedDuration"].min())
max_val = max(df["SimulatedDuration"].max(), df["PredictedDuration"].max())

perfect_line, = ax.plot(
    [min_val, max_val],
    [min_val, max_val],
    'k--',
    label='Perfect Prediction'
)

desired_order = ['Static Window', 'Dynamic Window', 'Dynamic MPC', 'RL']
handles = [handles_dict[s] for s in desired_order] + [perfect_line]
labels = desired_order + ['Perfect Prediction']

ax.set_xlabel("Simulated Duration", fontsize=20)
ax.set_ylabel("Predicted Duration", fontsize=20)

ax.legend(
    handles=handles,
    labels=labels,
    title='Strategy',
    fontsize=16,
    title_fontsize=18
)

ax.tick_params(axis='both', labelsize=16)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
