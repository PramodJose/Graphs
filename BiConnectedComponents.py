import header
INP_FILE = "graph_articulation_points.dat"
NUMBER_OF_VERTICES = 7


def findBiConnectedComponents(graph, v):
    try:
        findBiConnectedComponents.counter += 1
    except AttributeError:
        findBiConnectedComponents.counter = 1
        findBiConnectedComponents.componentNum = 1
        print("The Bi-Connected components are:-\nComponent 1:")
        graph.reset()

    v.status = "Visited"
    v.dfsNum = v.low = findBiConnectedComponents.counter

    for w in v.adjVertices:
        if w.status != "Visited":
            w.parent = v
            findBiConnectedComponents(graph, w)

            if w.low >= v.dfsNum and v.colour != "Black":       # v is an articulation point
                print(v.name)
                findBiConnectedComponents.componentNum += 1
                print("Component", findBiConnectedComponents.componentNum)
                print(v.name, "", end="")
                v.colour = "Black"

        elif v.parent != w:
            v.low = min(v.low, w.dfsNum)

    if v.colour != "Black":
        print(v.name, "", end="")


fin = open(INP_FILE, "r")
g = header.Graph(fin, NUMBER_OF_VERTICES)
g.displayVertices()
findBiConnectedComponents(g, g.vertices[3])
fin.close()
