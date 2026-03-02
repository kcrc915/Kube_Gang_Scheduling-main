import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("RL Data.csv")  

df["Duration before Checkpointing"] = pd.to_numeric(df["Duration before Checkpointing"])
df["Durantion after Checkpointing"] = pd.to_numeric(df["Durantion after Checkpointing"])
df["Checkpoints"] = pd.to_numeric(df["Checkpoints"])

window_order = ['W10','W9','W8','W7','W6','W5','W4','W3','W2','W1']
action_order = ['A2','A3','A4','A5','A6','A7','A8','A9','A10']


heat_before = df.pivot(
    index="Window size",
    columns="Action",
    values="Duration before Checkpointing"
).reindex(index=window_order, columns=action_order)

heat_after = df.pivot(
    index="Window size",
    columns="Action",
    values="Durantion after Checkpointing"
).reindex(index=window_order, columns=action_order)

heat_cp = df.pivot(
    index="Window size",
    columns="Action",
    values="Checkpoints"
).reindex(index=window_order, columns=action_order)


vmin_dur = min(heat_before.min().min(), heat_after.min().min())
vmax_dur = max(heat_before.max().max(), heat_after.max().max())


fig, axes = plt.subplots(1, 3, figsize=(24, 7), constrained_layout=True)

hm1 = sns.heatmap(
    heat_before, cmap="YlGnBu",
    vmin=vmin_dur, vmax=vmax_dur,
    cbar=False, ax=axes[0]
)

hm2 = sns.heatmap(
    heat_after, cmap="YlGnBu",
    vmin=vmin_dur, vmax=vmax_dur,
    cbar=False, ax=axes[1]
)

hm3 = sns.heatmap(
    heat_cp, cmap="YlGnBu",
    cbar=False, ax=axes[2]
)

axes[0].set_title("Total Duration without Checkpointing", fontsize=16)
axes[1].set_title("Total Duration with Checkpointing", fontsize=16)
axes[2].set_title("Number of Checkpoints", fontsize=16)

for ax in axes:
    ax.set_xlabel("Action", fontsize=14)
    ax.set_ylabel("Look-ahead Window Size", fontsize=14)


cbar_dur = fig.colorbar(
    hm2.collections[0],
    ax=axes[:2],
    pad=0.02
)
cbar_dur.set_label("Total Duration (s)", fontsize=14)

cbar_cp = fig.colorbar(
    hm3.collections[0],
    ax=axes[2],
    pad=0.02
)
cbar_cp.set_label("Checkpoints", fontsize=14)

x_labels = [int(a.replace('A','')) for a in action_order]
y_labels = [int(w.replace('W','')) for w in window_order]

for ax in axes:
    ax.set_xticks(range(len(action_order)))
    ax.set_yticks(range(len(window_order)))
    ax.set_xticklabels(x_labels)
    ax.set_yticklabels(y_labels)

for ax in axes:
    ax.set_xticks([i + 0.5 for i in range(len(action_order))])
    ax.set_yticks([i + 0.5 for i in range(len(window_order))])

    ax.set_xticklabels(x_labels)
    ax.set_yticklabels(y_labels)






plt.show()
