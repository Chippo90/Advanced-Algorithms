**Hamburg Hospital Shortest Path Analysis**

This project analyzes the road network of Hamburg and computes the shortest path from random locations to the nearest hospital. The system uses three graph algorithms: Dijkstra’s, A*, and Kruskal’s (Minimum Spanning Tree). Data is retrieved from OpenStreetMap via OSMnx.

**1. Project Structure.**

├── main.py

├── data_loader.py

├── graph_utils.py

├── dijkstra.py

├── astar.py

├── kruskal.py

├── evaluation.py

└── README.md


**2. Installation**

Create a virtual environment:
python -m venv .venv

Activate the environment:
On macOS/Linux:
source .venv/bin/activate

On Windows:
.venv\Scripts\activate

Install dependencies:
pip install osmnx networkx geopandas scikit-learn

**3. Running the Program**
python main.py

This will:

A. Load the Hamburg road network graph.

B. Load hospital data from OpenStreetMap.

C. Map hospitals to nearest graph nodes.

D. Run 5 scenarios (random locations).

E. Compare Dijkstra vs A* runtimes.

F. Compute a Minimum Spanning Tree using Kruskal.

**4. Output**

For each scenario, you will see:

i. Nearest hospital name

ii. Distance (meters)

iii. Runtime (seconds) for both Dijkstra and A*

iv. Algorithms Used

v. Dijkstra: Greedy shortest path algorithm that expands the closest unvisited node.

vi. A*: Informed search using a heuristic (Euclidean distance) to guide the search.

vii. Kruskal: Greedy algorithm used to compute the Minimum Spanning Tree of the entire graph.



**5. Author:**

Chehab Hany

Gisma University of Applied Sciences
