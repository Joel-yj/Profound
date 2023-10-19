import streamlit as st
import pandas as pd
from st_pages import add_indentation, hide_pages, show_pages, Page, Section


st.set_page_config(page_title="Profound", page_icon="🏠", layout="wide")
hide_pages([
    Page('profound.py'),
    Page("Prof1.py")
])
add_indentation()

df = pd.read_csv('Assignment2.csv')
index = 0
df = df.iloc[index]
# st.image("dp/0.jpg")
# html_str = f"""
#             <h1 style = "text-align : center;" class="a">{df['Full Name']}</h1>
#             """
# st.markdown(html_str, unsafe_allow_html=True)

st.title(df["Full Name"])
st.image(f"dp/{index}.jpg",width=300)
st.header("Background Information")

