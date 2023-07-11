import yfinance as yf

# Define the criteria
low_turnover_threshold = 10000000  # 1,00,00,000 = 1 cr
profit_threshold = 1.8

# Get a list of Indian stock tickers
tickers = ['JITFINFRA.NS','SERVOTECH.NS','BCG.NS','NUCLEUS.NS',	'IZMO.NS','HARDWYN.NS',	'GANGAFORGE.NS','MAANALU.NS',	'INDOTECH.NS', 'SUZLON.NS']  # Example: List of Indian stock tickers

# Loop through each ticker and filter based on criteria
filtered_stocks = []
for ticker_symbol in tickers:
    ticker = yf.Ticker(ticker_symbol)
    history = ticker.history(period="6mo")  # Fetch historical data for the past 6 months (adjust as needed)
    turnover = history['Volume'].mean()  # Calculate average turnover
    returns = (history['Close'][-1] - history['Close'][0]) / history['Close'][0]  # Calculate returns

    if turnover < low_turnover_threshold and returns > profit_threshold:
        filtered_stocks.append(ticker.ticker)
        
# Print the filtered stocks
print("Stocks with low turnover:")
for stock in filtered_stocks:
    print(stock)
