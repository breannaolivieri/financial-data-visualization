import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Get the data again
ticker = "AAPL"
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365)

print(f"Downloading {ticker} stock data...")
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Create a simple line chart of closing prices
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['Close'], linewidth=2, color='#1f77b4')
plt.title(f'{ticker} Stock Price - Past Year', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the chart
plt.savefig('apple_stock_chart.png', dpi=300, bbox_inches='tight')
print("\n✅ Chart saved as 'apple_stock_chart.png'!")
plt.show()