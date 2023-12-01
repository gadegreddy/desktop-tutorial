import yfinance as yf
import pandas as pd

# Download historical stock data for TCS
symbol = "TCS.NS"  # 'NS' represents the stock exchange (in this case, NSE)
start_date = "2023-06-22"
end_date = "2023-06-22"

start = pd.Timestamp(start_date)
end = pd.Timestamp(end_date) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

data = yf.download(symbol, start=start, end=end)

# Calculate turnover
data['Turnover'] = data['Close'] * data['Volume']

# Display the calculated turnover
print(data['Turnover'])
