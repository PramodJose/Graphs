import sys
import header
import TopologicalSort
import dijkstra
import kruskal
import FindArticulationPoints
import StronglyConnectedComponents


if len(sys.argv) != 2:
    print("Usage:-\npython3 main.py <output-file>")
    exit()
fin = open(header.INP_FILE, "r")
fout = open(sys.argv[1], "w")
g = header.Graph(fin, header.NUMBER_OF_VERTICES)
TopologicalSort.topologicalSort(g, fout)
g.resetVertexNEdge()

fout.write("\nFor the second graph:\nShortest paths for the first vertex:\n\n")
g = header.Graph(fin, header.NUMBER_OF_VERTICES)
dijkstra.dijkstra(g, g.vertices[0], fout)
g.resetVertexNEdge()

g = header.Graph(fin, header.NUMBER_OF_VERTICES)
kruskal.kruskal(g, fout)
g.resetVertexNEdge()

fout.write("\nFor the fourth graph, the articulation points are:\n")
g = header.Graph(fin, header.NUMBER_OF_VERTICES)
source = g.vertices[int(fin.readline().split()[0]) - 1]
FindArticulationPoints.findArticulationPoints(g, source, fout)
g.resetVertexNEdge()

fout.write("\nFor the fifth graph, the articulation points are:\n")
FindArticulationPoints.findArticulationPoints.counter = None
g = header.Graph(fin, header.NUMBER_OF_VERTICES)
source = g.vertices[int(fin.readline().split()[0]) - 1]
FindArticulationPoints.findArticulationPoints(g, source, fout)
g.resetVertexNEdge()

fout.write("The strongly connected components of the sixth graph are:\n")
g = header.Graph(fin, header.NUMBER_OF_VERTICES)
StronglyConnectedComponents.SSCDriver(g, fout)

fin.close()
fout.close()
