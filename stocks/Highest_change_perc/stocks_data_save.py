import yfinance as yf
import pandas as pd
import datetime

stock_symbols = ["PTCIL.NS", "DIXON.NS","FORCEMOT.NS", "IWEL.NS","ANGELONE.NS","HEG.NS"]  # Replace with the desired list of stock symbols
start_date = datetime.datetime.now() - datetime.timedelta(days=30)  # Fetch data for the last 30 days
end_date = datetime.datetime.now()

all_stock_data = pd.DataFrame()  # Create an empty DataFrame to store the data for all stocks

for stock_symbol in stock_symbols:
    # Download the stock data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    
    # Add a column to indicate the stock symbol
    stock_data['Symbol'] = stock_symbol
    
    # Calculate turnover
    Turnover = stock_data['Close'] * stock_data['Volume']
    
    # Add a column to indicate the stock symbol
    stock_data['Turnover'] = Turnover
    
    # Concatenate the data for the current stock with the overall data
    all_stock_data = pd.concat([all_stock_data, stock_data])

# Save the data to a CSV file
all_stock_data.to_csv("all_stock_data_2.csv")
