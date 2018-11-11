import header
INP_FILE = "../graphs/graph_articulation_points_graph5.dat"


def findArticulationPoints(graph, v):
    try:
        findArticulationPoints.counter += 1
    except AttributeError:
        findArticulationPoints.counter = 1
        graph.reset()
        childrenOfRoot = 0
        print("Source is", v.name)

    v.dfsNum = v.low = findArticulationPoints.counter
    v.status = "Visited"

    for w in v.adjVertices:
        if w.status != "Visited":
            if v.dfsNum == 1:           # if it is the root..
                childrenOfRoot += 1     # .. then increment the count of children of root.
            w.parent = v
            findArticulationPoints(graph, w)

            if v.dfsNum != 1 and w.low >= v.dfsNum and v.colour != "Printed":
                print(v.name, "is an articulation point")
                v.colour = "Printed"
            v.low = min(v.low, w.low)

        elif v.parent != w:
            v.low = min(v.low, w.dfsNum)

    if v.dfsNum == 1 and childrenOfRoot > 1:
        print(v.name, "is an articulation point")


fin = open(INP_FILE, "r")
NUMBER_OF_VERTICES= int(fin.readline().split()[0])
g = header.Graph(fin, NUMBER_OF_VERTICES)
g.displayVertices()
source = g.vertices[int(fin.readline().split()[0]) - 1]
findArticulationPoints(g, source)
fin.close()