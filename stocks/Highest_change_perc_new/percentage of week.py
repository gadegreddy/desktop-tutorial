import pandas as pd

# Read the input CSV file
df = pd.read_csv('all_stock_data_three_months.csv')

# Calculate the month-year
df['Month-Year'] = pd.to_datetime(df['Date']).dt.strftime('%b-%Y')

# Group the data by 'Stock Name', 'Month-Year', and 'Week No' and calculate the percentage change
df['Percentage Change'] = df.groupby(['Stock Name', 'Month-Year', 'Week'])['Adj Close'].transform(lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0] * 100)

# Select the desired columns for the output CSV
output_columns = ['Month-Year', 'Stock Name', 'Week', 'Percentage Change']
output_df = df[output_columns]

# Remove duplicate rows
output_df.drop_duplicates(inplace=True)

# Write the output CSV file
output_df.to_csv('all_stocks_Week_change.csv', index=False)
