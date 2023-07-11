import os
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.arima.model import ARIMA
import pickle

# Load the stock data
symbol = "ICICIBANK.NS"
data = yf.download(symbol, start="2010-01-01", end="2023-06-22")

# Define the folder to save the models
model_folder = "saved_models"
if not os.path.exists(model_folder):
    os.makedirs(model_folder)

# Check for existing saved models
saved_models = os.listdir(model_folder)
if saved_models:
    latest_model = max(saved_models)
    with open(os.path.join(model_folder, latest_model), 'rb') as f:
        model = pickle.load(f)
    latest_date = pd.to_datetime(latest_model.split("_")[0])
    new_data = data[data.index > latest_date]
    new_scaled_data = scaler.transform(new_data["Close"].values.reshape(-1, 1))
    for i in range(len(new_scaled_data)):
        model.update(new_scaled_data[i])
else:
    # Preprocess the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1, 1))

    # Define the number of previous days' prices to consider
    lookback = 90

    # Build the ARMA model
    model = ARIMA(scaled_data, order=(2, 0, 1))
    model_fit = model.fit()

# Make predictions for the next five days
future_days = 15
last_x_days = scaled_data[-lookback:].flatten()
predictions = []
for _ in range(future_days):
    prediction = model_fit.forecast(steps=1)
    predictions.append(prediction[0])
    last_x_days = np.append(last_x_days[1:], prediction[0])

# Inverse transform the predicted prices
predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# Create a DataFrame for the predicted prices
dates = pd.date_range(start=data.index[-1] + pd.DateOffset(days=1), periods=future_days)
predicted_prices = pd.DataFrame(predictions, index=dates, columns=["Predicted Price"])

# Save the predicted prices to a CSV file
predicted_prices.to_csv("predicted_prices.csv")

# Save the trained model with the current date as the file name
current_date = pd.to_datetime(data.index[-1]).strftime("%Y-%m-%d")
model_filename = os.path.join(model_folder, f"{current_date}_model.pkl")
with open(model_filename, 'wb') as f:
    pickle.dump(model, f)