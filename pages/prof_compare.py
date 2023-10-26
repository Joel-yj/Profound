import streamlit as st
import pandas as pd
from st_pages import add_indentation, hide_pages, show_pages, Page, Section
from streamlit_extras.tags import tagger_component
import ast

st.set_page_config(layout="wide")
add_indentation()

df = pd.read_csv('Assignment2.csv')
df['Research Interest'] = df['Research Interest'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
core = pd.read_csv("CORE.csv")
st.title("Compare Professors")

col1, col2 = st.columns(2)

with col1:
    prof1 = st.selectbox(
        "Select a professor",
        df['Full Name'].tolist(),
        key = "prof1",
        index= None
    )

    if prof1 != None:
        left_col,centre_col,righ_col = st.columns(3)
        with centre_col:
            with st.container():
                html_str = f"<h1 style='text-align: center;'>{prof1}</h1>"
                st.markdown(html_str, unsafe_allow_html=True)
                dp = df.loc[df['Full Name'] == prof1].index[0]
                st.image(f"dp/{dp}.jpg", use_column_width=True)
        st.header("Research Interests")
        tagger_component(
            content= "",
            tags = df.loc[df['Full Name'] == prof1]["Research Interest"].iloc[0],
            color_name="blue",
        )

        name2 = prof1 + ", Nanyang Technological University"
        try:
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
            st.write("Total citations: " + str(int(df['Citations'].iloc[0])))
            st.subheader("Citation Indices")
            st.write(newdf)
        except:
            st.header("Citations")
            st.write("No data available from Google Scholar")

        name1 = prof1.replace(" ", "_")
        pubs = pd.read_csv(f"publications/{name1}.csv")

        pubs = pubs.drop(columns='Unnamed: 0')
        pubs['Year'] = pubs['Year'].astype(str)

        condition = pubs['Journal Acronym'].isin(core['Acronym'])
        result_pubs = pubs[condition]
        result_core = core[core['Acronym'].isin(result_pubs['Journal Acronym'])]
        merged_df = pd.merge(result_pubs, result_core, left_on='Journal Acronym',right_on="Acronym" ,how='inner')
        conference = merged_df.drop(["Acronym","Authors","Rank_x"], axis=1)
        conference.rename(columns={'Rank_y': 'Rank'}, inplace=True)
        st.header("Conferences")
        st.write(conference)
        st.subheader("Number of papers published at conference ranks")
        st.write(conference['Rank'].value_counts().sort_index(ascending=True))


with col2:
    prof2 = st.selectbox(
        "Select a professor",
        df['Full Name'].tolist(),
        key = "prof2",
        index= None
    )
    if prof2 != None:
        left_col,centre_col,righ_col = st.columns(3)
        with centre_col:
            with st.container():
                html_str = f"<h1 style='text-align: center;'>{prof2}</h1>"
                st.markdown(html_str, unsafe_allow_html=True)
                dp = df.loc[df['Full Name'] == prof2].index[0]
                st.image(f"dp/{dp}.jpg", use_column_width=True)
        st.header("Research Interests")
        tagger_component(
            content= "",
            tags = df.loc[df['Full Name'] == prof2]["Research Interest"].iloc[0],
            color_name="blue",
        )

        name2 = prof2 + ", Nanyang Technological University"
        try:
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
            st.write("Total citations: " + str(int(df['Citations'].iloc[0])))
            st.subheader("Citation Indices")
            st.write(newdf)
        except:
            st.header("Citations")
            st.write("No data available from Google Scholar")
        


        name1 = prof2.replace(" ", "_")
        pubs = pd.read_csv(f"publications/{name1}.csv")

        pubs = pubs.drop(columns='Unnamed: 0')
        pubs['Year'] = pubs['Year'].astype(str)

        condition = pubs['Journal Acronym'].isin(core['Acronym'])
        result_pubs = pubs[condition]
        result_core = core[core['Acronym'].isin(result_pubs['Journal Acronym'])]
        merged_df = pd.merge(result_pubs, result_core, left_on='Journal Acronym',right_on="Acronym" ,how='inner')
        conference = merged_df.drop(["Acronym","Authors","Rank_x"], axis=1)
        conference.rename(columns={'Rank_y': 'Rank'}, inplace=True)
        st.header("Conferences")
        st.write(conference)
        st.subheader("Number of papers published at conference ranks")
        st.write(conference['Rank'].value_counts().sort_index(ascending=True))