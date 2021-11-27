# Python Implementation for Minimum Spanning Tree using Prim's Algorithm
# Author: Joachim Wambua

def prims_algorithm(vertices, graph):
    # Initialise array to hold vertices selected in the MST set
    selectedVertex = [0 for vertex in range(0, vertices)]
    max_minimum = 1000000
    # Initialising the Prim's algorithm's starting vertex to index 0
    selectedVertex[0] = True

    #  Prim's Algorithm logic
    while 0 in selectedVertex:
        # Set minimum to maximum value
        minimum = max_minimum
        # Initialise 1st & last vertices with an edge in between
        first_vertex = 0
        last_vertex = 0
        # Looping through the vertices
        for node in range(vertices):
            # If current vertex is in the reached set of vertices...
            if selectedVertex[node]:
                # Then loop through the adjacent vertices to find edge with minimum weight
                for node1 in range(vertices):
                    # Checks if current vertex is not in the MST set & is part of the overall graph
                    if (not selectedVertex[node1]) and graph[node][node1] > 0:
                        # If True, Check if weight on current edge(between node1&2) is less than the current minimum
                        if graph[node][node1] < minimum:
                            # If True, Set new minimum weight
                            minimum = graph[node][node1]
                            first_vertex = node
                            last_vertex = node1
        # Print the adjacent edge with the least weight selected for the MST
        print(str(first_vertex) + ' ---- ' + str(last_vertex) + '  =  ' + str(graph[first_vertex][last_vertex]))
        # Add the latest vertex to the MST array
        selectedVertex[last_vertex] = True
    print()


if __name__ == "__main__":
    # Initialise Test Graph
    test_graph = [[0, 28, 0, 0, 0, 10, 0],
                  [28, 0, 16, 0, 0, 0, 14],
                  [0, 16, 0, 12, 0, 0, 0],
                  [0, 0, 12, 0, 22, 0, 18],
                  [0, 0, 0, 22, 0, 25, 24],
                  [10, 0, 0, 0, 25, 0, 0],
                  [0, 14, 0, 18, 24, 0, 0]]
    print('Selected Edge: Weight')
    # Testing the Prim's MST Function
    prims_algorithm(7, test_graph)
