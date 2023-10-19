import streamlit as st
import pandas as pd
from st_pages import Page, hide_pages, show_pages

st.set_page_config(page_title="Profound", page_icon="🏠", layout="wide")

df = pd.read_csv('Assignment2.csv')
df = df.iloc[0]
# st.image("dp/0.jpg")
# html_str = f"""
#             <h1 style = "text-align : center;" class="a">{df['Full Name']}</h1>
#             """
# st.markdown(html_str, unsafe_allow_html=True)

st.title(df["Full Name"])
st.image("dp/0.jpg")

