import streamlit as st
import pandas as pd
from st_pages import add_indentation, hide_pages, show_pages, Page, Section


st.set_page_config(layout="wide")

add_indentation()

df = pd.read_csv('Assignment2.csv')
index = 0
df = df.iloc[index]

left_co, cent_co,last_co = st.columns([0.3,0.6,0.1])
with cent_co:
    st.title(df["Full Name"])
    st.image(f"dp/{index}.jpg",width=300)

tab1, tab2 = st.tabs(["Background Information", "Research Profile"])

with tab1:
    st.header("Biography")
    st.write(df['Biography'])
    