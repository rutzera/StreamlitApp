import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from jsonbin import load_key, save_key
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# Set page title
st.set_page_config(page_title="CSV Scatter Plot")



# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]

# -------- user login --------
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

fullname, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == True:   # login successful
    authenticator.logout('Logout', 'main')   # show logout button
elif authentication_status == False:
    st.error('Username/password is incorrect')
    st.stop()
elif authentication_status == None:
    st.warning('Please enter your username and password')
    st.stop()



st.write(username)


test = load_key(api_key, bin_id, username)
st.write(test)


#### APP
# Set page layout
st.write("# CSV Scatter Plot")
st.write("Upload a CSV file with two numerical columns to generate a scatter plot.")

# Create file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Display scatter plot if file is uploaded
if uploaded_file is not None:
    # Load CSV file into pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Check that DataFrame has at least two columns
    if len(df.columns) < 2:
        st.write("Error: CSV file must have at least two columns.")
    else:
        # Create scatter plot using matplotlib
        fig, ax = plt.subplots()
        ax.scatter(df.iloc[:, 0], df.iloc[:, 1])
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel(df.columns[1])
        ax.set_title("Scatter Plot")

        # Display scatter plot using Streamlit
        st.pyplot(fig)
        
        
