# simple_sales_forecast.py
# Author: Awichal Abhishek
# Description: A simple 3-month moving average sales forecast example

import pandas as pd

# Sample sales data
data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales": [120, 135, 150, 160, 170, 180]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate 3-month moving average
df["moving_average"] = df["sales"].rolling(window=3).mean()

# Forecast next month
last_three = df["sales"].tail(3).mean()
forecast = round(last_three, 2)

print("=== Monthly Sales Data ===")
print(df)
print("\nNext Month Sales Forecast (3-month average):", forecast)

