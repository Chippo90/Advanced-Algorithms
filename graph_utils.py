# Import OSMnx for spatial nearest node search
import osmnx as ox


def map_hospitals_to_nodes(G, hospitals):
    # Create an empty list to store hospital node mappings
    # Each hospital is stored individually (important!)
    hospital_list = []

    # Loop through each hospital in the dataset
    for idx, row in hospitals.iterrows():

        # Compute the centroid of the hospital geometry
        point = row.geometry.centroid

        # Extract hospital name (if missing, use default name)
        name = row.get("name", "Unknown Hospital")

        # Find nearest graph node to hospital location
        nearest_node = ox.distance.nearest_nodes(G, point.x, point.y)

        # Store each hospital as separate entry (node, name)
        hospital_list.append((nearest_node, name))

    # Return full hospital list (length should be ~31)
    return hospital_list