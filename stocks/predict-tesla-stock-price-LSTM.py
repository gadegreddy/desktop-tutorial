#download csv file  of ICICI from the below link 
#https://query1.finance.yahoo.com/v7/finance/download/ICICIBANK.NS?period1=1025481600&period2=1686441600&interval=1d&events=history&includeAdjustedClose=true


import numpy as np 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import load_model


# Reading in the data
icici = pd.read_csv('ICICIBANK.csv')
 
# Isolating the date and close price
icici = icici[['Date', 'Close']]

# Selecting the stationary part of the dataset
"""
Start date: 1/1/22 -> index = 884
End date: 12/31/22 -> index = 1639
"""
new_icici = icici.loc[884:1639]

# Feature preprocessing
new_icici = new_icici.drop('Date', axis=1)
new_icici = new_icici.reset_index(drop=True)
T = new_icici.values.astype('float32')

# Min-max scaling to get the values in the range [0,1] to optimize convergence speed
scaler = MinMaxScaler(feature_range=(0, 1))
T = scaler.fit_transform(T)

# 80-20 split
train_size = int(len(T) * 0.8)
train, test = T[:train_size], T[train_size:]

# Method for creating features from the time series data
def create_features(data, window_size):
    X, Y = [], []
    for i in range(len(data) - window_size - 1):
        window = data[i:(i + window_size), 0]
        X.append(window)
        Y.append(data[i + window_size, 0])
    return np.array(X), np.array(Y)

# Roughly one month of trading assuming 5 trading days per week
window_size = 20
X_train, Y_train = create_features(train, window_size)
X_test, Y_test = create_features(test, window_size)

# Reshape to the format of [samples, time steps, features]
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Building model
model = Sequential()
model.add(LSTM(units=50, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Save models
filepath = 'saved_models/model_epoch_{epoch:02d}.hdf5'
#checkpoint = ModelCheckpoint(filepath=filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
checkpoint = ModelCheckpoint(filepath=filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min', save_weights_only=False)

history = model.fit(X_train, Y_train, epochs=100, batch_size=20, validation_data=(X_test, Y_test), 
                    callbacks=[checkpoint], verbose=1, shuffle=False)

# Save the best model after training
best_model_path = 'saved_models/best_model.hdf5'
model.save(best_model_path)

best_model = load_model('saved_models/best_model.hdf5')


# history = model.fit(X_train, Y_train, epochs=100, batch_size=20, validation_data=(X_test, Y_test), 
#                     callbacks=[checkpoint], verbose=1, shuffle=False)

# # Load the best model and predict
# best_model = Sequential()
# best_model = load_model('saved_models/model_epoch_89.hdf5')

# Predict and inverse transform the predictions

train_predict = best_model.predict(X_train)
Y_hat_train = scaler.inverse_transform(train_predict)

test_predict = best_model.predict(X_test)
Y_hat_test = scaler.inverse_transform(test_predict)

# Inverse transform the actual values, to return them to their original values
Y_train = scaler.inverse_transform([Y_train])
Y_test = scaler.inverse_transform([Y_test])

# Reshape
Y_hat_train = np.reshape(Y_hat_train, newshape=-1)
Y_hat_test = np.reshape(Y_hat_test, newshape=-1)
Y_train = np.reshape(Y_train, newshape=-1)
Y_test = np.reshape(Y_test, newshape=-1)

# Model performance evaluation
train_RMSE = np.sqrt(mean_squared_error(Y_train, Y_hat_train))
test_RMSE = np.sqrt(mean_squared_error(Y_test, Y_hat_test))

print('Train RMSE:', train_RMSE)
print('Test RMSE:', test_RMSE)
