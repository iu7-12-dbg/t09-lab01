from django.test.testcases import TestCase
from VisualGraph.models import GraphModel
from graph import graph, astar, dijkstra
from VisualGraph.views import *


class GraphTest(TestCase):
    def setUp(self):
        strgr = '{' \
                '"arcs": [{"a": 0, "b": 1, "w": 10}, {"a": 1, "b": 2, "w": 5},' \
                '{"a": 2, "b": 3, "w": 3}, {"a":0, "b": 2, "w":15}], ' \
                '"nodes": [{"value": 0, "x": 10, "y":5}, {"value": 1, "x": 15, "y":10},' \
                '{"value": 2, "x": 0, "y":0}, {"value": 3, "x": 10, "y":0}]' \
                '}'
        g = GraphModel(text=strgr)
        g.save()
        assert g is not None
        assert g.text == strgr
        self.g = g

    def test_pop_from_db(self):
        gg = GraphModel.objects.get(id=1)
        assert gg is not None
        assert gg == self.g

    # пипец, нигде было не написано, что тесты надо начинать с 'test*'

    def test_solveDijkstra(self):
        g = self.g
        g = graph.graph_from_text(g.text)
        d = dijkstra.Dijkstra(g)
        res = d.start(0)
        assert res == {0: 0, 1: 10, 2: 15, 3: 18}

    def test_solveAstar(self):
        g = self.g
        g = graph.graph_from_text(g.text)
        a = astar.AStar(g)
        start = astar.getNode(g.nodes(), 0)
        end = astar.getNode(g.nodes(), 3)
        res = a.start(start, end)
        assert res is not None
        assert res != []
        assert res == [3, 2, 0]

    # def testView_get(self):
    #     assert GraphView.get('', 1, ) == HttpResponse(self.g.text)



