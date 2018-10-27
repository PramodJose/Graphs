import header
INP_FILE = "graph_articulation_points.dat"


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
            findArticulationPoints(graph, w)

            if w.low >= v.dfsNum and v.colour != "Printed":
                print(v.name, "is an articulation point")
                v.colour = "Printed"
            v.low = min(v.low, w.low)

        elif v.parent != w:
            v.low = min(v.low, w.dfsNum)


fin = open(INP_FILE, "r")
NUMBER_OF_VERTICES= int(fin.readline().split()[0])
g = header.Graph(fin, NUMBER_OF_VERTICES)
g.displayVertices()
findArticulationPoints(g, g.vertices[0])
fin.close()