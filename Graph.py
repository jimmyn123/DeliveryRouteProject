# Jimmy Nguyen
# Student ID: 000579757


# a graph class that contains vertices and their connections
class Graph:

    # constructor that creates a new list for adjacency and weight
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    # adds a new vertex
    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    # adds an edge in one direction
    def add_directed_edge(self, start_vert, end_vert, weight=1.0):
        self.edge_weights[(start_vert, end_vert)] = weight
        self.adjacency_list[start_vert].append(end_vert)

    # adds two edges by using the one edge function
    def add_undirected_edge(self, vert_a, vert_b, weight=1.0):
        self.add_directed_edge(vert_a, vert_b, weight)
        self.add_directed_edge(vert_b, vert_a, weight)
