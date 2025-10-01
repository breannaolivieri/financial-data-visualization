import yfinance as yf
import pandas as pd
import datetime

# Let's get Apple stock data for the past year
ticker = "AAPL"
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365)

# Download the data
print(f"Downloading {ticker} stock data...")
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Display first few rows
print("\nFirst 5 rows of data:")
print(stock_data.head())

# Display basic info
print(f"\nTotal days of data: {len(stock_data)}")
print(f"\nColumns available: {stock_data.columns.tolist()}")
