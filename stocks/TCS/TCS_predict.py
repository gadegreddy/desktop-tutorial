import os
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense

# Load the stock data
symbol = "TCS.NS"
data = yf.download(symbol, start="2010-01-01", end="2023-06-22")

# Define the folder to save the models
model_folder = "saved_models"
os.makedirs(model_folder, exist_ok=True)

# Check for existing saved models
saved_models = os.listdir(model_folder)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1, 1))

if saved_models:
    latest_model = max(saved_models)
    model = load_model(os.path.join(model_folder, latest_model))
    latest_date = pd.to_datetime(latest_model.split("_")[0])
    new_data = data[data.index > latest_date]
    scaler = MinMaxScaler(feature_range=(0, 1))
    new_scaled_data = scaler.fit_transform(new_data["Close"].values.reshape(-1, 1))
    lookback = 6  # Number of previous days' prices to consider

    X_new, y_new = [], []
    for i in range(lookback, len(new_scaled_data)):
        X_new.append(new_scaled_data[i - lookback:i, 0])
        y_new.append(new_scaled_data[i, 0])

    X_new, y_new = np.array(X_new), np.array(y_new)
    X_new = np.reshape(X_new, (X_new.shape[0], X_new.shape[1], 1))

    model.fit(X_new, y_new, epochs=50, batch_size=32)

else:
   
    # Prepare the data for LSTM
    lookback = 6  # Number of previous days' prices to consider
    X, y = [], []
    for i in range(lookback, len(scaled_data)):
        X.append(scaled_data[i - lookback:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))
    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(X, y, epochs=50, batch_size=32)

# Make predictions for the next five days
future_days = 5
last_x_days = scaled_data[-lookback:].reshape(1, lookback, 1)
predictions = []
for _ in range(future_days):
    prediction = model.predict(last_x_days)
    predictions.append(prediction[0, 0])
    last_x_days = np.append(last_x_days[:, 1:, :], prediction.reshape(1, 1, 1), axis=1)

# Inverse transform the predicted prices
predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# Create a DataFrame for the predicted prices
dates = pd.date_range(start=data.index[-1] + pd.DateOffset(days=1), periods=future_days)
predicted_prices = pd.DataFrame(predictions, index=dates, columns=["Predicted Price"])

# Save the predicted prices to a CSV file
predicted_prices.to_csv("predicted_prices.csv")

# Save the trained model with the current date as the file name
current_date = pd.to_datetime(data.index[-1]).strftime("%Y-%m-%d")
model.save(os.path.join(model_folder, f"{current_date}_model.h5"))
