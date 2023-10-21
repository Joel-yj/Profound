import streamlit as st
import pandas as pd
from st_pages import add_indentation, hide_pages, show_pages, Page, Section


st.set_page_config(layout="wide")
add_indentation()

df = pd.read_csv('Assignment2.csv')

st.title("Compare Professors")

col1, col2 = st.columns(2)

with col1:
    prof1 = st.selectbox(
        "Select a professor",
        df['Full Name'].tolist(),
        key = "prof1"
    )
    st.header(prof1)
    dp = df.loc[df['Full Name'] == prof1].index[0]
    st.image(f"dp/{dp}.jpg", width=300)


with col2:
    prof2 = st.selectbox(
        "Select a professor",
        df['Full Name'].tolist(),
        key = "prof2"
    )
    st.header(prof2)