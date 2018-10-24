import header
INP_FILE = "graph_qsample.dat"


def DFS(graph, source):
    try:
        DFS.counter += 1
    except AttributeError:
        DFS.counter = 1
        DFS.dfsTreeNum = 1
        graph.reset()
        print("DFS Tree number 1")

    source.dfsNum = DFS.counter
    source.status = "Visited"
    print(source.name, "  ", end="")

    for neighbour in source.adjVertices:
        if neighbour.status != "Visited":
            DFS(graph, neighbour)

    if source.dfsNum == 1:
        for vertex in graph.vertices:
            if vertex.status != "Visited":
                DFS.dfsTreeNum += 1
                print("\nDFS Tree number", DFS.dfsTreeNum)
                DFS(graph, vertex)
        print()


fin = open(INP_FILE, "r")
g = header.Graph(fin, 7)
g.displayVertices()
DFS(g, g.vertices[4])
fin.close()
