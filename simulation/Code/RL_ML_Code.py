import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


train_data = pd.read_excel("RLTestData.xlsx", sheet_name="Sheet1")

train_data.columns = train_data.columns.str.strip()  
train_data.columns = train_data.columns.str.replace('\ufeff', '')  

X = train_data[["w", "a", "simulation length", "Workload", "Checkpoint penalty"]]
y = train_data["Total Duration"]

X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=200, random_state=42)

model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

y_val_pred = model.predict(X_val)
mse_val = mean_squared_error(y_val, y_val_pred)
print(f"Validation MSE: {mse_val}")

test_data = pd.read_excel("RLtestdata_Testing.xlsx", sheet_name="Sheet1")

test_data.columns = test_data.columns.str.strip()
test_data.columns = test_data.columns.str.replace('\ufeff', '')

results = []

for index, row in test_data.iterrows():
    simulation_length = row["simulation length"]
    workload = row["Workload"]
    checkpoint_penalty = row["checkpoint penalty"]

    best_w = None
    best_a = None
    best_duration = float('inf')

    for w in range(1, 11):
        for a in range(1, 11):
            features = [[w, a, simulation_length, workload, checkpoint_penalty]]

            predicted_duration = model.predict(features)[0]

            if predicted_duration < best_duration:
                best_duration = predicted_duration
                best_w = w
                best_a = a

    results.append({
        "simulation length": simulation_length,
        "Workload": workload,
        "Checkpoint penalty": checkpoint_penalty,
        "Best w": best_w,
        "Best a": best_a,
        "Predicted Duration": best_duration
    })

results_df = pd.DataFrame(results)

results_df.to_csv("RLtestdata_Testing_Results.csv", index=False)

print("Results saved to 'RLtestdata_Testing_Results.csv'")
