import streamlit as st
import plotly.graph_objects as go
import networkx as nx
import pandas as pd
from st_pages import add_indentation
from functions import generate_graph, plot_network

add_indentation()


def main():
    st.title("Interactive Graph Network")
    
    # Check if the graph and positions are already in session state, otherwise generate them
    if 'G' not in st.session_state:
        st.session_state.G = generate_graph()
        st.session_state.pos = nx.spring_layout(st.session_state.G, seed=88)

    # Dropdown to select the node
    selected_node = st.selectbox("Select a node to highlight its degree 2 connections:", st.session_state.G.nodes())

    # Check if the selected node has changed (or if it hasn't been set yet) 
    # and if we need to re-draw the graph
    if 'selected_node' not in st.session_state or st.session_state.selected_node != selected_node:
        st.session_state.selected_node = selected_node
        fig = plot_network(st.session_state.G, st.session_state.pos, st.session_state.selected_node)
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()