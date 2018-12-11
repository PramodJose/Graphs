import header
import collections
INP_FILE = "../graphs/graph_bipartite.dat"


def is_bipartite(source):
    Q = collections.deque()
    Q.append(source)
    source.bipartite_set = 1
    source.status = "Added to Queue"

    while len(Q) > 0:
        vertex = Q.popleft()
        vertex.status = "Visited"
        print(vertex.name, " - ", vertex.bipartite_set)

        for neighbour in vertex.adjVertices:
            if neighbour.status is None:
                neighbour.bipartite_set = 3 - vertex.bipartite_set
                neighbour.status = "Added to Queue"
                Q.append(neighbour)
            elif neighbour.bipartite_set != 3 - vertex.bipartite_set:
                return False

    return True


fin = open(INP_FILE, "r")
NUMBER_OF_VERTICES= int(fin.readline().split()[0])
g = header.Graph(fin, NUMBER_OF_VERTICES)
g.displayVertices()
print(is_bipartite(g.vertices[0]))
fin.close()
