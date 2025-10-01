import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import datetime

# Get the data
ticker = "AAPL"
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=90)  # Last 3 months

print(f"Downloading {ticker} stock data...")
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Handle multi-index columns if present
if isinstance(stock_data.columns, pd.MultiIndex):
    stock_data.columns = stock_data.columns.get_level_values(0)

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=stock_data.index,
    open=stock_data['Open'],
    high=stock_data['High'],
    low=stock_data['Low'],
    close=stock_data['Close'],
    increasing_line_color='#26A69A',  # Green for up days
    decreasing_line_color='#EF5350'   # Red for down days
)])

fig.update_layout(
    title=f'{ticker} Candlestick Chart - Last 3 Months',
    yaxis_title='Stock Price ($)',
    xaxis_title='Date',
    template='plotly_white',
    height=600,
    xaxis_rangeslider_visible=False
)

# Save as HTML
fig.write_html('candlestick_chart.html')
print("\n✅ Candlestick chart saved as 'candlestick_chart.html'!")
print("Open the HTML file in your browser to see the interactive chart!")
fig.show()