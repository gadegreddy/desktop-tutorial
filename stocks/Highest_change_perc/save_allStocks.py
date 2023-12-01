import yfinance as yf
import pandas as pd

all_stock_data = pd.DataFrame()  # Create an empty DataFrame to store the data for all stocks
data = pd.read_csv("EQUITY_all.csv")

for index, row in data.iterrows():
    ticker = row['SYMBOL']
    stock_data = yf.download(ticker, period='3mo')  # Download stock data for the last three months
    
    # Reset the index to convert the date index to a column
    stock_data.reset_index(inplace=True)
    
    # Add a column to indicate the stock symbol
    stock_data['Stock Name'] = ticker
    
    # Add a column to indicate the turnover
    stock_data['Turnover'] = stock_data['Close'] * stock_data['Volume']
    
    # Check if turnover is greater than 1000000
    if stock_data['Turnover'].max() > 1000000:
        # Concatenate the data for the current stock with the overall data
        all_stock_data = pd.concat([all_stock_data, stock_data])

# Save the data to a CSV file
all_stock_data.to_csv("all_stock_data_three_months.csv", index=False)
