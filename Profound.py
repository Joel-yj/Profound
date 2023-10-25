import streamlit as st
import pandas as pd
import base64
from streamlit_card import card
from streamlit_tags import st_tags
import ast
from st_pages import Page, hide_pages, show_pages, Section, add_indentation  
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="Profound", page_icon="🏠", layout="wide")
st.title("🔍 Profound ")
st.markdown("##")

# Load data
df = pd.read_csv("Assignment2.csv")
df['Research Interest'] = df['Research Interest'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Sidebar
st.sidebar.image("assets/ntu_logo.jpg")
st.sidebar.header("Filter by")

add_indentation()
show_pages([
    Page('Profound.py', 'Home', "🏠"),
    Page('pages/prof_compare.py', 'Compare Prof', "🔍"),
    Page('pages/graph.py', 'Collaboration Graph', "📊"),
    Section(name = 'Prof Profiles', icon="👥"),
    Page(f'pages/Prof0.py', df.iloc[0]['Full Name'], "👤",in_section=True),
    Page(f'pages/Prof1.py', df.iloc[1]['Full Name'], "👤",in_section=True),
    Page(f'pages/Prof2.py', df.iloc[2]['Full Name'], "👤",in_section=True),
    Page(f'pages/Prof3.py', df.iloc[3]['Full Name'], "👤",in_section=True),
    Page(f'pages/Prof4.py', df.iloc[4]['Full Name'], "👤",in_section=True),
    Page(f'pages/Prof5.py', df.iloc[5]['Full Name'], "👤",in_section=True),
    Page(f'pages/Prof6.py', df.iloc[6]['Full Name'], "👤",in_section=True),
])

if "loaded_images" not in st.session_state:
    st.session_state.loaded_images = {}

# Loading their dp and research interests
total1,total2,total3,=st.columns(3,gap='medium')

# Dashboard for profs
for index,row in df.iterrows():
    if index%3==0:
        with total1:
            
            html_str = f"""
            <h1 style = "text-align : center;" class="a">{row['Full Name']}</h1>
            """
            st.markdown(html_str, unsafe_allow_html=True)
            if index not in st.session_state.loaded_images:
                image_path = "dp/" + str(index) + ".jpg"
                with open(image_path, "rb") as f:
                        data = f.read()
                        encoded = base64.b64encode(data)
                        data = "data:image/png;base64," + encoded.decode("utf-8")
                st.session_state.loaded_images[index] = data
            else:
                data = st.session_state.loaded_images[index]
            hasClicked = card(
                title="",
                text="",
                image=data,
                on_click=lambda: switch_page(row['Full Name']),
                styles={
                    "card": {
                        "max-width" : "100%",
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
            
            keywords = st_tags(label = "## Research Interests", value = row['Research Interest'], text= " ", key= index)

                

    if index%3==1:
        with total2:
            html_str = f"""
                <h1 style = "text-align : center;" class="a">{row['Full Name']}</h1>
                """
            st.markdown(html_str, unsafe_allow_html=True)
            if index not in st.session_state.loaded_images:
                image_path = "dp/" + str(index) + ".jpg"
                with open(image_path, "rb") as f:
                        data = f.read()
                        encoded = base64.b64encode(data)
                        data = "data:image/png;base64," + encoded.decode("utf-8")
                st.session_state.loaded_images[index] = data
            else:
                data = st.session_state.loaded_images[index]

            hasClicked = card(
                title="",
                text="",
                image=data,
                on_click=lambda: switch_page(row['Full Name']),
                styles={
                    "card": {
                        "max-width" : "100%",
                        "height": "500px",
                        "width": "500px",
                        "margin": "10px",
                        "border-radius": "40px",
                        "justifyContent" : "space-between",
                        "filter" : "brightness(2)",
                        "boxShadow": "0px 0px 0px rgba(0, 0, 0, 0)",
                    },
                } 
            )
            keywords = st_tags(label = "## Research Interests", value = row['Research Interest'], text= " ", key= index)


    if index%3==2:
        with total3:
            html_str = f"""
                <h1 style = "text-align : center;" class="a">{row['Full Name']}</h1>
                """
            st.markdown(html_str, unsafe_allow_html=True)
            if index not in st.session_state.loaded_images:
                image_path = "dp/" + str(index) + ".jpg"
                with open(image_path, "rb") as f:
                        data = f.read()
                        encoded = base64.b64encode(data)
                        data = "data:image/png;base64," + encoded.decode("utf-8")
                st.session_state.loaded_images[index] = data
            else:
                data = st.session_state.loaded_images[index]
            card(
                title="",
                text="",
                image=data,
                on_click=lambda: switch_page(row['Full Name']),
                styles={
                    "card": {
                        "max-width" : "100%",
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
            keywords = st_tags(label = "## Research Interests", value = row['Research Interest'], text= " ", key= index)



