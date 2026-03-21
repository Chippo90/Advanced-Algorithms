import random
import time
import osmnx as ox

def run_experiments(G, hospital_list, dijkstra_func, astar_func):

    results = []

    nodes = list(G.nodes)

    for i in range(5):

        #Choose random location in the city
        source = random.choice(nodes)

        #Dijkstra
        start = time.time()
        d_node, d_name, d_distance = dijkstra_func(
            G,
            source,
            hospital_list
        )
        d_time = time.time() - start

        #A*
        start = time.time()
        a_node, a_name, a_distance = astar_func(
            G,
            source,
            hospital_list
        )
        a_time = time.time() - start

        results.append({
            "scenario": i + 1,
            "source": source,
            "dijkstra": (d_name, d_distance, d_time),
            "astar": (a_name, a_distance, a_time)
        })

    return results