import collections


def topologicalSort(graph, fout):
    graph.reset()
    topologicalNum = 0

    Q = collections.deque()
    for vertex in graph.vertices:
        if vertex.indegree == 0:
            Q.append(vertex)
            vertex.status = "Added to Queue"

    number = 1
    fout.write("The topological sort of the first graph is:\nVERTEX\tNUMBER\n")
    while len(Q) > 0:
        vertex = Q.popleft()
        topologicalNum += 1
        message = vertex.name + "\t\t" + str(number) + "\n"
        fout.write(message)
        number += 1
        vertex.status = "Visited"

        for neighbour in vertex.adjVertices:
            if neighbour.status is None:
                neighbour.indegree -= 1
                if neighbour.indegree == 0:
                    Q.append(neighbour)
                    neighbour.status = "Added to queue"

    if topologicalNum != graph.vertexCount:
        fout.write("There was a cycle!")
    else:
        fout.write("\n")
