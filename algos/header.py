class Vertex:
    count = 0

    def __init__(self):
        self.name = chr(ord('A') + Vertex.count)
        Vertex.count += 1
        self.adjVertices = []
        self.status = None
        self.indegree = 0
        self.dfsNum = None
        self.low = None
        self.parent = None
        self.colour = None

    def __del__(self):
        Vertex.count -= 1


class Edge:
    count = 1

    def __init__(self):
        self.label = Edge.count
        Edge.count += 1
        self.weight = 0
        self.src = None
        self.dest = None
        self.type = None

    def __del__(self):
        Edge.count -= 1


class Graph:

    def __init__(self, fin, vertexCount):
        self.vertexCount = vertexCount
        self.vertices = []
        self.edges = {}

        for i in range(vertexCount):
            self.vertices.append(Vertex())

        for i in range(vertexCount):
            line = fin.readline().split()
            adjVerticesCount = int(line[0])
            line = line[1:]

            for j in range(adjVerticesCount):
                neighbour = self.vertices[int(line[j*2]) - 1]
                neighbour.indegree += 1

                weight = int(line[j*2 + 1])
                newEdge = Edge()
                newEdge.weight = weight
                newEdge.src = self.vertices[i]
                newEdge.dest = neighbour

                self.vertices[i].adjVertices.append(neighbour)
                self.edges[(self.vertices[i], neighbour)] = newEdge

    def displayVertices(self):
        print("The graph is:-")

        for i in range(self.vertexCount):
            print("Vertex " + self.vertices[i].name, " -->  ", end="")
            adjVerticesCount = len(self.vertices[i].adjVertices)

            for j in range(adjVerticesCount):
                neighbour = self.vertices[i].adjVertices[j]
                weight = self.edges[(self.vertices[i], neighbour)].weight
                print(neighbour.name + "(" + str(weight) + ")", end="")
                if j != adjVerticesCount -1:
                    print(", ", end="")
            print()
        print()

    def displayVerticesStatus(self):    # Primarily used for debugging code.
        print("The status of the vertices are:-")

        for i in range(self.vertexCount):
            print(self.vertices[i].name, " : ", self.vertices[i].status)

        print()

    def reset(self):
        for i in range(self.vertexCount):
            self.vertices[i].status = None
            self.vertices[i].colour = None
