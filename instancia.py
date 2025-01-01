import streamlit as st
import pandas as pd

# URL of the public Google Sheet in CSV format
sheet_url = 'https://docs.google.com/spreadsheets/d/1Hu2Rl6QE6-Fd_MeP2M4Ffb6Xzcmwm8cJ1p6QwsJa0fs/export?format=csv'

# Read data from the Google Sheet
@st.cache_data  # Use this for Streamlit Cloud
def load_data():
    data = pd.read_csv(sheet_url)
    return data

# Load the dataset
st.title('Property Details')
data = load_data()

# Display column names for debugging
st.write("Available columns:", data.columns.tolist())

# Display the first row of the dataset
first_row = data.iloc[0]

st.header('Property Information')
st.write(f"**ID:** {first_row.get('ID', 'Not Available')}")
st.write(f"**Location:** {first_row.get('Location', 'Not Available')}")
st.write(f"**Type:** {first_row.get('Type', 'Not Available')}")
st.write(f"**Price:** {first_row.get('Price', 'Not Available')} €")
st.write(f"**Deposit (25%):** {first_row.get('Deposit', 'Not Available')} €")
st.write(f"**Claim Amount:** {first_row.get('Claim Amount', 'Not Available')} €")
st.write(f"**Charges:** {first_row.get('Charges', 'Not Available')} €")
st.write(f"**Appraisal:** {first_row.get('Appraisal', 'Not Available')} €")
st.write(f"**Auction Date:** {first_row.get('Auction Date', 'Not Available')}")
