import networkx as nx

def heuristic(u, v, G):
    #Get coordinates of node u
    x1, y1 = G.nodes[u]["x"], G.nodes[u]["y"]
    #Get coordinates of node v
    x2, y2 = G.nodes[v]["x"], G.nodes[v]["y"]
    #Return straight line distance
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def astar_nearest_hospital(G, source, hospital_list):
    #Convert graph to undirected
    G_undirected = G.to_undirected()

    min_distance = float("inf")
    nearest_node = None
    nearest_name = None

    for node, name in hospital_list:
        try:
            #Use A* to compute shortest path length to each hospital
            distance = nx.astar_path_length(
                G_undirected,
                source,
                node,
                heuristic=lambda u, v: heuristic(u, v, G_undirected),
                weight="length"
            )

            #If this is the smallest distance, update results
            if distance < min_distance:
                min_distance = distance
                nearest_node = node
                nearest_name = name

        except Exception as e:
            #If there’s an issue, print error
            print(f"Error in A*: Source={source}, Hospital={name}: {e}")
            continue

    return nearest_node, nearest_name, min_distance
