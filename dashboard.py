
import streamlit as st
import ccxt
from datetime import datetime

st.set_page_config(page_title="Crypto Bot MVP", layout="wide")

# --- Sidebar ---
st.sidebar.title("Settings")
st.sidebar.markdown("This panel will allow you to adjust trading parameters.")

# --- Page Title ---
st.title("🚀 Crypto Bot MVP")
st.markdown("Welcome to your crypto trading dashboard!")

# --- Market Overview Section ---
st.header("📊 Market Overview")

exchange = ccxt.binance()
symbols = ['BTC/AUD', 'ETH/AUD', 'BNB/AUD']
market_data = {}

for symbol in symbols:
    try:
        ticker = exchange.fetch_ticker(symbol)
        market_data[symbol] = {
            'price': ticker['last'],
            'change': ticker['percentage'],
            'time': datetime.fromtimestamp(ticker['timestamp'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        }
    except Exception as e:
        market_data[symbol] = {'price': 'N/A', 'change': 'N/A', 'time': 'Error fetching data'}

# Display live prices
for symbol, data in market_data.items():
    st.subheader(f"{symbol}")
    st.write(f"💰 Price: {data['price']}")
    st.write(f"📉 Change: {data['change']}%")
    st.write(f"🕒 Updated: {data['time']}")
    st.markdown("---")

# --- Suggested Trades Section ---
st.header("💡 Suggested Trades")
st.success("Trade logic coming soon!")

st.markdown("---")
st.caption("Built for personal use. No financial advice.")
