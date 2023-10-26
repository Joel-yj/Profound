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
options= []
options.append("All")
options.extend(df['Full Name'].tolist())
filter = st.sidebar.selectbox("Search for Professors",options,key="filter",)

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

# Loading their dp and research interests
total1,total2,total3,=st.columns(3,gap='medium')

if filter == "All":
    row_number = 0
    with st.container():
        for index, row in df.iterrows():
            if index % 3 == 0:
                row_number += 1
                columns = st.columns(3)
            
            with columns[index % 3]:
                html_str = f"<h1 style='text-align: center;'>{row['Full Name']}</h1>"
                st.markdown(html_str, unsafe_allow_html=True)

                image_path = "dp/" + str(index) + ".jpg"
                with open(image_path, "rb") as f:
                    data = f.read()
                    encoded = base64.b64encode(data)
                    data = "data:image/png;base64," + encoded.decode("utf-8")

                hasClicked = card(
                    title="",
                    text="",
                    image=data,
                    on_click=lambda: switch_page(row['Full Name']),
                    styles={
                        "card": {
                            "max-width": "100%",
                            "height": "500px",
                            "width": "500px",
                            "margin": "10px",
                            "border-radius": "40px",
                            "justifyContent": "space-between",
                            "filter": "brightness(2)",
                            "boxShadow": "0px 0px 0px rgba(0, 0, 0, 0)",
                        },
                    },
                )

                keywords = st_tags(
                    label="## Research Interests",
                    value=row['Research Interest'],
                    text=" ",
                    key=index
                )
else:
    filtered_df = df[df['Full Name'].str.contains(filter, case=False, na=False)]
    filtered_df['Research Interest'] = filtered_df['Research Interest'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    html_str = f"<h1 style='text-align: center;'>{filtered_df.iloc[0]['Full Name']}</h1>"
    st.markdown(html_str, unsafe_allow_html=True)

    image_path = "dp/" + str(filtered_df.index[0]) + ".jpg"
    with open(image_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
        data = "data:image/png;base64," + encoded.decode("utf-8")

    hasClicked = card(
        title="",
        text="",
        image=data,
        on_click=lambda: switch_page(filtered_df.iloc[0]['Full Name']),
        styles={
            "card": {
                "max-width": "100%",
                "height": "500px",
                "width": "500px",
                "margin": "10px",
                "border-radius": "40px",
                "justifyContent": "space-between",
                "filter": "brightness(2)",
                "boxShadow": "0px 0px 0px rgba(0, 0, 0, 0)",
            },
        },
    )

    keywords = st_tags(
        label="## Research Interests",
        value=filtered_df.iloc[0]['Research Interest'],
        text=" ",
    )


                



