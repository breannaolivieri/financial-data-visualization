import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Get data for multiple tech stocks
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365)

print("Downloading stock data for multiple companies...")
stock_data = yf.download(tickers, start=start_date, end=end_date)

# Get just the closing prices
closing_prices = stock_data['Close']

# Calculate correlation between stocks
correlation = closing_prices.corr()

# Create the heat map
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, 
            annot=True,  # Show correlation values
            cmap='coolwarm',  # Color scheme
            center=0,
            fmt='.2f',
            square=True,
            linewidths=1,
            cbar_kws={"shrink": 0.8})

plt.title('Stock Price Correlation Heat Map\n(Apple, Microsoft, Google, Amazon, Tesla)', 
          fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("\n✅ Heat map saved as 'correlation_heatmap.png'!")
plt.show()