import header
INP_FILE = "graph_edge_labelling.dat"


fin = open(INP_FILE, "r")
NUMBER_OF_VERTICES= int(fin.readline().split()[0])
g = header.Graph(fin, NUMBER_OF_VERTICES)
fin.close()
g.displayVertices()
#g.displayEdges()
g.revGraph()
g.displayVertices()
#g.displayEdges()
