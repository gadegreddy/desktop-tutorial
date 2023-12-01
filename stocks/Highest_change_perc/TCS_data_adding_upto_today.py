import yfinance as yf
import pandas as pd
import datetime

file_path = "TCS.NS.csv"  # Provide the path to the saved file

# Load the data from the CSV file
stock_data = pd.read_csv(file_path)

last_date = stock_data['Date'].dropna().iloc[-1]  # Exclude rows with NaN values and get the last valid date
last_date = datetime.datetime.strptime(last_date, '%m/%d/%Y').date()

today = datetime.date.today()

missing_dates = []
current_date = last_date + datetime.timedelta(days=1)

while current_date < today:
    if current_date.weekday() < 5:  # Exclude weekends (assuming 0 is Monday and 4 is Friday)
        missing_dates.append(current_date)
    current_date += datetime.timedelta(days=1)

for missing_date in missing_dates:
    # Check if the missing date already exists in the stock_data DataFrame
    if missing_date.strftime('%m/%d/%Y') not in stock_data['Date'].values:
        # Download the missing day's data
        missing_day_data = yf.download("TCS.NS", start=missing_date, end=missing_date + pd.Timedelta(days=1) - pd.Timedelta(seconds=1))

        if not missing_day_data.empty:
            # Create a new DataFrame with the missing day's data
            new_data = pd.DataFrame({'Date': [missing_date]})
            new_data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = missing_day_data.iloc[0]

            # Append the new data to the stock_data DataFrame
            #stock_data = stock_data.append(new_data, ignore_index=True)
            stock_data = pd.concat([stock_data, new_data], ignore_index=True)


# Save the updated data to the CSV file
stock_data.to_csv(file_path, index=False)
