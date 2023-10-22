import streamlit as st
import plotly.graph_objects as go
import networkx as nx
import pandas as pd


# Generate a sample graph
def generate_graph():
    G=nx.Graph()

    df1 = pd.read_csv('Assignment2.csv')
    faculty_names = df1['Full Name'].tolist()

    for name in faculty_names:
        G.add_node(name)

    for i in range(86):
        if i == 67:
            continue
        co_author_df = pd.read_csv('co_author/' + str(i) + '.csv', header = None)
        current_prof = faculty_names[i]

        for _,row in co_author_df.iterrows():
            co_author_name = row[1]
            if co_author_name in faculty_names:
                G.add_edge(current_prof, co_author_name)
    return G

# Get nodes with 2-degree connections from a specific node
def get_degree_2_nodes(G, node):
    first_degree_nodes = list(G.neighbors(node))
    second_degree_nodes = []
    for n in first_degree_nodes:
        second_degree_nodes.extend(list(G.neighbors(n)))
    second_degree_nodes = list(set(second_degree_nodes))
    return first_degree_nodes, second_degree_nodes

# Create the visualization
def plot_network(G, pos,highlight_node=None):
    pos = nx.spring_layout(G, seed=88)
    
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x = [pos[n][0] for n in G.nodes()]
    node_y = [pos[n][1] for n in G.nodes()]
    node_labels = [str(n) for n in G.nodes()]

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        text=node_labels,  # Set node labels
        marker=dict(size=10, color='blue')
    )

    if highlight_node:
        first_degree, second_degree = get_degree_2_nodes(G, highlight_node)
        node_trace['marker']['color'] = ['red' if n == highlight_node else ('yellow' if n in first_degree else ('green' if n in second_degree else 'blue')) for n in G.nodes()]

    fig = go.Figure(data=[go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(color='gray')),
                          node_trace],
                    layout=go.Layout(
                        showlegend=False, 
                        hovermode='closest',
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),  # Hide x-axis gridlines
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)   # Hide y-axis gridlines
                    ))
    
    return fig


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