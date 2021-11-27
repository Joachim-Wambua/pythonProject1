# Python Implementation for Minimum Spanning Tree using Prim's Algorithm
# Author:
def prims_algorithm(vertices, graph):
    # Matrix to hold MST(Minimum Spanning Tree)
    mstMatrix = [[0 for column in range(vertices)] for row in range(vertices)]
    # Initialise array to hold vertices in MST set
    selectedVertices = [0 for vertex in range(0, vertices)]
    positiveInfinity = 1000000
    edges = 0
    selectedVertices[0] = True
    # Prims Algorithm logic
    while edges < vertices - 1:
        minimum = positiveInfinity
        first_vertex = 0
        last_vertex = 0
        for node in range(vertices):
            if selectedVertices[node]:
                for node1 in range(vertices):
                    if (not selectedVertices[node1]) and graph[node][node1] > 0:
                        if graph[node][node1] < minimum:
                            # Set new minimum weight
                            minimum = graph[node][node1]
                            first_vertex = node
                            last_vertex = node1
        print(str(first_vertex) + ' ---- ' + str(last_vertex) + '  =  ' + str(graph[first_vertex][last_vertex]))
        selectedVertices[last_vertex] = True
        edges += 1
        mstMatrix[first_vertex][last_vertex] = minimum

        if minimum == positiveInfinity:
            mstMatrix[first_vertex][last_vertex] = 0
            mstMatrix[first_vertex][last_vertex] = mstMatrix[last_vertex][first_vertex]
            print()
    print()
    print('MST Adjacency Matrix:')
    print(mstMatrix)


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
