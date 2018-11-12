# This piece of source code has been inspired by Padhmamala ma'am's notes and geeksforgeeks.org.
# Link: https://www.geeksforgeeks.org/strongly-connected-components/
# Status of this code: Rough; works on all inputs, but still need to clean it and add comments.
import collections


def createDFSStack(graph, v, stack):
    try:
        createDFSStack.count += 1
    except AttributeError:
        createDFSStack.count = 0

    v.dfsNum = createDFSStack.count
    v.status = "Visited"

    for neighbour in v.adjVertices:
        if neighbour.status != "Visited":
            createDFSStack(graph, neighbour, stack)

    stack.append(v)

    if v.dfsNum == 0:
        for vertex in graph.vertices:
            if vertex.status != "Visited":  # if any of the nodes have not yet been visited, then run DFS on them..
                createDFSStack(graph, vertex, stack)


def basicDFS(graph, v, fout):
    v.status = "Visited"
    fout.write(v.name + " ")
    for neighbour in v.adjVertices:
        if neighbour.status != "Visited":
            basicDFS(graph, neighbour, fout)


def findSSCs(graph, stack, fout):
    while len(stack) != 0:
        v = stack.pop()
        if v.status != "Visited":
            fout.write("{")
            basicDFS(graph, v, fout)
            fout.write("}\t")


def SSCDriver(graph, fout):
    stack = collections.deque()
    createDFSStack(graph, graph.vertices[0], stack)
    graph.revGraph()
    findSSCs(graph, stack, fout)
