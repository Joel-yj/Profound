import streamlit as st
import pandas as pd
import base64
from streamlit_card import card
from streamlit_tags import st_tags
import ast

st.set_page_config(page_title="Profound", page_icon="🏠", layout="wide")
st.title("🔍 Profound ")
st.markdown("##")

# Load data
df = pd.read_csv("Assignment2.csv")
df['Research Interest'] = df['Research Interest'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Sidebar
st.sidebar.image("assets/ntu_logo.jpg")
st.sidebar.header("Filter by")


# Loading their dp

total1,total2,total3,=st.columns(3,gap='large')

# Dashboard for profs
for index,row in df.iterrows():
    if index%3==0:
        with total1:
            
            html_str = f"""
            <h1 style = "text-align : center;" class="a">{row['Full Name']}</h1>
            """
            st.markdown(html_str, unsafe_allow_html=True)
            image_path = "dp/" + str(index) + ".jpg"
            with open(image_path, "rb") as f:
                    data = f.read()
                    encoded = base64.b64encode(data)
                    data = "data:image/png;base64," + encoded.decode("utf-8")
            card(
                title="",
                text="",
                image=data,
                styles={
                    "card": {
                        "height": "500px",
                        "width": "500px",
                        "margin": "10px",
                        "border-radius": "40px",
                        "justifyContent" : "space-between",
                        "filter" : "brightness(2)",
                        "boxShadow": "0px 0px 0px rgba(0, 0, 0, 0)"
                    },
                } 
            )
            
            keywords = st_tags(label = "## Research Interests", value = row['Research Interest'])

    if index%3==1:
        with total2:
            image_path = "dp/" + str(index) + ".jpg"
            with open(image_path, "rb") as f:
                data = f.read()
                encoded = base64.b64encode(data)
                data = "data:image/png;base64," + encoded.decode("utf-8")
                html_str = f"""
                <h1 style = "text-align : center;" class="a">{row['Full Name']}</h1>
                """
                st.markdown(html_str, unsafe_allow_html=True)
            card(
                title="",
                text="",
                image=data,
                styles={
                    "card": {
                        "height": "500px",
                        "width": "500px",
                        "margin": "10px",
                        "border-radius": "40px",
                        "justifyContent" : "space-between",
                        "filter" : "brightness(2)",
                        "boxShadow": "0px 0px 0px rgba(0, 0, 0, 0)"
                    },
                } 
            )
            keywords = st_tags(label = "## Research Interests", value = row['Research Interest'])


    if index%3==2:
        with total3:
            image_path = "dp/" + str(index) + ".jpg"
            with open(image_path, "rb") as f:
                data = f.read()
                encoded = base64.b64encode(data)
                data = "data:image/png;base64," + encoded.decode("utf-8")
                html_str = f"""
                <h1 style = "text-align : center;" class="a">{row['Full Name']}</h1>
                """
                st.markdown(html_str, unsafe_allow_html=True)
            card(
                title="",
                text="",
                image=data,
                styles={
                    "card": {
                        "height": "500px",
                        "width": "500px",
                        "margin": "10px",
                        "border-radius": "40px",
                        "justifyContent" : "space-between",
                        "filter" : "brightness(2)",
                        "boxShadow": "0px 0px 0px rgba(0, 0, 0, 0)"
                    },
                } 
            )
            keywords = st_tags(label = "## Research Interests", value = row['Research Interest'], text= " ")

