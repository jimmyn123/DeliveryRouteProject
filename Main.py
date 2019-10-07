# Jimmy Nguyen
# Student ID: 000579757

from HashTable import DirectHashTable
from Package import Package
from Graph import Graph
from LocationVertex import LocationVertex
from datetime import date, datetime, time, timedelta
from Truck import Truck


# Displays the locations and their IDs
def display_locations(location_list):
    for i in range(1, location_list.__len__()+1):
        print("ID: " + str(i) + ", location: " + str(location_list[i]))

def initialize_locations():
    # Create a list of the locations
    location_list = {};
    location_list[1] = "Made Up University, 7001 North 700 East, Salt Lake City, UT 84107"
    location_list[2] = "International Peace Gardens, 1060 Dalton Ave S, Salt Lake City, UT 84104"
    location_list[3] = "Sugar House Park, 1330 2100 S, Salt Lake City, UT 84106"
    location_list[4] = "Taylorsville-Bennion Heritage City Gov Off, 1488 4800 S, Salt Lake City, UT 84123"
    location_list[5] = "Salt Lake City Division of Health Services, 177 W Price Ave, Salt Lake City, UT 84115"
    location_list[6] = "South Salt Lake Public Works, 195 W Oakland Ave, Salt Lake City, UT 84115"
    location_list[7] = "Salt Lake City Streets and Sanitation, 2010 W 500 S, Salt Lake City, UT 84104"
    location_list[8] = "Deker Lake, 2300 Parkway Blvd, West Valley City, UT 84119"
    location_list[9] = "Salt Lake City Ottinger Hall, 233 Canyon Rd, Salt Lake City, UT 84103"
    location_list[10] = "Columbus Library, 2530 S 500 E, Salt Lake City, UT 84106"
    location_list[11] = "Taylorsville City Hall, 2600 Taylorsville Blvd, Salt Lake City, UT 84118"
    location_list[12] = "South Salt Lake Police, 2835 Main St, Salt Lake City, UT 84115"
    location_list[13] = "Council Hall, 300 State St, Salt Lake City, UT 84103"
    location_list[14] = "Redwood Park, 3060 Lester St, West Valley City, UT 84119"
    location_list[15] = "Salt Lake County Mental Health, 3148 S 1100 W, Salt Lake City, UT 84119"
    location_list[16] = "Salt Lake County/United Police Dept, 3365 S 900 W, Salt Lake City, UT 84119"
    location_list[17] = "West Valley Prosecutor, 3575 W Valley Central Sta bus Loop, West Valley City, UT 84119"
    location_list[18] = "Housing Auth. of Salt Lake County, 3595 Main St, West Valley City, UT 84115"
    location_list[19] = "Utah DMV Administrative Office, 380 W 2880 S, West Valley City, UT 84115"
    location_list[20] = "Third District Juvenile Court, 410 S State St, Salt Lake City, UT 84111"
    location_list[21] = "Cottonwood Regional Softball Complex, 4300 S 1300 E, Millcreek, UT 84117"
    location_list[22] = "Holiday City Office, 4580 S 2300 E, Holladay, UT 84117"
    location_list[23] = "Murray City Museum, 5025 State St, Murray, UT 84107"
    location_list[24] = "Valley Regional Softball Complex, 5100 South 2700 West, Millcreek, UT 84118"
    location_list[25] = "City Center of Rock Springs, 5383 South 900 East #104, Millcreek, UT 84117"
    location_list[26] = "Rice Terrace Pavilion Park, 600 E 900 South, Millcreek, UT 84105"
    location_list[27] = "Wheeler Historic Farm , 6351 South 900 East, Murray, UT 84121"

    return location_list


def initialize_vertices(location_list):
    vertices = {}
    vertices[1] = LocationVertex(location_list[1])
    vertices[2] = LocationVertex(location_list[2])
    vertices[3] = LocationVertex(location_list[3])
    vertices[4] = LocationVertex(location_list[4])
    vertices[5] = LocationVertex(location_list[5])
    vertices[6] = LocationVertex(location_list[6])
    vertices[7] = LocationVertex(location_list[7])
    vertices[8] = LocationVertex(location_list[8])
    vertices[9] = LocationVertex(location_list[9])
    vertices[10] = LocationVertex(location_list[10])
    vertices[11] = LocationVertex(location_list[11])
    vertices[12] = LocationVertex(location_list[12])
    vertices[13] = LocationVertex(location_list[13])
    vertices[14] = LocationVertex(location_list[14])
    vertices[15] = LocationVertex(location_list[15])
    vertices[16] = LocationVertex(location_list[16])
    vertices[17] = LocationVertex(location_list[17])
    vertices[18] = LocationVertex(location_list[18])
    vertices[19] = LocationVertex(location_list[19])
    vertices[20] = LocationVertex(location_list[20])
    vertices[21] = LocationVertex(location_list[21])
    vertices[22] = LocationVertex(location_list[22])
    vertices[23] = LocationVertex(location_list[23])
    vertices[24] = LocationVertex(location_list[24])
    vertices[25] = LocationVertex(location_list[25])
    vertices[26] = LocationVertex(location_list[26])
    vertices[27] = LocationVertex(location_list[27])

    return vertices


def initialize_map(vertices):
    # Create graph and add vertex locations
    route_map = Graph()

    # Adds the actual vertices to the graph
    route_map.add_vertex(vertices[1])
    route_map.add_vertex(vertices[2])
    route_map.add_vertex(vertices[3])
    route_map.add_vertex(vertices[4])
    route_map.add_vertex(vertices[5])
    route_map.add_vertex(vertices[6])
    route_map.add_vertex(vertices[7])
    route_map.add_vertex(vertices[8])
    route_map.add_vertex(vertices[9])
    route_map.add_vertex(vertices[10])
    route_map.add_vertex(vertices[11])
    route_map.add_vertex(vertices[12])
    route_map.add_vertex(vertices[13])
    route_map.add_vertex(vertices[14])
    route_map.add_vertex(vertices[15])
    route_map.add_vertex(vertices[16])
    route_map.add_vertex(vertices[17])
    route_map.add_vertex(vertices[18])
    route_map.add_vertex(vertices[19])
    route_map.add_vertex(vertices[20])
    route_map.add_vertex(vertices[21])
    route_map.add_vertex(vertices[22])
    route_map.add_vertex(vertices[23])
    route_map.add_vertex(vertices[24])
    route_map.add_vertex(vertices[25])
    route_map.add_vertex(vertices[26])
    route_map.add_vertex(vertices[27])

    # add edge for 2nd vertex
    route_map.add_undirected_edge(vertices[1], vertices[2], 7.2)

    # add edge for 3rd vertex
    route_map.add_undirected_edge(vertices[1], vertices[3], 3.8)
    route_map.add_undirected_edge(vertices[2], vertices[3], 7.1)

    # add edge for 4th vertex
    route_map.add_undirected_edge(vertices[1], vertices[4], 11.0)
    route_map.add_undirected_edge(vertices[2], vertices[4], 6.4)
    route_map.add_undirected_edge(vertices[3], vertices[4], 9.2)

    # add edge for 5th vertex
    route_map.add_undirected_edge(vertices[1], vertices[5], 2.2)
    route_map.add_undirected_edge(vertices[2], vertices[5], 6.0)
    route_map.add_undirected_edge(vertices[3], vertices[5], 4.4)
    route_map.add_undirected_edge(vertices[4], vertices[5], 5.6)

    # add edge for 6th vertex
    route_map.add_undirected_edge(vertices[1], vertices[6], 3.5)
    route_map.add_undirected_edge(vertices[2], vertices[6], 4.8)
    route_map.add_undirected_edge(vertices[3], vertices[6], 2.8)
    route_map.add_undirected_edge(vertices[4], vertices[6], 6.9)
    route_map.add_undirected_edge(vertices[5], vertices[6], 1.9)

    # add edge for 7th vertex
    route_map.add_undirected_edge(vertices[1], vertices[7], 10.9)
    route_map.add_undirected_edge(vertices[2], vertices[7], 1.6)
    route_map.add_undirected_edge(vertices[3], vertices[7], 8.6)
    route_map.add_undirected_edge(vertices[4], vertices[7], 8.6)
    route_map.add_undirected_edge(vertices[5], vertices[7], 7.9)
    route_map.add_undirected_edge(vertices[6], vertices[7], 6.3)

    # add edge for 8th vertex
    route_map.add_undirected_edge(vertices[1], vertices[8], 8.6)
    route_map.add_undirected_edge(vertices[2], vertices[8], 2.8)
    route_map.add_undirected_edge(vertices[3], vertices[8], 6.3)
    route_map.add_undirected_edge(vertices[4], vertices[8], 4.0)
    route_map.add_undirected_edge(vertices[5], vertices[8], 5.1)
    route_map.add_undirected_edge(vertices[6], vertices[8], 4.3)
    route_map.add_undirected_edge(vertices[7], vertices[8], 4.0)

    # add edge for 9th vertex
    route_map.add_undirected_edge(vertices[1], vertices[9], 7.6)
    route_map.add_undirected_edge(vertices[2], vertices[9], 4.8)
    route_map.add_undirected_edge(vertices[3], vertices[9], 5.3)
    route_map.add_undirected_edge(vertices[4], vertices[9], 11.1)
    route_map.add_undirected_edge(vertices[5], vertices[9], 7.5)
    route_map.add_undirected_edge(vertices[6], vertices[9], 4.5)
    route_map.add_undirected_edge(vertices[7], vertices[9], 4.2)
    route_map.add_undirected_edge(vertices[8], vertices[9], 7.7)

    # add edge for 10th vertex
    route_map.add_undirected_edge(vertices[1], vertices[10], 2.8)
    route_map.add_undirected_edge(vertices[2], vertices[10], 6.3)
    route_map.add_undirected_edge(vertices[3], vertices[10], 1.6)
    route_map.add_undirected_edge(vertices[4], vertices[10], 7.3)
    route_map.add_undirected_edge(vertices[5], vertices[10], 2.6)
    route_map.add_undirected_edge(vertices[6], vertices[10], 1.5)
    route_map.add_undirected_edge(vertices[7], vertices[10], 8.0)
    route_map.add_undirected_edge(vertices[8], vertices[10], 9.3)
    route_map.add_undirected_edge(vertices[9], vertices[10], 4.8)

    # add edge for 11th vertex
    route_map.add_undirected_edge(vertices[1], vertices[11], 6.4)
    route_map.add_undirected_edge(vertices[2], vertices[11], 7.3)
    route_map.add_undirected_edge(vertices[3], vertices[11], 10.4)
    route_map.add_undirected_edge(vertices[4], vertices[11], 1.0)
    route_map.add_undirected_edge(vertices[5], vertices[11], 6.5)
    route_map.add_undirected_edge(vertices[6], vertices[11], 8.7)
    route_map.add_undirected_edge(vertices[7], vertices[11], 8.6)
    route_map.add_undirected_edge(vertices[8], vertices[11], 4.6)
    route_map.add_undirected_edge(vertices[9], vertices[11], 11.9)
    route_map.add_undirected_edge(vertices[10], vertices[11], 9.4)

    # add edge for 12th vertex
    route_map.add_undirected_edge(vertices[1], vertices[12], 3.2)
    route_map.add_undirected_edge(vertices[2], vertices[12], 5.3)
    route_map.add_undirected_edge(vertices[3], vertices[12], 3.0)
    route_map.add_undirected_edge(vertices[4], vertices[12], 6.4)
    route_map.add_undirected_edge(vertices[5], vertices[12], 1.5)
    route_map.add_undirected_edge(vertices[6], vertices[12], 0.8)
    route_map.add_undirected_edge(vertices[7], vertices[12], 6.9)
    route_map.add_undirected_edge(vertices[8], vertices[12], 4.8)
    route_map.add_undirected_edge(vertices[9], vertices[12], 4.7)
    route_map.add_undirected_edge(vertices[10], vertices[12], 1.1)
    route_map.add_undirected_edge(vertices[11], vertices[12], 7.3)

    # add edge for 13th vertex
    route_map.add_undirected_edge(vertices[1], vertices[13], 7.6)
    route_map.add_undirected_edge(vertices[2], vertices[13], 4.8)
    route_map.add_undirected_edge(vertices[3], vertices[13], 5.3)
    route_map.add_undirected_edge(vertices[4], vertices[13], 11.1)
    route_map.add_undirected_edge(vertices[5], vertices[13], 7.5)
    route_map.add_undirected_edge(vertices[6], vertices[13], 4.5)
    route_map.add_undirected_edge(vertices[7], vertices[13], 4.2)
    route_map.add_undirected_edge(vertices[8], vertices[13], 7.7)
    route_map.add_undirected_edge(vertices[9], vertices[13], 0.6)
    route_map.add_undirected_edge(vertices[10], vertices[13], 5.1)
    route_map.add_undirected_edge(vertices[11], vertices[13], 12.0)
    route_map.add_undirected_edge(vertices[12], vertices[13], 4.7)

    # add edge for 14th vertex
    route_map.add_undirected_edge(vertices[1], vertices[14], 5.2)
    route_map.add_undirected_edge(vertices[2], vertices[14], 3.0)
    route_map.add_undirected_edge(vertices[3], vertices[14], 6.5)
    route_map.add_undirected_edge(vertices[4], vertices[14], 3.9)
    route_map.add_undirected_edge(vertices[5], vertices[14], 3.2)
    route_map.add_undirected_edge(vertices[6], vertices[14], 3.9)
    route_map.add_undirected_edge(vertices[7], vertices[14], 4.2)
    route_map.add_undirected_edge(vertices[8], vertices[14], 1.6)
    route_map.add_undirected_edge(vertices[9], vertices[14], 7.6)
    route_map.add_undirected_edge(vertices[10], vertices[14], 4.6)
    route_map.add_undirected_edge(vertices[11], vertices[14], 4.9)
    route_map.add_undirected_edge(vertices[12], vertices[14], 3.5)
    route_map.add_undirected_edge(vertices[13], vertices[14], 7.3)

    # add edge for 15th vertex
    route_map.add_undirected_edge(vertices[1], vertices[15], 4.4)
    route_map.add_undirected_edge(vertices[2], vertices[15], 4.6)
    route_map.add_undirected_edge(vertices[3], vertices[15], 5.6)
    route_map.add_undirected_edge(vertices[4], vertices[15], 4.3)
    route_map.add_undirected_edge(vertices[5], vertices[15], 2.4)
    route_map.add_undirected_edge(vertices[6], vertices[15], 3.0)
    route_map.add_undirected_edge(vertices[7], vertices[15], 8.0)
    route_map.add_undirected_edge(vertices[8], vertices[15], 3.3)
    route_map.add_undirected_edge(vertices[9], vertices[15], 7.8)
    route_map.add_undirected_edge(vertices[10], vertices[15], 3.7)
    route_map.add_undirected_edge(vertices[11], vertices[15], 5.2)
    route_map.add_undirected_edge(vertices[12], vertices[15], 2.6)
    route_map.add_undirected_edge(vertices[13], vertices[15], 7.8)
    route_map.add_undirected_edge(vertices[14], vertices[15], 1.3)

    # add edge for 16th vertex
    route_map.add_undirected_edge(vertices[1], vertices[16], 3.7)
    route_map.add_undirected_edge(vertices[2], vertices[16], 4.5)
    route_map.add_undirected_edge(vertices[3], vertices[16], 5.8)
    route_map.add_undirected_edge(vertices[4], vertices[16], 4.4)
    route_map.add_undirected_edge(vertices[5], vertices[16], 2.7)
    route_map.add_undirected_edge(vertices[6], vertices[16], 3.8)
    route_map.add_undirected_edge(vertices[7], vertices[16], 5.8)
    route_map.add_undirected_edge(vertices[8], vertices[16], 3.4)
    route_map.add_undirected_edge(vertices[9], vertices[16], 6.6)
    route_map.add_undirected_edge(vertices[10], vertices[16], 4.0)
    route_map.add_undirected_edge(vertices[11], vertices[16], 5.4)
    route_map.add_undirected_edge(vertices[12], vertices[16], 2.9)
    route_map.add_undirected_edge(vertices[13], vertices[16], 6.6)
    route_map.add_undirected_edge(vertices[14], vertices[16], 1.5)
    route_map.add_undirected_edge(vertices[15], vertices[16], 0.6)

    # add edge for 17th vertex
    route_map.add_undirected_edge(vertices[1], vertices[17], 7.6)
    route_map.add_undirected_edge(vertices[2], vertices[17], 7.4)
    route_map.add_undirected_edge(vertices[3], vertices[17], 5.7)
    route_map.add_undirected_edge(vertices[4], vertices[17], 7.2)
    route_map.add_undirected_edge(vertices[5], vertices[17], 1.4)
    route_map.add_undirected_edge(vertices[6], vertices[17], 5.7)
    route_map.add_undirected_edge(vertices[7], vertices[17], 7.2)
    route_map.add_undirected_edge(vertices[8], vertices[17], 3.1)
    route_map.add_undirected_edge(vertices[9], vertices[17], 7.1)
    route_map.add_undirected_edge(vertices[10], vertices[17], 6.7)
    route_map.add_undirected_edge(vertices[11], vertices[17], 8.1)
    route_map.add_undirected_edge(vertices[12], vertices[17], 6.3)
    route_map.add_undirected_edge(vertices[13], vertices[17], 7.1)
    route_map.add_undirected_edge(vertices[14], vertices[17], 4.0)
    route_map.add_undirected_edge(vertices[15], vertices[17], 6.4)
    route_map.add_undirected_edge(vertices[16], vertices[17], 5.6)

    # add edge for 18th vertex
    route_map.add_undirected_edge(vertices[1], vertices[18], 2.0)
    route_map.add_undirected_edge(vertices[2], vertices[18], 6.0)
    route_map.add_undirected_edge(vertices[3], vertices[18], 4.1)
    route_map.add_undirected_edge(vertices[4], vertices[18], 5.3)
    route_map.add_undirected_edge(vertices[5], vertices[18], 0.5)
    route_map.add_undirected_edge(vertices[6], vertices[18], 1.9)
    route_map.add_undirected_edge(vertices[7], vertices[18], 7.7)
    route_map.add_undirected_edge(vertices[8], vertices[18], 5.1)
    route_map.add_undirected_edge(vertices[9], vertices[18], 5.9)
    route_map.add_undirected_edge(vertices[10], vertices[18], 2.3)
    route_map.add_undirected_edge(vertices[11], vertices[18], 6.2)
    route_map.add_undirected_edge(vertices[12], vertices[18], 1.2)
    route_map.add_undirected_edge(vertices[13], vertices[18], 5.9)
    route_map.add_undirected_edge(vertices[14], vertices[18], 3.2)
    route_map.add_undirected_edge(vertices[15], vertices[18], 2.4)
    route_map.add_undirected_edge(vertices[16], vertices[18], 1.6)
    route_map.add_undirected_edge(vertices[17], vertices[18], 7.1)

    # add edge for 19th vertex
    route_map.add_undirected_edge(vertices[1], vertices[19], 3.6)
    route_map.add_undirected_edge(vertices[2], vertices[19], 5.0)
    route_map.add_undirected_edge(vertices[3], vertices[19], 3.6)
    route_map.add_undirected_edge(vertices[4], vertices[19], 6.0)
    route_map.add_undirected_edge(vertices[5], vertices[19], 1.7)
    route_map.add_undirected_edge(vertices[6], vertices[19], 1.1)
    route_map.add_undirected_edge(vertices[7], vertices[19], 6.6)
    route_map.add_undirected_edge(vertices[8], vertices[19], 4.6)
    route_map.add_undirected_edge(vertices[9], vertices[19], 5.4)
    route_map.add_undirected_edge(vertices[10], vertices[19], 1.8)
    route_map.add_undirected_edge(vertices[11], vertices[19], 6.9)
    route_map.add_undirected_edge(vertices[12], vertices[19], 1.0)
    route_map.add_undirected_edge(vertices[13], vertices[19], 5.4)
    route_map.add_undirected_edge(vertices[14], vertices[19], 3.0)
    route_map.add_undirected_edge(vertices[15], vertices[19], 2.2)
    route_map.add_undirected_edge(vertices[16], vertices[19], 1.7)
    route_map.add_undirected_edge(vertices[17], vertices[19], 6.1)
    route_map.add_undirected_edge(vertices[18], vertices[19], 1.6)

    # add edge for 20th vertex
    route_map.add_undirected_edge(vertices[1], vertices[20], 6.5)
    route_map.add_undirected_edge(vertices[2], vertices[20], 4.8)
    route_map.add_undirected_edge(vertices[3], vertices[20], 4.3)
    route_map.add_undirected_edge(vertices[4], vertices[20], 10.6)
    route_map.add_undirected_edge(vertices[5], vertices[20], 6.5)
    route_map.add_undirected_edge(vertices[6], vertices[20], 3.5)
    route_map.add_undirected_edge(vertices[7], vertices[20], 3.2)
    route_map.add_undirected_edge(vertices[8], vertices[20], 6.7)
    route_map.add_undirected_edge(vertices[9], vertices[20], 1.0)
    route_map.add_undirected_edge(vertices[10], vertices[20], 4.1)
    route_map.add_undirected_edge(vertices[11], vertices[20], 11.5)
    route_map.add_undirected_edge(vertices[12], vertices[20], 3.7)
    route_map.add_undirected_edge(vertices[13], vertices[20], 1.0)
    route_map.add_undirected_edge(vertices[14], vertices[20], 6.9)
    route_map.add_undirected_edge(vertices[15], vertices[20], 6.8)
    route_map.add_undirected_edge(vertices[16], vertices[20], 6.4)
    route_map.add_undirected_edge(vertices[17], vertices[20], 7.2)
    route_map.add_undirected_edge(vertices[18], vertices[20], 4.9)
    route_map.add_undirected_edge(vertices[19], vertices[20], 4.4)

    # add edge for 21st vertex
    route_map.add_undirected_edge(vertices[1], vertices[21], 1.9)
    route_map.add_undirected_edge(vertices[2], vertices[21], 9.5)
    route_map.add_undirected_edge(vertices[3], vertices[21], 3.3)
    route_map.add_undirected_edge(vertices[4], vertices[21], 5.9)
    route_map.add_undirected_edge(vertices[5], vertices[21], 3.2)
    route_map.add_undirected_edge(vertices[6], vertices[21], 4.9)
    route_map.add_undirected_edge(vertices[7], vertices[21], 11.2)
    route_map.add_undirected_edge(vertices[8], vertices[21], 8.1)
    route_map.add_undirected_edge(vertices[9], vertices[21], 8.5)
    route_map.add_undirected_edge(vertices[10], vertices[21], 3.8)
    route_map.add_undirected_edge(vertices[11], vertices[21], 6.9)
    route_map.add_undirected_edge(vertices[12], vertices[21], 4.1)
    route_map.add_undirected_edge(vertices[13], vertices[21], 8.5)
    route_map.add_undirected_edge(vertices[14], vertices[21], 6.2)
    route_map.add_undirected_edge(vertices[15], vertices[21], 5.3)
    route_map.add_undirected_edge(vertices[16], vertices[21], 4.9)
    route_map.add_undirected_edge(vertices[17], vertices[21], 10.6)
    route_map.add_undirected_edge(vertices[18], vertices[21], 3.0)
    route_map.add_undirected_edge(vertices[19], vertices[21], 4.6)
    route_map.add_undirected_edge(vertices[20], vertices[21], 7.5)

    # add edge for 22nd vertex
    route_map.add_undirected_edge(vertices[1], vertices[22], 3.4)
    route_map.add_undirected_edge(vertices[2], vertices[22], 10.9)
    route_map.add_undirected_edge(vertices[3], vertices[22], 5.0)
    route_map.add_undirected_edge(vertices[4], vertices[22], 7.4)
    route_map.add_undirected_edge(vertices[5], vertices[22], 5.2)
    route_map.add_undirected_edge(vertices[6], vertices[22], 6.9)
    route_map.add_undirected_edge(vertices[7], vertices[22], 12.7)
    route_map.add_undirected_edge(vertices[8], vertices[22], 10.7)
    route_map.add_undirected_edge(vertices[9], vertices[22], 10.3)
    route_map.add_undirected_edge(vertices[10], vertices[22], 5.8)
    route_map.add_undirected_edge(vertices[11], vertices[22], 8.3)
    route_map.add_undirected_edge(vertices[12], vertices[22], 6.2)
    route_map.add_undirected_edge(vertices[13], vertices[22], 10.3)
    route_map.add_undirected_edge(vertices[14], vertices[22], 8.2)
    route_map.add_undirected_edge(vertices[15], vertices[22], 7.4)
    route_map.add_undirected_edge(vertices[16], vertices[22], 6.9)
    route_map.add_undirected_edge(vertices[17], vertices[22], 12.0)
    route_map.add_undirected_edge(vertices[18], vertices[22], 5.0)
    route_map.add_undirected_edge(vertices[19], vertices[22], 6.6)
    route_map.add_undirected_edge(vertices[20], vertices[22], 9.3)
    route_map.add_undirected_edge(vertices[21], vertices[22], 2.0)

    # add edge for 23rd vertex
    route_map.add_undirected_edge(vertices[1], vertices[23], 2.4)
    route_map.add_undirected_edge(vertices[2], vertices[23], 8.3)
    route_map.add_undirected_edge(vertices[3], vertices[23], 6.1)
    route_map.add_undirected_edge(vertices[4], vertices[23], 4.7)
    route_map.add_undirected_edge(vertices[5], vertices[23], 2.5)
    route_map.add_undirected_edge(vertices[6], vertices[23], 4.2)
    route_map.add_undirected_edge(vertices[7], vertices[23], 10.0)
    route_map.add_undirected_edge(vertices[8], vertices[23], 7.8)
    route_map.add_undirected_edge(vertices[9], vertices[23], 7.8)
    route_map.add_undirected_edge(vertices[10], vertices[23], 4.3)
    route_map.add_undirected_edge(vertices[11], vertices[23], 4.1)
    route_map.add_undirected_edge(vertices[12], vertices[23], 3.4)
    route_map.add_undirected_edge(vertices[13], vertices[23], 7.8)
    route_map.add_undirected_edge(vertices[14], vertices[23], 5.5)
    route_map.add_undirected_edge(vertices[15], vertices[23], 4.6)
    route_map.add_undirected_edge(vertices[16], vertices[23], 4.2)
    route_map.add_undirected_edge(vertices[17], vertices[23], 9.4)
    route_map.add_undirected_edge(vertices[18], vertices[23], 2.3)
    route_map.add_undirected_edge(vertices[19], vertices[23], 3.9)
    route_map.add_undirected_edge(vertices[20], vertices[23], 6.8)
    route_map.add_undirected_edge(vertices[21], vertices[23], 2.9)
    route_map.add_undirected_edge(vertices[22], vertices[23], 4.4)

    # add edge for 24th vertex
    route_map.add_undirected_edge(vertices[1], vertices[24], 6.4)
    route_map.add_undirected_edge(vertices[2], vertices[24], 6.9)
    route_map.add_undirected_edge(vertices[3], vertices[24], 9.7)
    route_map.add_undirected_edge(vertices[4], vertices[24], 0.6)
    route_map.add_undirected_edge(vertices[5], vertices[24], 6.0)
    route_map.add_undirected_edge(vertices[6], vertices[24], 9.0)
    route_map.add_undirected_edge(vertices[7], vertices[24], 8.2)
    route_map.add_undirected_edge(vertices[8], vertices[24], 4.2)
    route_map.add_undirected_edge(vertices[9], vertices[24], 11.5)
    route_map.add_undirected_edge(vertices[10], vertices[24], 7.8)
    route_map.add_undirected_edge(vertices[11], vertices[24], 0.4)
    route_map.add_undirected_edge(vertices[12], vertices[24], 6.9)
    route_map.add_undirected_edge(vertices[13], vertices[24], 11.5)
    route_map.add_undirected_edge(vertices[14], vertices[24], 4.4)
    route_map.add_undirected_edge(vertices[15], vertices[24], 4.8)
    route_map.add_undirected_edge(vertices[16], vertices[24], 5.6)
    route_map.add_undirected_edge(vertices[17], vertices[24], 7.5)
    route_map.add_undirected_edge(vertices[18], vertices[24], 5.5)
    route_map.add_undirected_edge(vertices[19], vertices[24], 6.5)
    route_map.add_undirected_edge(vertices[20], vertices[24], 11.4)
    route_map.add_undirected_edge(vertices[21], vertices[24], 6.4)
    route_map.add_undirected_edge(vertices[22], vertices[24], 7.9)
    route_map.add_undirected_edge(vertices[23], vertices[24], 4.5)

    # add edge for 25th vertex
    route_map.add_undirected_edge(vertices[1], vertices[25], 2.4)
    route_map.add_undirected_edge(vertices[2], vertices[25], 10.0)
    route_map.add_undirected_edge(vertices[3], vertices[25], 6.1)
    route_map.add_undirected_edge(vertices[4], vertices[25], 6.4)
    route_map.add_undirected_edge(vertices[5], vertices[25], 4.2)
    route_map.add_undirected_edge(vertices[6], vertices[25], 5.9)
    route_map.add_undirected_edge(vertices[7], vertices[25], 11.7)
    route_map.add_undirected_edge(vertices[8], vertices[25], 9.5)
    route_map.add_undirected_edge(vertices[9], vertices[25], 9.5)
    route_map.add_undirected_edge(vertices[10], vertices[25], 4.8)
    route_map.add_undirected_edge(vertices[11], vertices[25], 4.9)
    route_map.add_undirected_edge(vertices[12], vertices[25], 5.2)
    route_map.add_undirected_edge(vertices[13], vertices[25], 9.5)
    route_map.add_undirected_edge(vertices[14], vertices[25], 7.2)
    route_map.add_undirected_edge(vertices[15], vertices[25], 6.3)
    route_map.add_undirected_edge(vertices[16], vertices[25], 5.9)
    route_map.add_undirected_edge(vertices[17], vertices[25], 11.1)
    route_map.add_undirected_edge(vertices[18], vertices[25], 4.0)
    route_map.add_undirected_edge(vertices[19], vertices[25], 5.6)
    route_map.add_undirected_edge(vertices[20], vertices[25], 8.5)
    route_map.add_undirected_edge(vertices[21], vertices[25], 2.8)
    route_map.add_undirected_edge(vertices[22], vertices[25], 3.4)
    route_map.add_undirected_edge(vertices[23], vertices[25], 1.7)
    route_map.add_undirected_edge(vertices[24], vertices[25], 5.4)

    # add edge for 26th vertex
    route_map.add_undirected_edge(vertices[1], vertices[26], 5.0)
    route_map.add_undirected_edge(vertices[2], vertices[26], 4.4)
    route_map.add_undirected_edge(vertices[3], vertices[26], 2.8)
    route_map.add_undirected_edge(vertices[4], vertices[26], 10.1)
    route_map.add_undirected_edge(vertices[5], vertices[26], 5.4)
    route_map.add_undirected_edge(vertices[6], vertices[26], 3.5)
    route_map.add_undirected_edge(vertices[7], vertices[26], 5.1)
    route_map.add_undirected_edge(vertices[8], vertices[26], 6.2)
    route_map.add_undirected_edge(vertices[9], vertices[26], 2.8)
    route_map.add_undirected_edge(vertices[10], vertices[26], 3.2)
    route_map.add_undirected_edge(vertices[11], vertices[26], 11.0)
    route_map.add_undirected_edge(vertices[12], vertices[26], 3.7)
    route_map.add_undirected_edge(vertices[13], vertices[26], 2.8)
    route_map.add_undirected_edge(vertices[14], vertices[26], 6.4)
    route_map.add_undirected_edge(vertices[15], vertices[26], 6.5)
    route_map.add_undirected_edge(vertices[16], vertices[26], 5.7)
    route_map.add_undirected_edge(vertices[17], vertices[26], 6.2)
    route_map.add_undirected_edge(vertices[18], vertices[26], 5.1)
    route_map.add_undirected_edge(vertices[19], vertices[26], 4.3)
    route_map.add_undirected_edge(vertices[20], vertices[26], 1.8)
    route_map.add_undirected_edge(vertices[21], vertices[26], 6.0)
    route_map.add_undirected_edge(vertices[22], vertices[26], 7.9)
    route_map.add_undirected_edge(vertices[23], vertices[26], 6.8)
    route_map.add_undirected_edge(vertices[24], vertices[26], 10.6)
    route_map.add_undirected_edge(vertices[25], vertices[26], 7.0)

    # add edge for 27th vertex
    route_map.add_undirected_edge(vertices[1], vertices[27], 3.6)
    route_map.add_undirected_edge(vertices[2], vertices[27], 13.0)
    route_map.add_undirected_edge(vertices[3], vertices[27], 7.4)
    route_map.add_undirected_edge(vertices[4], vertices[27], 10.1)
    route_map.add_undirected_edge(vertices[5], vertices[27], 5.5)
    route_map.add_undirected_edge(vertices[6], vertices[27], 7.2)
    route_map.add_undirected_edge(vertices[7], vertices[27], 14.2)
    route_map.add_undirected_edge(vertices[8], vertices[27], 10.7)
    route_map.add_undirected_edge(vertices[9], vertices[27], 14.1)
    route_map.add_undirected_edge(vertices[10], vertices[27], 6.0)
    route_map.add_undirected_edge(vertices[11], vertices[27], 6.8)
    route_map.add_undirected_edge(vertices[12], vertices[27], 6.4)
    route_map.add_undirected_edge(vertices[13], vertices[27], 14.1)
    route_map.add_undirected_edge(vertices[14], vertices[27], 10.5)
    route_map.add_undirected_edge(vertices[15], vertices[27], 8.8)
    route_map.add_undirected_edge(vertices[16], vertices[27], 8.4)
    route_map.add_undirected_edge(vertices[17], vertices[27], 13.6)
    route_map.add_undirected_edge(vertices[18], vertices[27], 5.2)
    route_map.add_undirected_edge(vertices[19], vertices[27], 6.9)
    route_map.add_undirected_edge(vertices[20], vertices[27], 13.1)
    route_map.add_undirected_edge(vertices[21], vertices[27], 4.1)
    route_map.add_undirected_edge(vertices[22], vertices[27], 4.7)
    route_map.add_undirected_edge(vertices[23], vertices[27], 3.1)
    route_map.add_undirected_edge(vertices[24], vertices[27], 7.8)
    route_map.add_undirected_edge(vertices[25], vertices[27], 1.3)
    route_map.add_undirected_edge(vertices[26], vertices[27], 8.3)

    return route_map


def initialize_packages(vertices):
    package_list = {}
    package_list[1] = Package(1, vertices[6], time(hour=10, minute=30), 21, None, time(hour=8), "unloaded")
    package_list[2] = Package(2, vertices[10], None, 44, None, time(hour=8), "unloaded")
    package_list[3] = Package(3, vertices[9], None, 2, 2, time(hour=8), "unloaded")
    package_list[4] = Package(4, vertices[19], None, 4, None, time(hour=8), "unloaded")
    package_list[5] = Package(5, vertices[20], None, 5, None, time(hour=8), "unloaded")
    package_list[6] = Package(6, vertices[14], time(hour=10, minute=30), 88, None, time(hour=9, minute=5), "unloaded")
    package_list[7] = Package(7, vertices[3], None, 8, None, time(hour=8), "unloaded")
    package_list[8] = Package(8, vertices[13], None, 9, None, time(hour=8), "unloaded")
    package_list[9] = Package(9, vertices[13], None, 2, None, time(hour=8), "unloaded")
    package_list[10] = Package(10, vertices[26], None, 1, None, time(hour=8), "unloaded")
    package_list[11] = Package(11, vertices[11], None, 1, None, time(hour=8), "unloaded")
    package_list[12] = Package(12, vertices[17], None, 1, None, time(hour=8), "unloaded")
    package_list[13] = Package(13, vertices[7], time(hour=10, minute=30), 2, None, time(hour=8), "unloaded")
    package_list[14] = Package(14, vertices[21], time(hour=10, minute=30), 88, None, time(hour=8), "unloaded")
    package_list[15] = Package(15, vertices[22], time(hour=9), 4, None, time(hour=8), "unloaded")
    package_list[16] = Package(16, vertices[22], time(hour=10, minute=30), 88, None, time(hour=8), "unloaded")
    package_list[17] = Package(17, vertices[15], None, 2, None, time(hour=8), "unloaded")
    package_list[18] = Package(18, vertices[4], None, 6, 2, time(hour=8), "unloaded")
    package_list[19] = Package(19, vertices[5], None, 37, None, time(hour=8), "unloaded")
    package_list[20] = Package(20, vertices[18], time(hour=10, minute=30), 37, None, time(hour=8), "unloaded")
    package_list[21] = Package(21, vertices[18], None, 3, None, time(hour=8), "unloaded")
    package_list[22] = Package(22, vertices[27], None, 2, None, time(hour=8), "unloaded")
    package_list[23] = Package(23, vertices[24], None, 5, None, time(hour=8), "unloaded")
    package_list[24] = Package(24, vertices[23], None, 7, None, time(hour=8), "unloaded")
    package_list[25] = Package(25, vertices[25], time(hour=10, minute=30), 7, None, time(hour=9, minute=5), "unloaded")
    package_list[26] = Package(26, vertices[25], None, 25, None, time(hour=8), "unloaded")
    package_list[27] = Package(27, vertices[2], None, 5, None, time(hour=8), "unloaded")
    package_list[28] = Package(28, vertices[12], None, 7, None, time(hour=9, minute=5), "unloaded")
    package_list[29] = Package(29, vertices[3], time(hour=10, minute=30), 2, None, time(hour=8), "unloaded")
    package_list[30] = Package(30, vertices[13], None, 1, None, time(hour=8), "unloaded")
    package_list[31] = Package(31, vertices[16], time(hour=10, minute=30), 1, None, time(hour=8), "unloaded")
    package_list[32] = Package(32, vertices[16], None, 1, None, time(hour=9, minute=5), "unloaded")
    package_list[33] = Package(33, vertices[10], None, 1, None, time(hour=8), "unloaded")
    package_list[34] = Package(34, vertices[22], time(hour=10, minute=30), 2, None, time(hour=8), "unloaded")
    package_list[35] = Package(35, vertices[2], None, 88, None, time(hour=9, minute=5), "unloaded")
    package_list[36] = Package(36, vertices[8], None, 88, 2, time(hour=8), "unloaded")
    package_list[37] = Package(37, vertices[20], time(hour=10, minute=30), 2, None, time(hour=8), "unloaded")
    package_list[38] = Package(38, vertices[20], None, 9, 2, time(hour=8), "unloaded")
    package_list[39] = Package(39, vertices[7], None, 9, None, time(hour=8), "unloaded")
    package_list[40] = Package(40, vertices[19], time(hour=10, minute=30), 45, None, time(hour=8), "unloaded")

    return package_list


def initialize_package(package_list):
    # Create custom hash table and add packages using direct mapping for keys
    package_table = DirectHashTable()
    package_table.put(1, package_list[1])
    package_table.put(2, package_list[2])
    package_table.put(3, package_list[3])
    package_table.put(4, package_list[4])
    package_table.put(5, package_list[5])
    package_table.put(6, package_list[6])
    package_table.put(7, package_list[7])
    package_table.put(8, package_list[8])
    package_table.put(9, package_list[9])
    package_table.put(10, package_list[10])
    package_table.put(11, package_list[11])
    package_table.put(12, package_list[12])
    package_table.put(13, package_list[13])
    package_table.put(14, package_list[14])
    package_table.put(15, package_list[15])
    package_table.put(16, package_list[16])
    package_table.put(17, package_list[17])
    package_table.put(18, package_list[18])
    package_table.put(19, package_list[19])
    package_table.put(20, package_list[20])
    package_table.put(21, package_list[21])
    package_table.put(22, package_list[22])
    package_table.put(23, package_list[23])
    package_table.put(24, package_list[24])
    package_table.put(25, package_list[25])
    package_table.put(26, package_list[26])
    package_table.put(27, package_list[27])
    package_table.put(28, package_list[28])
    package_table.put(29, package_list[29])
    package_table.put(30, package_list[30])
    package_table.put(31, package_list[31])
    package_table.put(32, package_list[32])
    package_table.put(33, package_list[33])
    package_table.put(34, package_list[34])
    package_table.put(35, package_list[35])
    package_table.put(36, package_list[36])
    package_table.put(37, package_list[37])
    package_table.put(38, package_list[38])
    package_table.put(39, package_list[39])
    package_table.put(40, package_list[40])

    return package_table


def associate_packages(package_list):
    # creates a graph to track the relationships of packages
    package_associations = Graph()

    # have to add all vertices to have adjacency list, future-proofing
    package_associations.add_vertex(package_list[1])
    package_associations.add_vertex(package_list[2])
    package_associations.add_vertex(package_list[3])
    package_associations.add_vertex(package_list[4])
    package_associations.add_vertex(package_list[5])
    package_associations.add_vertex(package_list[6])
    package_associations.add_vertex(package_list[7])
    package_associations.add_vertex(package_list[8])
    package_associations.add_vertex(package_list[9])
    package_associations.add_vertex(package_list[10])
    package_associations.add_vertex(package_list[11])
    package_associations.add_vertex(package_list[12])
    package_associations.add_vertex(package_list[13])
    package_associations.add_vertex(package_list[14])
    package_associations.add_vertex(package_list[15])
    package_associations.add_vertex(package_list[16])
    package_associations.add_vertex(package_list[17])
    package_associations.add_vertex(package_list[18])
    package_associations.add_vertex(package_list[19])
    package_associations.add_vertex(package_list[20])
    package_associations.add_vertex(package_list[21])
    package_associations.add_vertex(package_list[22])
    package_associations.add_vertex(package_list[23])
    package_associations.add_vertex(package_list[24])
    package_associations.add_vertex(package_list[25])
    package_associations.add_vertex(package_list[26])
    package_associations.add_vertex(package_list[27])
    package_associations.add_vertex(package_list[28])
    package_associations.add_vertex(package_list[29])
    package_associations.add_vertex(package_list[30])
    package_associations.add_vertex(package_list[31])
    package_associations.add_vertex(package_list[32])
    package_associations.add_vertex(package_list[33])
    package_associations.add_vertex(package_list[34])
    package_associations.add_vertex(package_list[35])
    package_associations.add_vertex(package_list[36])
    package_associations.add_vertex(package_list[37])
    package_associations.add_vertex(package_list[38])
    package_associations.add_vertex(package_list[39])
    package_associations.add_vertex(package_list[40])

    package_associations.add_undirected_edge(package_list[14], package_list[15])
    package_associations.add_undirected_edge(package_list[14], package_list[19])
    package_associations.add_undirected_edge(package_list[16], package_list[13])
    package_associations.add_undirected_edge(package_list[16], package_list[19])
    package_associations.add_undirected_edge(package_list[20], package_list[13])
    package_associations.add_undirected_edge(package_list[20], package_list[15])

    return package_associations


# a dfs search for the packages to see what other packages are connected to them
def get_connected_packages(package_associations, start_vertex):
    connected_packages = []
    remaining_packages = [start_vertex]

    while remaining_packages:
        package = remaining_packages.pop()
        if not connected_packages.__contains__(package):
            connected_packages.append(package)
            for vertex in package_associations.adjacency_list[package]:
                remaining_packages.append(vertex)

    return connected_packages


# set number of trucks so we can assume first one is ID = 1, 2nd is ID = 2 and 3rd is ID = 3
def initialize_trucks(vertices):
    truck_list = [Truck(1, vertices[1]), Truck(2, vertices[1]), Truck(3, vertices[1])]
    return truck_list


# loads truck with packages that have deadlines, associated packages, and specific truck numbers
def load_deadline_packages(truck_list, package_list, package_associations, current_time):
    for p in package_list:
        package = package_list[p]
        if package.deliver_by is not None and at_hub(package, current_time) and package.status == "unloaded":
            truck_number = unfilled_truck(truck_list)
            if package.truck_number is not None:
                truck_number = package.truck_number

            # if there are other packages associated with this package, load them all
            connected_packages = get_connected_packages(package_associations, package)
            if connected_packages.__len__() < truck_list[truck_number-1].get_available_slots():
                for pack in connected_packages:
                    load_to_specific_truck(truck_list, truck_number, pack)


# loads truck with packages that have deadlines and specific truck numbers
def load_specific_deadline_packages(truck_list, package_list, current_time):
    for p in package_list:
        package = package_list[p]
        if package.deliver_by is not None and at_hub(package, current_time) and package.status == "unloaded":
            truck_number = unfilled_truck(truck_list)
            if package.truck_number is not None:
                truck_number = package.truck_number
            load_to_specific_truck(truck_list, truck_number, package)


# loads truck with packages that have deadlines only
def load_only_deadline_packages(truck_list, package_list, current_time):
    for p in package_list:
        package = package_list[p]
        if package.deliver_by is not None and at_hub(package, current_time) and package.status == "unloaded":
            truck_number = unfilled_truck(truck_list)
            load_to_specific_truck(truck_list, truck_number, package)


# loads truck with packages that have associated packages only
def load_only_associated_packages(truck_list, package_list, package_associations, current_time):
    for p in package_list:
        package = package_list[p]
        if at_hub(package, current_time) and package.status == "unloaded":
            truck_number = unfilled_truck(truck_list)
            if package.truck_number is not None:
                truck_number = package.truck_number

            # if there are other packages associated with this package, load them all
            connected_packages = get_connected_packages(package_associations, package)
            if connected_packages.__len__() > truck_list[truck_number-1].get_available_slots():
                truck_number = switch_trucks(truck_number)
            if 1 < connected_packages.__len__() < truck_list[truck_number-1].get_available_slots():
                for pack in connected_packages:
                    load_to_specific_truck(truck_list, truck_number, pack)


# loads only packages that want a specific truck
def load_packages_to_specific_truck(truck_list, package_list, current_time):
    for p in package_list:
        package = package_list[p]
        truck_number = package.truck_number
        if truck_number is not None and package.status == "unloaded" and at_hub(package, current_time):
            load_to_specific_truck(truck_list, truck_number, package)


# loads the remaining packages
def load_remaining_packages(truck_list, package_list, current_time):
    for p in package_list:
        package = package_list[p]
        truck_number = unfilled_truck(truck_list)
        if truck_number is not None and package.status == "unloaded" and at_hub(package, current_time):
            load_to_specific_truck(truck_list, truck_number, package)


# loads to a specific truck
def load_to_specific_truck(truck_list, truck_number, package):
    return truck_list[truck_number - 1].load_package(package)


# finds the unfilled truck
def unfilled_truck(truck_list):
    if truck_list[0].package_count == 16:
        return 2
    return 1


# switches trucks
def switch_trucks(truck_number):
    if truck_number == 1:
        return 2
    return 1


# figure out if all trucks are filled
def trucks_ready(truck_list, package_list, current_time):
    return (truck_list[1].count == 16 and truck_list[1].count == 16) or all_packages_loaded(package_list, current_time)


# returns if the package is at the hub
def at_hub(package, current_time):
    return current_time.time() >= package.depot_time


# see if all packages have been loaded
def all_packages_loaded(package_list, current_time):
    for p in package_list:
        package = package_list(p)
        if at_hub(package, current_time) and package.status is "unloaded":
            return False
    return True


# loads the trucks by taking into account the packages left that are unloaded and which trucks are empty
def load_trucks(truck_list, package_list, package_associations, current_time):
    # loads packages that have both a deadline and are associated with other packages
    load_deadline_packages(truck_list, package_list, package_associations, current_time)
    load_specific_deadline_packages(truck_list, package_list, current_time)
    load_only_deadline_packages(truck_list, package_list, current_time)
    load_only_associated_packages(truck_list, package_list, package_associations, current_time)
    load_packages_to_specific_truck(truck_list, package_list, current_time)
    load_remaining_packages(truck_list, package_list, current_time)


# assumes everything will be delivered by midnight
# get status also runs the delivery up until the time given
def get_status(truck_list, route_map, input_time, package_list, package_associations, vertices):
    status_time = datetime.combine(date.today(), input_time)
    current_time = datetime.combine(date.today(), time(hour=8, minute=1))

    # only two trucks can be used since there are only two drivers
    truck_1 = truck_list[0]
    truck_2 = truck_list[1]

    # while the time is not equal to the time at the inquiry of status, increment time and drive
    while status_time > current_time:
        # if time is 10:20 fix the address of package 9
        if current_time.time() == time(hour=10, minute=20):
            adjust_address(package_list[9], vertices[20])

        # sends the trucks out to deliver the package
        truck_1.deliver_package(route_map, current_time.time())
        truck_2.deliver_package(route_map, current_time.time())

        # finds any empty trucks and reloads the packages
        empty_trucks = []
        if truck_1.packages.__len__() == 0:
            empty_trucks.append(truck_1)
        if truck_2.packages.__len__() == 0:
            empty_trucks.append(truck_2)

        # loads truck if there are empty trucks
        if empty_trucks:
            load_trucks(empty_trucks, package_list, package_associations, current_time)

        current_time = current_time + timedelta(minutes=1)


# adjusts the package address at 10:20 AM
def adjust_address(package, destination):
    package.destination = destination
    package.status = "in delivery"


# calculates the packages delivered on time and also total distance
def show_delivery_stats(truck_list, package_list):
    # calculates the packages delivered
    total_packages_delivered = 0
    for p in package_list:
        if package_list[p].status[:13] == "delivered at ":
            total_packages_delivered += 1

    # calculates the total distance traveled
    total_distance_traveled = 0.0
    for truck in truck_list:
        total_distance_traveled += truck.distance_traveled

    print("Packages delivered on time: " + str(total_packages_delivered))
    print("Total miles traveled between all trucks: " + str(round(total_distance_traveled, 2)))


# prints all details from the packages in the package list
def print_package_details(package_list):
    print("Package Details:")
    for p in package_list:
        print("ID: " + str(package_list[p].id) + ", destination:  " + package_list[p].destination.address)
        print("weight: " + str(package_list[p].weight) + ", Deliver by: " + str(package_list[p].deliver_by) +
              ", status: " + package_list[p].status)


# gets the time from the user
def get_hour():
    while True:
        print("Insert time")
        input_hour = int(input("hour (8-23): "))
        if 8 <= input_hour < 24:
            return input_hour


# gets the minutes from the user
def get_minute():
    while True:
        print("Insert time")
        input_minute = int(input("minute(0-59): "))
        if 0 <= input_minute < 60:
            return input_minute


# gets the package id from the user
def get_id():
    while True:
        print("Package ID: ")
        input_id = int(input("ID (number): "))

        # makes sure the input is an integer
        if isinstance(input_id, int):
            return input_id


# the main program, this is what runs at the start of the program
def main():

    # unless the user chooses quit, show them a menu
    while True:
        # initialize everything
        location_list = initialize_locations()
        vertices = initialize_vertices(location_list)
        route_map = initialize_map(vertices)
        package_list = initialize_packages(vertices)
        package_table = initialize_package(package_list)
        package_associations = associate_packages(package_list)
        truck_list = initialize_trucks(vertices)

        # sets the current time to the start of the day
        current_time = datetime.combine(date.today(), time(hour=8))

        load_trucks(truck_list, package_list, package_associations, current_time)

        # starts the menu
        print("1) Get status - All Packages")
        print("2) Get status by ID")
        print("3) Quit")

        menu_option = input("Menu option (numbers only): ")

        # depending on the input, gets the status of the package
        if menu_option == "1":
            get_status(truck_list, route_map, time(hour=get_hour(), minute=get_minute()), package_list,
                       package_associations, vertices)
            print_package_details(package_list)
            show_delivery_stats(truck_list, package_list)
        if menu_option == "2":
            get_status(truck_list, route_map, time(hour=get_hour(), minute=get_minute()), package_list,
                       package_associations, vertices)
            input_id = get_id()
            if package_table.get(input_id):
                specific_package = {}
                specific_package[1] = package_table.get(input_id)
                print_package_details(specific_package)
            else:
                print("Not a valid ID")
        if menu_option == "3":
            break



main()
