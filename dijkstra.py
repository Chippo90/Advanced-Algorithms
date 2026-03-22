import networkx as nx

def dijkstra_nearest_hospital(G, source, hospital_list):

    #Convert graph to undirected to avoid direction issues
    G_undirected = G.to_undirected()

    #Compute shortest paths to all nodes
    lengths = nx.single_source_dijkstra_path_length(
        G_undirected,
        source,
        weight="length"
    )

    min_distance = float("inf")
    nearest_node = None
    nearest_name = None

    #Find nearest hospital among all nodes
    for node, name in hospital_list:
        if node in lengths:
            distance = lengths[node]
            if distance < min_distance:
                min_distance = distance
                nearest_node = node
                nearest_name = name

    return nearest_node, nearest_name, min_distance
