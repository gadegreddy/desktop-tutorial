import os
import pandas as pd
import h5py
import yfinance as yf


def save_stock_data_as_h5(csv_file):
    # Create a folder for storing stock data if it doesn't exist
    if not os.path.exists("Stocks_data"):
        os.makedirs("Stocks_data")

    # Read the input CSV file
    tickers = pd.read_csv(csv_file)["Symbol"]

    for ticker in tickers:
        # Create a separate folder for each stock
        stock_folder = os.path.join("Stocks_data", ticker)
        if not os.path.exists(stock_folder):
            os.makedirs(stock_folder)

        # Fetch stock data using yfinance
        stock_data = yf.download(ticker)

        # Save the stock data as .h5 file
        h5_file = os.path.join(stock_folder, f"{ticker}.h5")
        with h5py.File(h5_file, "w") as hf:
            hf.create_dataset("data", data=stock_data.to_dict(orient="list"))

def update_h5_files():
    # Get the list of folders for each stock
    stock_folders = os.listdir("Stocks_data")

    top_gainers = pd.DataFrame()
    top_losers = pd.DataFrame()

    for folder in stock_folders:
        stock_folder = os.path.join("Stocks_data", folder)
        if os.path.isdir(stock_folder):
            h5_file = os.path.join(stock_folder, f"{folder}.h5")
            with h5py.File(h5_file, "a") as hf:
                # Get the latest data from the .h5 file
                latest_data = hf["data"][-1]

                # Perform calculations to identify gainers and losers
                # Add the data to the top_gainers and top_losers DataFrames

    # Save the top_gainers and top_losers DataFrames as separate CSV files
    top_gainers.to_csv("top_gainers.csv", index=False)
    top_losers.to_csv("top_losers.csv", index=False)

# Example usage
csv_file = "sample_tickers.csv"
save_stock_data_as_h5(csv_file)
update_h5_files()
