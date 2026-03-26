import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Data: List of tuples (Character, Novel)
edges = [
    ("Eugène de Rastignac", "Father Goriot"),
    ("Eugène de Rastignac", "A Distinguished Provincial at Paris"),
    ("Eugène de Rastignac", "Scenes from a Courtesan's Life"),
    ("Eugène de Rastignac", "The Ball at Sceaux"),
    ("Eugène de Rastignac", "The Muse of the Department"),
    ("Eugène de Rastignac", "The Member for Arcis"),
    ("Eugène de Rastignac", "Cousin Betty"),
    ("Eugène de Rastignac", "The Secrets of the Princesse de Cadignan"),
    ("Eugène de Rastignac", "The Firm of Nucingen"),
    ("Vautrin", "Father Goriot"),
    ("Vautrin", "Lost Illusions"),
    ("Vautrin", "Scenes from a Courtesan's Life"),
    ("Vautrin", "The Harlot High and Low"),
    ("Lucien Chardon de Rubempré", "Lost Illusions"),
    ("Lucien Chardon de Rubempré", "Scenes from a Courtesan's Life"),
    ("Delphine de Nucingen", "Father Goriot"),
    ("Delphine de Nucingen", "The Firm of Nucingen"),
    ("Delphine de Nucingen", "The Secrets of the Princesse de Cadignan"),
    ("Baron Frédéric de Nucingen", "Father Goriot"),
    ("Baron Frédéric de Nucingen", "The Firm of Nucingen"),
    ("Baron Frédéric de Nucingen", "César Birotteau"),
    ("Baron Frédéric de Nucingen", "Pierrette"),
    ("Baron Frédéric de Nucingen", "Cousin Betty"),
    ("Horace Bianchon", "Father Goriot"),
    ("Horace Bianchon", "The Atheist's Mass"),
    ("Horace Bianchon", "The Magic Skin"),
    ("Horace Bianchon", "Ursule Mirouët"),
    ("Horace Bianchon", "Cousin Pons"),
    ("Horace Bianchon", "César Birotteau"),
    ("Madame de Beauséant", "Father Goriot"),
    ("Madame de Beauséant", "The Deserted Woman"),
    ("Madame de Beauséant", "The Secrets of the Princesse de Cadignan"),
    ("Madame de Beauséant", "Albert Savarus"),
    ("Henri de Marsay", "The Girl with the Golden Eyes"),
    ("Henri de Marsay", "History of the Thirteen"),
    ("Henri de Marsay", "A Marriage Settlement"),
    ("Henri de Marsay", "Another Study of Woman"),
    ("Henri de Marsay", "The Lily of the Valley"),
    ("César Birotteau", "César Birotteau"),
    ("César Birotteau", "The Firm of Nucingen"),
    ("César Birotteau", "The Middle Classes"),
    ("Anastasie de Restaud", "Father Goriot"),
    ("Maxime de Trailles", "Father Goriot"),
    ("Maxime de Trailles", "A Man of Business"),
    ("Maxime de Trailles", "Cousin Betty"),
    ("Maxime de Trailles", "The Member for Arcis"),
    ("Félix de Vandenesse", "The Lily of the Valley"),
    ("Félix de Vandenesse", "A Woman of Thirty"),
    ("Félix de Vandenesse", "The Muse of the Department"),
    ("Félix de Vandenesse", "A Daughter of Eve"),
    ("Esther Gobseck", "Scenes from a Courtesan's Life"),
    ("Madame Vauquer", "Father Goriot"),
    ("Colonel Chabert", "Colonel Chabert"),
    ("Philippe Bridau", "La Rabouilleuse"),
    ("Philippe Bridau", "A Bachelor's Establishment"),
    ("Joseph Bridau", "La Rabouilleuse"),
    ("Joseph Bridau", "A Bachelor's Establishment"),
    ("Madame Firmiani", "Madame Firmiani"),
    ("Madame Firmiani", "The Secrets of the Princesse de Cadignan"),
    ("Doctor Minoret", "Ursule Mirouët")
]

# Create the graph
G = nx.Graph()
G.add_edges_from(edges)

# Identify node types
nodes = G.nodes()
characters = set([edge[0] for edge in edges])
novels = set([edge[1] for edge in edges])

for node in nodes:
    if node in characters:
        G.nodes[node]['type'] = 'character'
    else:
        G.nodes[node]['type'] = 'novel'

# Set the size of the plot
plt.figure(figsize=(15, 10))

# Positions for all nodes
pos = nx.spring_layout(G, k=0.5, iterations=50)

# Node colors and sizes based on type
node_colors = []
node_sizes = []

for node in G.nodes():
    node_type = G.nodes[node]['type']
    degree = G.degree(node)
    if node_type == 'character':
        node_colors.append('skyblue')
        node_sizes.append(degree * 100)
    else:
        node_colors.append('lightgreen')
        node_sizes.append(800)  # Fixed size for novels

import plotly.graph_objects as go

edge_x = []
edge_y = []

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
node_text = []
node_color = []
node_size = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(node)
    node_type = G.nodes[node]['type']
    degree = G.degree(node)
    if node_type == 'character':
        node_color.append('skyblue')
        node_size.append(degree * 10)
    else:
        node_color.append('lightgreen')
        node_size.append(20)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    textposition="top center",
    hoverinfo='text',
    text=node_text,
    marker=dict(
        showscale=False,
        color=node_color,
        size=node_size,
        line_width=2))

fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='La Comédie Humaine Character-Novel Network',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="",
                        showarrow=False,
                        xref="paper", yref="paper") ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

fig.show()

