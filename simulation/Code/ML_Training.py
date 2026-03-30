#Same code can be used for Static, Dynamic Wondow and Dynamic MPC by changing the input files.
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

train_data = pd.read_csv("/content/StaticTestData.csv")

train_data.columns = train_data.columns.str.strip()  
train_data.columns = train_data.columns.str.replace('\ufeff', '')  

train_data = train_data.dropna()

print("Cleaned Column Names:", train_data.columns)

X = train_data[["Window size", "simulation length", "Workload", "checkpoint penalty"]]
y = train_data["Total Duration"]
print(train_data['checkpoint penalty'])
print(train_data['simulation length'])


X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=200, random_state=42)

model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

y_val_pred = model.predict(X_val)
mse_val = mean_squared_error(y_val, y_val_pred)
print(f"Validation MSE: {mse_val}")

test_data = pd.read_csv("/content/StaticWinTesting.csv")

test_data.columns = test_data.columns.str.strip()
test_data.columns = test_data.columns.str.replace('\ufeff', '')

results = []

for index, row in test_data.iterrows():
    simulation_length = row["simulation length"]
    workload = row["Workload"]
    checkpoint_penalty = row["checkpoint penalty"]

    best_window_size = None
    best_duration = float('inf')

    for window_size in range(1, 11):
        features = [[window_size, simulation_length, workload, checkpoint_penalty]]

        predicted_duration = model.predict(features)[0]

        if predicted_duration < best_duration:
            best_duration = predicted_duration
            best_window_size = window_size

    results.append({
        #"Window size": row["Window size"],
        "simulation length": simulation_length,
        "Workload": workload,
        "checkpoint penalty": checkpoint_penalty,
        #"Original Duration": row["Total Duraion"],
        "Best Window Size": best_window_size,
        "Predicted Duration": best_duration
    })

results_df = pd.DataFrame(results)

results_df.to_csv("TestStatWinTesting_Results.csv", index=False)

print("Results saved to 'TestStatWinTesting_Results.csv'")
