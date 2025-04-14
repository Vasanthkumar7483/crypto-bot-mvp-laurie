
import streamlit as st

st.set_page_config(page_title="Crypto Bot MVP", layout="wide")

st.title("🚀 Crypto Bot MVP")
st.markdown("Welcome to your crypto trading dashboard!")

st.header("📊 Market Overview")
st.write("This section will display market trends and indicators.")

st.header("💡 Suggested Trades")
st.success("No trades recommended at the moment. Stay tuned!")

st.sidebar.title("Settings")
st.sidebar.markdown("This panel will allow you to adjust trading parameters.")

st.markdown("---")
st.caption("Built for personal use. No financial advice.")
