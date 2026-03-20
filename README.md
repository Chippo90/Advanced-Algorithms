Hamburg Hospital Shortest Path Analysis
This project analyzes the road network of Hamburg and computes the shortest path from random locations to the nearest hospital. The system uses three graph algorithms: Dijkstra’s, A*, and Kruskal’s (Minimum Spanning Tree). Data is retrieved from OpenStreetMap via OSMnx.

1. Project Structure.

├── main.py

├── data_loader.py

├── graph_utils.py

├── dijkstra.py

├── astar.py

├── kruskal.py

├── evaluation.py

└── README.md


3. Installation

Create a virtual environment:
python -m venv .venv

Activate the environment:

On macOS/Linux:
source .venv/bin/activate

On Windows:
.venv\Scripts\activate

Install dependencies:
pip install osmnx networkx geopandas scikit-learn

Running the Program
python main.py

This will:

Load the Hamburg road network graph.
Load hospital data from OpenStreetMap.
Map hospitals to nearest graph nodes.
Run 5 scenarios (random locations).
Compare Dijkstra vs A* runtimes.
Compute a Minimum Spanning Tree using Kruskal.
Output

For each scenario, you will see:

Nearest hospital name
Distance (meters)
Runtime (seconds) for both Dijkstra and A*
Algorithms Used
Dijkstra: Greedy shortest path algorithm that expands the closest unvisited node.
A*: Informed search using a heuristic (Euclidean distance) to guide the search.
Kruskal: Greedy algorithm used to compute the Minimum Spanning Tree of the entire graph.
Screenshots

Author:
Chehab Hany
