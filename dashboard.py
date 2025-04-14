
import streamlit as st
import streamlit_authenticator as stauth

# --- LOGIN SETUP ---
names = ['Laurie']
usernames = ['laurie']
passwords = ['Laurie123']  # You can hash this later for security

authenticator = stauth.Authenticate(
    names, usernames, passwords,
    'crypto_cookie', 'abcdef', cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
elif authentication_status:

    # --- MAIN DASHBOARD ---
    st.set_page_config(page_title="Crypto Bot MVP", layout="wide")
    st.sidebar.title("Settings")
    st.sidebar.markdown("This panel will allow you to adjust trading parameters.")

    st.title("🚀 Crypto Bot MVP")
    st.markdown("Welcome to your crypto trading dashboard!")

    st.header("📊 Market Overview")
    st.write("This section will display market trends and indicators.")

    st.header("💡 Suggested Trades")
    st.success("No trades recommended at the moment. Stay tuned!")

    st.markdown("---")
    st.caption("Built for personal use. No financial advice.")
