import pandas as pd
import yfinance as yf

def get_stock_with_highest_percentage_change(input_file, output_file):
    # Read input data from CSV file
    data = pd.read_csv(input_file)

    max_percentage_change = 0
    stock_with_max_change = None
    stock_details = None

    for index, row in data.iterrows():
        ticker = row['SYMBOL']
        stock_data = yf.download(ticker, period='1mo')  # Download stock data for the last month
        if len(stock_data) > 0:
            price_at_start = stock_data['Close'][0]
            price_at_end = stock_data['Close'][-1]
            percentage_change = (price_at_end - price_at_start) / price_at_start * 100

            if percentage_change > max_percentage_change:
                max_percentage_change = percentage_change
                stock_with_max_change = ticker
                stock_details = {
                    'price_at_start': price_at_start,
                    'price_at_end': price_at_end,
                    'percentage_change': percentage_change
                }

    # Update output data with additional details
    output_data = pd.DataFrame({'Ticker': [stock_with_max_change]})
    output_data = pd.concat([output_data, pd.DataFrame(stock_details, index=[0])], axis=1)

    # Write output data to CSV file
    output_data.to_csv(output_file, index=False)

# Example usage
input_file = 'sampl.csv'  # Replace with the path to your input CSV file
output_file = 'Highest_change.csv'  # Replace with the desired path for the output CSV file

get_stock_with_highest_percentage_change(input_file, output_file)
print(f"Output saved to {output_file}")


