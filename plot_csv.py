import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



# Set page title
st.set_page_config(page_title="CSV Scatter Plot")

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
        
        
with st.sidebar:
    with st.spinner("Loading..."):
        if st.button('Say hello'):
            st.write("Well hello there")
