# coding UTF-8


class Arc:
    def __init__(self, a, b, weight):  # конструктор
        self.__a = a
        self.__b = b
        self._weight = weight

    def __str__(self):  # это для консоли
        return str((self.a(), self.b(), self._weight))

    def __hash__(self):
        return self.__a * (2 ** 16) + self.__b

    def __iter__(self):
        return [self.__a, self.__b].__iter__()

    def a(self):
        return self.__a

    def b(self):
        return self.__b

    def w(self):
        return self._weight


class Graph:
    def __init__(self, nodes=None, arcs=None):
        self.__nodes = nodes if nodes else set()  # int
        self.__arcs = arcs if arcs else set()     # Arc
        for a in arcs:
            for n in a:
                if n not in self.__nodes:
                    raise ValueError

    def addnode(self, node):
        if node not in self.__nodes:
            self.__nodes.add(node)

    def addarc(self, arc):
        if arc not in self.__arcs:
            self.__nodes.add(arc)

    def delarc(self, arc):
        if arc in self.__arcs:
            self.__arcs.remove(arc)

    def delnode(self, node):
        if node in self.__nodes:
            self.__nodes.remove(node)

    def getarcs(self, node):
        arcs = set()
        for a in self.__arcs:
            if a.a() == node:
                arcs.add(a)
        return arcs

    def arcs(self):
        return self.__arcs.copy()

    def nodes(self):
        return self.__nodes.copy()
