

import pandas as pd
import streamlit as st
import os

# Sample data
data = {'Product': ['A', 'B', 'C'], 
        'Sales': [1200, 850, 950], 
        'Customers': [300, 400, 350]}

# Get the current working directory
current_directory = os.getcwd()
# Define the file path
file_path = os.path.join(current_directory, 'winequality-red.csv')

df = pd.read_csv(file_path)
# df = pd.DataFrame(data)
st.text(type(df))

# Show data with Streamlit elements
st.dataframe(df)                # Interactive table
st.data_editor(df)              # Editable table
st.table(df)                    # Static table

# Customize columns directly in the dataframe display
st.dataframe(df.style.format({'Sales': '${:,.0f}', 'Customers': '{:,.0f}'}))

