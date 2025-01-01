# URL of the public Google Sheet in CSV format
sheet_url = 'https://docs.google.com/spreadsheets/d/1Hu2Rl6QE6-Fd_MeP2M4Ffb6Xzcmwm8cJ1p6QwsJa0fs/export?format=csv'

# Read data from the Google Sheet
@st.cache_data
def load_data():
    data = pd.read_csv(sheet_url)
    return data

# Load the dataset
st.title('Property Details')
data = load_data()

# Display the first row of the dataset
first_row = data.iloc[0]

st.header('Property Information')
st.write(f"**ID:** {first_row['ID']}")
st.write(f"**Location:** {first_row['Location']}")
st.write(f"**Type:** {first_row['Type']}")
st.write(f"**Price:** {first_row['Price']} €")
st.write(f"**Deposit (25%):** {first_row['Deposit']} €")
st.write(f"**Claim Amount:** {first_row['Claim Amount']} €")
st.write(f"**Charges:** {first_row['Charges']} €")
st.write(f"**Appraisal:** {first_row['Appraisal']} €")
st.write(f"**Auction Date:** {first_row['Auction Date']}")
