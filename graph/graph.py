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

    def __eq__(self, other):
        if isinstance(other, Arc):
            return self.__a == other.__a and self.__b == other.__b and self._weight == other._weight
        return False

    def a(self):
        return self.__a

    def b(self):
        return self.__b

    def w(self):
        return self._weight


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

        self.__arcs = arcs if arcs is not None else set()     # Arc

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

        if arc not in self.__arcs:
            for node in arc:
                if node not in self.__nodes:
                    raise ValueError

            self.__nodes.add(arc)

    def delarc(self, arc):
        if arc is None:
            return

        if not isinstance(arc, Arc):
            raise TypeError("Parameter of wrong type is passed")

        if arc in self.__arcs:
            self.__arcs.remove(arc)

    def delnode(self, node):
        if node is None:
            return

        if not isinstance(node, int):
            raise TypeError("Parameter of wrong type is passed")

        if node in self.__nodes:
            self.__nodes.remove(node)

        arcs_to_delete = [arc for arc in self.__arcs if node in arc]

        for arc in arcs_to_delete:
            self.__arcs.remove(arc)

    def getarcs(self, node):
        if node is None:
            raise ValueError("node ca not be None")

        if not isinstance(node, int):
            raise TypeError("Parameter of wrong type is passed")

        if node not in self.__nodes:
            raise ValueError("Node is not exist")

        arcs = set()
        for a in self.__arcs:
            if a.a() == node:
                arcs.add(a)
        return arcs

    def arcs(self):
        return self.__arcs.copy()

    def nodes(self):
        return self.__nodes.copy()
