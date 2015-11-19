# coding UTF-8
import math, sys, json
INF = sys.maxsize


"""
    Отнаследовался от int, чтобы "унифицировать" все
    поэтому метод init не нужен - int статичен и определяется в new
"""


class Node(int):
    def __new__(cls, val, **kwargs):
        self = super(Node, cls).__new__(cls, val)
        key = kwargs.get('type', 'coord')
        if key == 'coord':
            self._x = kwargs['x']
            self._y = kwargs['y']
            self._type = key
            self.h = self.__coord_hfun
        return self

    def __coord_hfun(self, other):
        if not isinstance(other, Node):
            raise TypeError()
        val = (self._x - other._x) ** 2 + (self._y - other._y) ** 2
        return math.sqrt(val)

    @classmethod
    def from_dict(cls, d):
        n = Node(d['value'], type='coord', x=d['x'], y=d['y'])
        return n


class Arc:
    def __init__(self, a, b, weight):  # конструктор
        self._a = a
        self._b = b
        self._weight = weight

    def __str__(self):  # это для консоли
        return str((self.a(), self.b(), self._weight))

    def __hash__(self):
        return self._a * (2 ** 16) + self._b

    def __iter__(self):
        # return [self._a, self._b].__iter__()
        yield self._a
        yield self._b

    def __eq__(self, other):
        if isinstance(other, Arc):
            return self._a == other.a() and self._b == other.b() and self._weight == other.w()
        return False

    def a(self):
        return self._a

    def b(self):
        return self._b

    def w(self):
        return self._weight

    @classmethod
    def getnode(cls, nodes, number):
        a = filter(lambda x: x == number, nodes)
        for b in a:
            return b

    @classmethod
    def from_dict(cls, d, nodes):
        a = cls.getnode(nodes, d['a'])
        b = cls.getnode(nodes, d['b'])
        arc = cls(a, b, d['w'])
        return arc


def graph_from_text(text):
    obj = json.loads(text)
    nodes = obj['nodes']
    arcs = obj['arcs']
    nodes = {Node.from_dict(n) for n in nodes}
    arcs = {Arc.from_dict(a, nodes) for a in arcs}
    g = Graph(nodes, arcs)
    return g


class Graph:
    def __init__(self, nodes=None, arcs=None):
        if (nodes is None or len(nodes) == 0) and arcs is not None and len(arcs) > 0:  # can not add arcs without nodes
            raise ValueError

        if nodes is not None and not isinstance(nodes, set):
            raise TypeError("Parameter of wrong type = " + str(type(nodes)) + " is passed")

        if arcs is not None and not isinstance(arcs, set):
            raise TypeError("Parameter of wrong type = " + str(type(nodes)) + " is passed")

        self.__nodes = nodes if nodes is not None else set()  # int

        if arcs is not None:
            for a in arcs:
                for n in a:
                    if n not in self.__nodes:
                        raise ValueError

        self._arcs = arcs if arcs is not None else set()     # Arc

    def addnode(self, node):
        if node is None:
            return

        if not isinstance(node, int):
            raise TypeError("Parameter of wrong type is passed")

        if node not in self.__nodes:
            self.__nodes.add(node)

    def addarc(self, arc):
        if arc is None:
            return

        if not isinstance(arc, Arc):
            raise TypeError("Parameter of wrong type is passed")

        if arc not in self._arcs:
            for node in arc:
                if node not in self.__nodes:
                    raise ValueError

            self.__nodes.add(arc)

    def delarc(self, arc):
        if arc is None:
            return

        if not isinstance(arc, Arc):
            raise TypeError("Parameter of wrong type is passed")

        if arc in self._arcs:
            self._arcs.remove(arc)

    def delnode(self, node):
        if node is None:
            return

        if not isinstance(node, int):
            raise TypeError("Parameter of wrong type is passed")

        if node in self.__nodes:
            self.__nodes.remove(node)

        arcs_to_delete = [arc for arc in self._arcs if node in arc]

        for arc in arcs_to_delete:
            self._arcs.remove(arc)

    def getarcs(self, node):
        if node is None:
            raise ValueError("node ca not be None")

        if not isinstance(node, int):
            raise TypeError("Parameter of wrong type is passed")

        if node not in self.__nodes:
            raise ValueError("Node is not exist")

        arcs = set()
        for a in self._arcs:
            if a.a() == node:
                arcs.add(a)
        return arcs

    def arcs(self):
        return self._arcs.copy()

    def nodes(self):
        return self.__nodes.copy()

    def neighbors(self, node):
        for arc in self.getarcs(node):
            if arc.a() == node:
                yield (arc.b(), arc.w())
            else:
                yield (arc.a(), arc.w())
