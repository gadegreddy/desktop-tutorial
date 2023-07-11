import pandas as pd
import yfinance as yf

def get_stock_with_highest_percentage_change(input_file):
    stock_details = []
    data = pd.read_csv(input_file)
    
    for index, row in data.iterrows():
        ticker = row['STOCK']
        stock_data = yf.download(ticker, period='1mo')  # Download stock data for the last month
        if len(stock_data) > 0:
            price_at_start = stock_data['Close'][0]
            price_at_end = stock_data['Close'][-1]
            percentage_change = (price_at_end - price_at_start) / price_at_start * 100

            stock_details.append({
                'stock': ticker,
                'Price at Start': price_at_start,
                'Price at End': price_at_end,
                'Percentage Change': percentage_change
            })

    return stock_details

# Example usage
input_file = 'EQUITY_L.csv'  # Replace with the path to your input CSV file

stock_details = get_stock_with_highest_percentage_change(input_file)

# Sort the stock details by percentage change in descending order
stock_details.sort(key=lambda x: x['Percentage Change'], reverse=True)

# Get the top 10 stocks with maximum percentage change
top_10_max_change = stock_details[:500]

# Sort the stock details by percentage change in ascending order
stock_details.sort(key=lambda x: x['Percentage Change'])

# Get the top 10 stocks with minimum percentage change
top_10_min_change = stock_details[:100]

# Write the output to separate CSV files
pd.DataFrame(top_10_max_change).to_csv('June_Top_Gainers.csv', index=False)
pd.DataFrame(top_10_min_change).to_csv('June_Top_Losers.csv', index=False)
