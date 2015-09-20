
from graph.graph import *
from graph.dijkstra import *

a = Arc(0, 1, 1)
print(a, '\n')

nodes = {0, 1, 2, 3}
arcs = {Arc(0, 1, 1), Arc(1, 2, 1), Arc(2, 1, 2), Arc(2, 3, 2)}

G = Graph(nodes, arcs)
d = Dijkstra(G)
d.start(0)
print(d.result())



input('put enter\n')
