INP_FILE = "graph.dat"          # specifies the input file which contains the graph information
NUMBER_OF_VERTICES = 7          # constant denoting number of vertices per graph


# This class defines the blueprint of a Vertex object.
class Vertex:
    count = 0                       # class variable (not an instance variable) used to automatically name vertices.

    def __init__(self):             # constructor
        self.name = chr(ord('A') + Vertex.count)    # automatically names vertices starting from 'A'
        self.number = Vertex.count  # used by UnionFind for Kruskal's algo; used as an index into the array which keeps track of the components.
        Vertex.count += 1
        self.adjVertices = []       # an array of pointers pointing to the adjacent vertices
        self.revAdjVertices = []    # this is just a temporary list to hold the adjacent vertices while reversing a graph
        self.status = None          # the status can be made "Visited" when a vertex has been visited; by default it is None (NULL)
        self.indegree = 0           # keeps track of the indegree of a vertex
        self.dfsNum = None          # keeps track of the discovery number of a vertex during a DFS traversal.
        self.low = None             # keeps track of the lowest vertex DFSnum that can be reached from a vertex; used in finding Articulation points
        self.parent = None          # keeps track of the parent node of a vertex; used in finding articulation points.
        self.colour = None          # used to keep track of whether a vertex has already been printed once; used in finding
                                    # articulation points, when the same vertex is identified as an articulation point by multiple sub-graphs
        self.dRow = None            # stores a pointer to dijkstra-Row object; which contains fields used during Dijkstra's algo

    def __del__(self):              # destructor
        Vertex.count -= 1           # if any temporary Vertex object gets created, then reduce the count as soon as it goes out of scope
                                    # so that the next Vertex object would get that name.

    def reset(self):                # resets the class counter. Used before reading a new graph
        Vertex.count = 0


# This class defines the blueprint of an Edge object.
class Edge:
    count = 1                       # class variable (not an instance variable) used to automatically number edges.

    def __init__(self):             # constructor
        self.label = Edge.count     # automatically numbers vertices starting from 1
        Edge.count += 1
        self.weight = 0             # stores the weight of the edge
        self.src = None             # a pointer to the source vertex object
        self.dest = None            # a pointer to the destination vertex object
        self.type = None            # stores the type of the edge; used while labelling edges (not relevant for this assignment).
                                    # Will be used to classify edges into tree, back, forward and cross edges

    def __del__(self):              # destructor
        Edge.count -= 1             # if any temporary Edge object gets created, then reduce the count as soon as it goes out of scope
                                    # so that the next Vertex object would get that number.

    def __lt__(self, other):        # This function compares two Edge objects; and is required while making a heap of the edges.
        return self.weight < other.weight   # Such a heap is required for implementing the Kruskal's algo.

    def reset(self):
        Edge.count = 0              # resets the class counter. Used before reading a new graph


# This class defines the blueprint of a Graph object. A graph is a set of Vertices and Edges.
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

    def displayEdges(self):
        edgeList = list(self.edges.values())

        print("The edges are:-")
        print("Src\tDest\tLabel\tWeight\tType")
        for edge in edgeList:
            print(edge.src.name + "\t" + edge.dest.name + "\t\t" + str(edge.label) + "\t\t" + str(edge.weight) + "\t\t" + str(edge.type))
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
            self.vertices[i].dfsNum = None
            self.vertices[i].low = None
            self.vertices[i].parent = None

    def resetVertexNEdge(self):
        self.vertices[0].reset()
        edgesList = list(self.edges.values())
        edgesList[0].reset()

    def revGraph(self):
        self.reset()
        tempEdges = self.edges
        self.edges = {}
        for vertex in self.vertices:
            vertex.revAdjVertices = vertex.adjVertices
            vertex.adjVertices = []
            vertex.indegree = 0

        for vertex in self.vertices:
            for neighbour in vertex.revAdjVertices:
                neighbour.adjVertices.append(vertex)
                neighbour.indegree += 1

                edge = tempEdges[(vertex, neighbour)]
                tempVertex = edge.src
                edge.src = edge.dest
                edge.dest = tempVertex
                edge.type = None

                self.edges[(neighbour, vertex)] = edge
            vertex.revAdjVertices = []


# This code has been adapted from: https://github.com/williamfiset/data-structures/tree/master/com/williamfiset/datastructures/unionfind
# Explanation video & playlist on UnionFind: https://www.youtube.com/watch?v=KbFlZYCpONw&list=PLDV1Zeh2NRsBI1C-mR6ZhHTyfoEJWlxvq&index=5
# Employs path compression.
class UnionFind:
    def __init__(self, size):
        if size <= 0:
            raise TypeError("size <= 0 is not allowed")

        # Keeps track of the number of components.
        # Initially, the number of components is equal to the number of vertices.
        self.componentsCount = size

        # Keeps track of the size of each component.
        # Initially, all components have just one element in them, hence their size would be 1
        self.componentSize = [1] * size

        # link[i] points to the parent of i, if link[i] = i then i is a root node
        self.link = []

        # Initially, each vertex is its own parent.
        for i in range(size):
            self.link.append(i)

    # Find which component/set 'v' belongs to; takes amortized constant time.
    # Employs path compression.
    def find(self, v):
        root = v

        # Find the root of the component/set
        while root != self.link[root]:
            root = self.link[root]

        # Compress the path leading back to the root.
        # Doing this operation is called "path compression" and is what gives us amortized time complexity.
        while self.link[v] != root:
            nextNode = self.link[v]
            self.link[v] = root
            v = nextNode

        return root

    def connected(self, v, w):
        return self.find(v) == self.find(w)

    def componentSize(self, v):
        return self.componentSize[self.find(v)]

    # Unify the components/sets containing elements 'v' and 'w'
    def unify(self, v, w):
        root1 = self.find(v)
        root2 = self.find(w)

        # These elements are already in the same group!
        if root1 == root2:
            return

        # Merge smaller component/set into the larger one.
        if self.componentSize[root1] < self.componentSize[root2]:
            self.componentSize[root2] += self.componentSize[root1]
            self.link[root1] = root2
        else:
            self.componentSize[root1] += self.componentSize[root2]
            self.link[root2] = root1

        # Since the roots found are different we know that the number of components/sets has decreased by one
        self.componentsCount -= 1
