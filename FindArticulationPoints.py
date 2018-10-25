import header
INP_FILE = "graph_articulation_points.dat"
NUMBER_OF_VERTICES = 7


def findArticulationPoints(graph, v):
    try:
        findArticulationPoints.counter += 1
    except AttributeError:
        findArticulationPoints.counter = 1
        graph.reset()

    v.dfsNum = v.low = findArticulationPoints.counter
    v.status = "Visited"

    for w in v.adjVertices:
        if w.status != "Visited":
            w.parent = v
            w.low = v.dfsNum
            findArticulationPoints(graph, w)
            if w.low >= v.dfsNum and v.colour != "Black":
                print(v.name, "is an articulation point")
                v.colour = "Black"
            v.low = min(v.low, w.low)
        elif v.parent != w:
            v.low = min(v.low, w.dfsNum)


fin = open(INP_FILE, "r")
g = header.Graph(fin, NUMBER_OF_VERTICES)
g.displayVertices()
findArticulationPoints(g, g.vertices[0])
fin.close()