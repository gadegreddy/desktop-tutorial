import yfinance as yf
import pandas as pd
import os
import tables as pt

# Read the input CSV file with the stock tickers
input_file = 'sample_tickers.csv'
tickers = pd.read_csv(input_file)['Ticker'].tolist()

def get_top_gainers_and_losers():
    # Fetch the top 10 gainers
    gainers = yf.download(tickers, period='1d', progress=False, actions=False).pct_change().dropna().mean().sort_values(ascending=False)[:10]

    # Fetch the top 10 losers
    losers = yf.download(tickers, period='1d', progress=False, actions=False).pct_change().dropna().mean().sort_values()[:10]

    return gainers, losers

def save_to_h5(data, filename):
    data.to_hdf(filename, key='data', mode='w')

def save_to_csv(data, filename):
    data.to_csv(filename, index=True)

def update_h5_file(stock_symbol, filename):
    existing_data = pd.read_hdf(filename, key='data')
    latest_data = yf.download(stock_symbol, period='1d', progress=False, actions=False).pct_change().dropna().mean()
    updated_data = existing_data.append(latest_data)
    updated_data.to_hdf(filename, key='data', mode='w')

# Create a folder to store the stock data if it doesn't exist
if not os.path.exists("Stocks_data"):
    os.makedirs("Stocks_data")



# Loop through the tickers
for ticker in tickers:
    # Fetch data for the stock ticker
    stock_data = yf.download(ticker, period='1d', progress=False, actions=False).pct_change().dropna().mean()

    # Create a folder for the stock data
    folder_path = os.path.join("Stocks_data", ticker)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the data to an .h5 file
    file_path = os.path.join(folder_path, f"{ticker}.h5")
    save_to_h5(stock_data, file_path)

# Get the top gainers and losers
gainers, losers = get_top_gainers_and_losers()

# Save the top gainers and losers as CSV files
save_to_csv(gainers, 'top_gainers.csv')
save_to_csv(losers, 'top_losers.csv')

# Update the .h5 files with the latest data if available
for gainer in gainers.index:
    folder_path = os.path.join("Stocks_data", str(gainer))
    file_path = os.path.join(folder_path, f"{gainer}.h5")
    if os.path.exists(folder_path) and os.path.exists(file_path):
        update_h5_file(gainer, file_path)

for loser in losers.index:
    folder_path = os.path.join("Stocks_data", str(loser))
    file_path = os.path.join(folder_path, f"{loser}.h5")
    if os.path.exists(file_path):
        update_h5_file(loser, file_path)
