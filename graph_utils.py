#Import OSMnx for nearest node search
import osmnx as ox

def map_hospitals_to_nodes(G, hospitals):
    #Create an empty list to store hospital nodes
    #Each hospital is stored individually
    hospital_list = []

    #Loop for each hospital in the dataset
    for idx, row in hospitals.iterrows():

        #Compute the centroid of the hospital
        point = row.geometry.centroid

        #Extract hospital name
        name = row.get("name", "Unknown Hospital")

        #Find nearest graph node to hospital location
        nearest_node = ox.distance.nearest_nodes(G, point.x, point.y)

        #Store each hospital separately
        hospital_list.append((nearest_node, name))

    #Return hospital list
    return hospital_list
