# not working properly line no 125 is issue

import yfinance as yf
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, GRU, Dense
#from pyESN import ESN
import numpy as np
from datetime import date
import pickle
import os

# Set the stock symbol and download the data
stock_symbol = "TCS.NS"
data = yf.download(stock_symbol, period="1y")

# Split the data into train and test sets
train_size = int(len(data) * 0.8)
train_data, test_data = data[:train_size], data[train_size:]

# Preprocess the data
scaler = MinMaxScaler()
train_scaled = scaler.fit_transform(train_data["Close"].values.reshape(-1, 1))
test_scaled = scaler.transform(test_data["Close"].values.reshape(-1, 1))

# ARIMA model
arima_model = ARIMA(train_scaled, order=(5, 1, 0))
arima_model_fit = arima_model.fit()

# LSTM model
lstm_model = Sequential()
lstm_model.add(LSTM(50, activation='relu', input_shape=(1, 1)))
lstm_model.add(Dense(1))
lstm_model.compile(optimizer='adam', loss='mse')
lstm_model.fit(train_scaled, train_scaled, epochs=10, batch_size=1, verbose=0)

# # ESN model
# esn_model = ESN(n_inputs=1, n_outputs=1)
# train_input = train_scaled[:-1].reshape(1, -1, 1)
# train_target = train_scaled[1:].reshape(1, -1, 1)
# esn_model.fit(train_input, train_target)

# GRU model
gru_model = Sequential()
gru_model.add(GRU(50, activation='relu', input_shape=(1, 1)))
gru_model.add(Dense(1))
gru_model.compile(optimizer='adam', loss='mse')
gru_model.fit(train_scaled, train_scaled, epochs=10, batch_size=1, verbose=0)

# SVM model
svm_model = SVR(kernel='linear')
svm_model.fit(np.arange(len(train_scaled)).reshape(-1, 1), train_scaled.flatten())

# Create a directory to save the models if it doesn't exist
models_dir = "models"
os.makedirs(models_dir, exist_ok=True)

# Save the trained models with current date and model name as file names
today = date.today().strftime("%Y-%m-%d")
models = [(arima_model_fit, 'ARIMA'), (lstm_model, 'LSTM'), (gru_model, 'GRU'), (svm_model, 'SVM')]#(esn_model, 'ESN'), 

for model, model_name in models:
    model_file = f'{models_dir}/{today}_{model_name}.pkl'
    with open(model_file, 'wb') as f:
        pickle.dump(model, f)

# Load the saved models
loaded_models = []

for _, model_name in models:
    model_file = f'{models_dir}/{today}_{model_name}.pkl'
    with open(model_file, 'rb') as f:
        loaded_model = pickle.load(f)
        loaded_models.append(loaded_model)

# Predict the stock prices for the next five days
num_days = 5
predictions = []

for model in loaded_models:
    if isinstance(model, ARIMA):
        # ARIMA model prediction
        pred_scaled = model.forecast(steps=num_days)[0]
    elif isinstance(model, Sequential):
        # LSTM or GRU model prediction
        last_input = np.array([test_scaled[-1]])
        pred_scaled = []
        for _ in range(num_days):
            pred = model.predict(last_input.reshape(1, 1, 1))
            pred_scaled.append(pred)
            last_input = np.array([pred])
        pred_scaled = np.array(pred_scaled).reshape(-1, 1)
    # elif isinstance(model, ESN):
    #     # ESN model prediction
    #     last_input = np.array([train_scaled[-1]])
    #     pred_scaled = model.predict(np.ones((num_days, 1)), last_input)
    #     pred_scaled = pred_scaled.flatten()
    elif isinstance(model, SVR):
        # SVM model prediction
        last_index = len(train_scaled) - 1
        pred_scaled = []
        for _ in range(num_days):
            last_index += 1
            pred = model.predict(np.array([[last_index]]))
            pred_scaled.append(pred)
        pred_scaled = np.array(pred_scaled).reshape(-1, 1)

pred_unscaled = scaler.inverse_transform(pred_scaled)
predictions.append(pred_unscaled)

# Create a directory to save the predictions if it doesn't exist
predictions_dir = "predictions"
os.makedirs(predictions_dir, exist_ok=True)

# Save the predicted prices to separate CSV files for each model
for model, model_name in models:
    model_predictions = predictions[models.index((model, model_name))]
    model_predictions = model_predictions.reshape(-1)  # Reshape the predictions array
    prediction_dates = pd.date_range(start=test_data.index[-1] + pd.DateOffset(days=1),
                                     periods=num_days, closed='right')
    prediction_df = pd.DataFrame(data=model_predictions, index=prediction_dates, columns=["Predicted Close"])
    prediction_df.index.name = "Date"
    prediction_df.to_csv(f'{predictions_dir}/{today}_{model_name}_predictions.csv')
