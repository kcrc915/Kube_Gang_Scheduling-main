import pandas as pd
from sklearn.metrics import r2_score

data = pd.read_csv('/content/RLtestdata_Testing_Results.csv')

y = data['Simulated Duration']
y_hat = data['Predicted Duration']


r2 = r2_score(y, y_hat)

rmse = np.sqrt(mean_squared_error(y, y_hat))

mae = mean_absolute_error(y, y_hat)

mape = np.mean(np.abs((y - y_hat) / y)) * 100

print(f'R-squared (R²): {r2:.4f}')
print(f'RMSE: {rmse:.4f}')
print(f'MAE: {mae:.4f}')
print(f'MAPE: {mape:.2f}%')
print(f'R-squared (R²) value: {r2}')
