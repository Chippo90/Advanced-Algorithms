#Import project modules
from data_loader import load_graph, load_hospitals
from graph_utils import map_hospitals_to_nodes
from dijkstra import dijkstra_nearest_hospital
from astar import astar_nearest_hospital
from kruskal import compute_kruskal_mst
from evaluation import run_experiments

def main():
    #Load road network
    print("Loading graph...")
    G = load_graph()

    #Load hospitals
    print("Loading all hospitals...")
    hospitals = load_hospitals()

    #Map hospitals to graph nodes
    print("Mapping hospitals to the graph...")
    hospital_list = map_hospitals_to_nodes(G, hospitals)

    #Print total hospitals
    print(f"Total number of hospitals: {len(hospital_list)}")

    #Run scenarios
    print("Running scenarios...")
    results = run_experiments(
        G,
        hospital_list,
        dijkstra_nearest_hospital,
        astar_nearest_hospital
    )

    #Print results
    print("\nResults:")

    for r in results:
        print(f"\nScenario {r['scenario']}:")

        #Unpack Dijkstra results
        d_name, d_distance, d_time = r["dijkstra"]

        print("Dijkstra")
        print(f"  Hospital: {d_name}")
        print(f"  Distance: {d_distance:.2f} meters")
        print(f"  Runtime: {d_time:.4f} seconds")

        #Unpack A* results
        a_name, a_distance, a_time = r["astar"]

        print("A*")
        print(f"  Hospital: {a_name}")
        print(f"  Distance: {a_distance:.2f} meters")
        print(f"  Runtime: {a_time:.4f} seconds")

    # Compute Kruskal MST
    print("Computing Kruskal MST...")
    mst = compute_kruskal_mst(G)

    print("MST is computed successfully!")

#Run main file
if __name__ == "__main__":
    main()