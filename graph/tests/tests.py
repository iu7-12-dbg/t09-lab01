import unittest, random
from graph.graph import *
from graph.dijkstra import *


class TestArc(unittest.TestCase):
    def test_create(self):
        for i in range(10):
            a, b, c = random.random(), random.random(), random.random()
            arc = Arc(a, b, c)
            self.assertEqual(a, arc.a())
            self.assertEqual(b, arc.b())
            self.assertEqual(c, arc.w())

    def test_str(self):
        for i in range(10):
            a, b, c = random.random(), random.random(), random.random()
            arc = Arc(a, b, c)
            s = '(' + str(a) + ', ' + str(b) + ', ' + str(c) + ')'
            self.assertEqual(s, str(arc))


if __name__ == "__main__":
    unittest.main()