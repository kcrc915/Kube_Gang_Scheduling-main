import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('heatmap1.csv')

print("Columns in CSV:", data.columns)

print(data.head())

if 'Window size' not in data.columns:
    print("Error: 'Window Size' column not found in CSV.")
else:
    data['Total'] = pd.to_numeric(data['Total'], errors='coerce')

    data = data.dropna(subset=['Total'])

    heatmap_data = data.pivot(index='Window size', columns='Action', values='Total')

    sns.heatmap(heatmap_data, cmap='coolwarm')
    plt.title('Total duration before checkpointing')
    plt.show()
