import streamlit as st
import pandas as pd
import numpy as np

st.markdown(
    """
    <style>
    .main {
    background-color: #F63366;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

st.title('PhonePe Pulse Dashboard')
st.header('Created by Mayur')


col1, col2, col3 = st.columns(3)
with col1:
    option1 = st.selectbox(
        "Select One",
        ("Transaction", "Users")
    )
with col2:
    option2 = st.selectbox(
        "Select Year",
        ("2018", "2019", "2020", "2021", "2022")
    )
with col3:
    option3 = st.selectbox(
        "Select Quarter",
        ("First", "Second", "Third", "Fourth")
    )

# Showing india's map
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [20.76, 78.4],
    columns=['lat', 'lon'])

st.map(df)
