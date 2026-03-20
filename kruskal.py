# Import NetworkX
import networkx as nx


def compute_kruskal_mst(G):
    # Convert graph to undirected (MST requires undirected graph)
    G_undirected = G.to_undirected()

    # Compute Minimum Spanning Tree using Kruskal algorithm
    mst = nx.minimum_spanning_tree(
        G_undirected,
        weight="length",
        algorithm="kruskal"
    )

    # Return MST graph
    return mst