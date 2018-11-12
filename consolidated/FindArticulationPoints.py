import header
INP_FILE = "../graphs/graph_articulation_points_graph5.dat"


def findArticulationPoints(graph, v, fout):
    try:
        findArticulationPoints.counter += 1
    except (AttributeError, TypeError):
        findArticulationPoints.counter = 1
        graph.reset()
        childrenOfRoot = 0

    v.dfsNum = v.low = findArticulationPoints.counter
    v.status = "Visited"

    for w in v.adjVertices:
        if w.status != "Visited":
            if v.dfsNum == 1:           # if it is the root..
                childrenOfRoot += 1     # .. then increment the count of children of root.
            w.parent = v
            findArticulationPoints(graph, w, fout)

            if v.dfsNum != 1 and w.low >= v.dfsNum and v.colour != "Printed":
                fout.write(v.name + "\n")
                v.colour = "Printed"
            v.low = min(v.low, w.low)

        elif v.parent != w:
            v.low = min(v.low, w.dfsNum)

    if v.dfsNum == 1 and childrenOfRoot > 1:
        fout.write(v.name + " (root of the dfs tree)")

    if v.dfsNum == 1:
        fout.write("\n\n")
