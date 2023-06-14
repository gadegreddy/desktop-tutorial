import pandas as pd
import numpy as np
import tensorflow as tf
import yfinance as yf

def predict_stock_price(symbol, start_date, end_date):
    # Get the historical stock data
    df = yf.download(symbol, start_date, end_date)

    # Create the LSTM model
    model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(units=128, input_shape=(df.shape[1], 1)),
        tf.keras.layers.Dense(units=1)
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mse')

    # Train the model
    model.fit(df.values, df['Adj Close'].values, epochs=100)

    # Save the model
    model_filename = "tf_" + symbol + '_' + start_date + '.h5'
    model.save(model_filename)

    # Predict the stock price for the next five days
    prediction = model.predict(df.values[-5:])
    prediction = pd.DataFrame(prediction, columns=['Prediction'])

    # Save the prediction as a csv file
    prediction.to_csv('prediction_tf.csv', index=False)

if __name__ == '__main__':
    # Get the stock symbol and the start and end dates
    symbol = 'JSWISPL.NS'
    start_date = '2023-01-01'
    end_date = '2023-06-13'

    # Predict the stock price
    predict_stock_price(symbol, start_date, end_date)
