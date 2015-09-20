import sys
__author__ = 'cerg'
INF = sys.maxsize


class Dijkstra:
    def __init__(self, g):
        self.graph = g
        self.__reset()

    def __reset(self):
        self.__dist = {i: INF for i in self.graph.nodes()}   # словарь расстояний
        # self.__path = {i: list() for i in self.graph.nodes()} # один из вас, добавьте
        self.__u = set(self.graph.nodes())  # непосещенные вершины

    def __start(self, node):
        self.__dist[node] = 0

        while len(self.__u) > 0:
            temp = self.__selnode()
            self.__u.remove(temp)
            arcs = self.graph.getarcs(temp)
            for arc in arcs:
                dist = self.__dist[temp] + arc.w()
                if dist < self.__dist[arc.b()]:
                    self.__dist[arc.b()] = dist

    def __selnode(self):
        i = self.__u.pop()
        self.__u.add(i)
        for d in self.__dist:
            if self.__dist[d] < self.__dist[i] and d in self.__u:
                i = d
        return i

    def result(self):
        return self.__dist.copy()

    def start(self, node):
        self.__reset()
        if node not in self.graph.nodes():
            raise ValueError
        self.__start(node)
        return self.result()







