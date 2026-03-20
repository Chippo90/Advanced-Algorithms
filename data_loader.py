# Import OSMnx to download and process OpenStreetMap data
import osmnx as ox


def load_graph(place_name="Hamburg, Germany"):
    # Download the road network graph for the city (drivable roads only)
    G = ox.graph_from_place(place_name, network_type="drive")

    # Project the graph to a metric CRS (so distances are in meters)
    G = ox.project_graph(G)

    # Return the prepared graph
    return G


def load_hospitals(place_name="Hamburg, Germany"):
    # Define the OpenStreetMap tag used to retrieve hospitals
    tags = {"amenity": "hospital"}

    # Download all hospital features in the city
    hospitals = ox.features_from_place(place_name, tags)

    # Return the hospitals GeoDataFrame
    return hospitals