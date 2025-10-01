import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Get the data
ticker = "AAPL"
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365)

print(f"Downloading {ticker} stock data...")
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Fix the multi-index columns issue
if isinstance(stock_data.columns, pd.MultiIndex):
    stock_data.columns = stock_data.columns.get_level_values(0)

# Calculate moving averages
stock_data['MA_50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['MA_200'] = stock_data['Close'].rolling(window=200).mean()

# Create a figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Top chart: Price with moving averages
ax1.plot(stock_data.index, stock_data['Close'], label='Close Price', linewidth=2, color='#2E86AB')
ax1.plot(stock_data.index, stock_data['MA_50'], label='50-Day MA', linewidth=1.5, color='#A23B72', linestyle='--')
ax1.plot(stock_data.index, stock_data['MA_200'], label='200-Day MA', linewidth=1.5, color='#F18F01', linestyle='--')
ax1.set_title(f'{ticker} Stock Price & Moving Averages - Past Year', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Price ($)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3)

# Bottom chart: Volume
ax2.bar(stock_data.index, stock_data['Volume'].values, color='#6A4C93', alpha=0.7)
ax2.set_title('Trading Volume', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Date', fontsize=12)
ax2.set_ylabel('Volume', fontsize=12)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('stock_dashboard.png', dpi=300, bbox_inches='tight')
print("\n✅ Dashboard saved as 'stock_dashboard.png'!")
plt.show()