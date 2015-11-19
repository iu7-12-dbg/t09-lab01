
from graph.graph import *


def getNode(nodes, number):
    a = filter(lambda x: x == number, nodes)
    for b in a:
        return b


class AStar:
    def __init__(self, g):
        if not isinstance(g, Graph):
            raise TypeError()
        self._g = g

    def _getNext(self, open_set, f_score):
        res = open_set.copy().pop()
        for node in open_set:
            if f_score[node] < f_score[res]:
                res = node
        return res

    def __reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.append(current)
        return total_path

    def start(self, begin, end):
        closed_set = set()
        open_set = {begin}
        came_from = dict()
        g_score = {i: INF for i in self._g.nodes()}
        g_score[begin] = 0
        f_score = {i: INF for i in self._g.nodes()}
        f_score[begin] = g_score[begin] + begin.h(end)
        while len(open_set) > 0:
            current = self._getNext(open_set, f_score)
            if current == end:
                return self.__reconstruct_path(came_from, end)
            open_set.remove(current)
            closed_set.add(current)
            for neighbor, w in self._g.neighbors(current):
                if neighbor in closed_set:
                    continue
                temp_g_score = g_score[current] + w
                if neighbor not in open_set:
                    open_set.add(neighbor)
                elif temp_g_score >= g_score[neighbor]:
                    continue
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = g_score[neighbor] + neighbor.h(end)
        return []
