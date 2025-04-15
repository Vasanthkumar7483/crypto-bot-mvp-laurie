
import streamlit as st
import streamlit_authenticator as stauth

# --- LOGIN SETUP ---
credentials = {
    'usernames': {
        'laurie': {
            'name': 'Laurie',
            'password': '$2b$12$wGuB/5dkNmf9jcWBfAUtkemrquMZyPqkjm2/Um6f6LY5yIq4TUpUG'  # Hashed Laurie123
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    'crypto_cookie',
    'abcdef',
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login(
    location='main',
    fields={'Form name': 'Login'}
)

if authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
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
