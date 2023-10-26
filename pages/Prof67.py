
import streamlit as st
import pandas as pd
from st_pages import add_indentation, hide_pages, show_pages, Page, Section
import ast
from streamlit_extras.tags import tagger_component
from functions import generate_graph, plot_network
import os
import re

st.set_page_config(layout="wide")

add_indentation()

df = pd.read_csv('Assignment2.csv')
df['Research Interest'] = df['Research Interest'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
script_path = os.path.abspath(__file__)

# Extract the filename from the path
script_name = os.path.basename(script_path)
match = re.search(r'\d+', script_name)
if match:
    index = int(match.group())
df = df.iloc[index]

name = df['Full Name']
name1 = name.replace(" ", "_")
# pubs = pd.read_csv(f"publications/{name1}.csv")

# pubs = pubs.drop(columns='Unnamed: 0')
# pubs['Year'] = pubs['Year'].astype(str)


# core = pd.read_csv("CORE.csv")
# condition = pubs['Journal Acronym'].isin(core['Acronym'])
# result_pubs = pubs[condition]
# result_core = core[core['Acronym'].isin(result_pubs['Journal Acronym'])]
# merged_df = pd.merge(result_pubs, result_core, left_on='Journal Acronym',right_on="Acronym" ,how='inner')
# conference = merged_df.drop(["Acronym","Authors","Rank_x"], axis=1)
# conference.rename(columns={'Rank_y': 'Rank'}, inplace=True)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.title(df["Full Name"])
    st.image(f"dp/{index}.jpg",width=300)

tab1, tab2 ,tab3 = st.tabs(["Background Information", "Research Profile", "Collaboration Network"])

with tab1:
    st.header("Biography")
    st.write(df['Biography'])


with tab2:
    st.header("Research Interests")
    tagger_component(
        content= "",
        tags = df['Research Interest'],
        color_name="blue"
    )

    st.header("Publications")
    st.write("No data available from DBLP")
    try:
        name2 = df['Full Name'] + ", Nanyang Technological University"
        citations_year = pd.read_csv(f"citations/{name2}.csv")
        indices = pd.read_csv(f"indices/{name2}.csv")
        newdf = indices.transpose()
        newdf.columns = ['Total']
        year_2018 = []
        year_2018.append(newdf.iloc[1][0])
        year_2018.append(newdf.iloc[3][0])
        newdf.drop(["hindex5y","i10index5y"], inplace = True)
        newdf['2018'] = year_2018
        st.header("Citations")
        st.write("Citations by year")
        st.bar_chart(citations_year, x = "Year", y = "Citations",)
        st.write("Total citations: " + str(int(df['Citations'])))
        st.subheader("Citation Indices")
        st.write(newdf)
    except:
        st.header("Citations")
        st.write("No data available from Google Scholar")


    st.header("Conferences")
    st.write("No data available from DBLP")
    # st.subheader("Number of papers published at conference ranks")
    # st.write(conference['Rank'].value_counts().sort_index(ascending=True))

with tab3:
    G = generate_graph()
    nodes_to_remove = [node for node, degree in dict(G.degree()).items() if degree == 0]
    # Remove nodes with no edges
    G.remove_nodes_from(nodes_to_remove)
    if name in nodes_to_remove:
        st.write("No collaboration network available")
    else:
        fig = plot_network(G, None, name)
        st.plotly_chart(fig)
