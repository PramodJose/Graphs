import heapq
import header


def graphToHeap(graph):                     # This function creates a min heap out of the edges of a graph
    edgesHeap = list(graph.edges.values())  # create a list (array) of all the Edge objects of a graph
    heapq.heapify(edgesHeap)                # create a min heap of the edges (the same array is used to store the heap)..
    return edgesHeap                        # ..and return it


def kruskal(graph, fout):                   # This function
    uf = header.UnionFind(graph.vertexCount)    # the union find object...
    edgesHeap = graphToHeap(graph)              # a heap of all the edges
    edgesAccepted = 0
    cost = 0

    fout.write("The edges in the minimum spanning tree for the third graph are:\n")
    while edgesAccepted < graph.vertexCount - 1:
        minEdge = heapq.heappop(edgesHeap)

        if not uf.connected(minEdge.src.number, minEdge.dest.number):
            uf.unify(minEdge.src.number, minEdge.dest.number)
            fout.write("(" + minEdge.src.name + ", " + minEdge.dest.name + ", " + str(minEdge.weight) + ")\n")
            cost += minEdge.weight
            edgesAccepted += 1

    fout.write("Its cost is " + str(cost) + "\n\n")
