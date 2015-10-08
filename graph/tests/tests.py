import unittest, random
from graph.graph import *
from graph.dijkstra import *


class TestArc(unittest.TestCase):
    def test_create(self):
        for i in range(10):
            a, b, c = random.random() * 100, random.random() * 100, random.random() * 100
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


class TestGraph(unittest.TestCase):

    # ----------------------------------------------------------------------------------------
    # tests for constructor of the class
    # ----------------------------------------------------------------------------------------
    def testCreationWithoutNodesAndArcs(self):
        graph = Graph(None, None)
        self.assertEqual(graph.nodes(), set(), "Creation with nodes = None and arcs = None FAILED")
        self.assertEqual(graph.arcs(), set(), "Creation with nodes = None and arcs = None FAILED")

    def testCreationWithNodesAndWithoutArcs(self):
        graph = Graph(set(), None)
        self.assertEqual(graph.nodes(), set(), "Creation with nodes != None and arcs = None FAILED")
        self.assertEqual(graph.arcs(), set(), "Creation with nodes != None and arcs = None FAILED")

    def testCreationWithoutNodesAndWithArcs(self):
        graph = Graph(None, set())
        self.assertEqual(graph.nodes(), set(), "Creation with nodes = None and arcs != None FAILED")
        self.assertEqual(graph.arcs(), set(), "Creation with nodes = None and arcs != None FAILED")

    def testCreationWithWrongTypeOfNodesParameter(self):
        with self.assertRaises(TypeError):
            def function(): lambda: 1 + 1
            Graph(function, None)  # passing function instead of set of nodes

    def testCreationWithWrongTypeOfArcsParameter(self):
        with self.assertRaises(TypeError):
            def function(): lambda: 1 + 1
            Graph(None, function)  # passing function instead of set of arcs

    def testCreationWithEmptyNodesAndEmptyArcsParameter(self):
        graph = Graph(set(), set())
        self.assertEqual(graph.nodes(), set(), "Creation with nodes = set() and arcs = set() FAILED")
        self.assertEqual(graph.arcs(), set(), "Creation with nodes = set() and arcs = set() FAILED")

    def testCreationWithNotEmptyNodesAndEmptyArcsParameter(self):
        nodes = set([1, 2, 3])
        graph = Graph(nodes, None)
        self.assertEqual(graph.nodes(), nodes, "Creation with nodes 1, 2, 3 and empty arcs set FAILED")
        self.assertEqual(graph.arcs(), set(), "Creation with nodes 1, 2, 3 and empty arcs set  FAILED")

    def testCreationWithEmptyNodesAndNotEmptyArcsParameter(self):
        with self.assertRaises(ValueError):
            arcs = set([Arc(1, 2, 10), Arc(2, 3, 12)])
            Graph(None, arcs)

    def testCreationWithNotEmptyNodesAndNotEmptyArcsParameter(self):
        nodes = set([1, 2, 3])
        arcs = set([Arc(1, 2, 10), Arc(2, 3, 12)])
        graph = Graph(nodes, arcs)
        self.assertEqual(graph.nodes(), nodes, "Creation with nodes 1, 2, 3 and (Arc(1, 2, 10), Arc(2, 3, 12)) FAILED")
        self.assertEqual(graph.arcs(), arcs, "Creation with nodes 1, 2, 3 and (Arc(1, 2, 10), Arc(2, 3, 12)) FAILED")

    def testCreationWithNotConsistentNodesAndArcsSets(self):
        with self.assertRaises(ValueError):
            nodes = set([1, 2, 3])
            arcs = set([Arc(1, 4, 34), Arc(2, 0, 112)])
            Graph(nodes, arcs)

    # ----------------------------------------------------------------------------------------
    # tests for addnode method
    # ----------------------------------------------------------------------------------------
    def testAddNodeWithNodeEqualsNone(self):
        graph = Graph(set(), set())
        graph.addnode(None)
        self.assertEqual(graph.nodes(), set(), "Addition of node = None FAILED")
        self.assertEqual(graph.arcs(), set(), "Addition of node = None FAILED")

    def testAddNodeWithWrongTypeOfNodeParameter(self):
        with self.assertRaises(TypeError):
            def function(): lambda: 1 + 1
            Graph(set(), set()).addnode(function)

    def testAdditionOfExistingNode(self):
        graph = Graph(set([1]), set())
        graph.addnode(1)
        self.assertEqual(graph.nodes(), set([1]), "Addition of node = 1 (existent) FAILED")
        self.assertEqual(graph.arcs(), set(), "Addition of node = 1 (existent) FAILED")

    def testAdditionOfNewNode(self):
        graph = Graph(set([1]), set())
        graph.addnode(2)
        self.assertEqual(graph.nodes(), set([1, 2]), "Addition of node = 2 to set of nodes = (1) FAILED")
        self.assertEqual(graph.arcs(), set(), "Addition of node = 2 to set of nodes = (1) (existent) FAILED")

    # ----------------------------------------------------------------------------------------
    # tests for addarc method
    # ----------------------------------------------------------------------------------------
    def testAddArcWithArcEqualsNone(self):
        graph = Graph(set(), set())
        graph.addarc(None)
        self.assertEqual(graph.nodes(), set(), "Addition of arc = None FAILED")
        self.assertEqual(graph.arcs(), set(), "Addition of arc = None FAILED")

    def testAddArcWithWrongTypeOfArcParameter(self):
        with self.assertRaises(TypeError):
            def function(): lambda: 1 + 1
            Graph(set(), set()).addarc(function)

    def testAdditionOfExistingArc(self):
        graph = Graph(set([1, 2]), set([Arc(1, 2, 10)]))
        graph.addarc(Arc(1, 2, 10))
        self.assertEqual(graph.nodes(), set([1, 2]), "Addition of Arc(1, 2, 10) (existent) FAILED")
        self.assertEqual(graph.arcs(), set([Arc(1, 2, 10)]), "Addition of Arc(1, 2, 10) (existent) FAILED")

    def testAdditionOfArcWithNotExistingNodes(self):
        with self.assertRaises(ValueError):
            graph = Graph(set([1, 2]), set())
            graph.addarc(Arc(3, 2, 10))

    def testAdditionOfArcWithExistingNodes(self):
        graph = Graph(set([1, 2]), set([Arc(1, 2, 10)]))
        graph.addarc(Arc(1, 2, 10))
        self.assertEqual(graph.nodes(), set([1, 2]), "Addition of Arc(1, 2, 10) (existing) FAILED")
        self.assertEqual(graph.arcs(), set([Arc(1, 2, 10)]), "Addition of Arc(1, 2, 10) (existing) FAILED")

    # ----------------------------------------------------------------------------------------
    # tests for delarc method
    # ----------------------------------------------------------------------------------------
    def testDeleteArcWithArcEqualsNone(self):
        graph = Graph(set([1, 2]), set([Arc(1, 2, 10)]))
        graph.delarc(None)
        self.assertEqual(graph.nodes(), set([1, 2]), "Deletion of Arc = None FAILED")
        self.assertEqual(graph.arcs(), set([Arc(1, 2, 10)]), "Deletion of Arc = None FAILED")

    def testDeleteArcWithWrongTypeOfArcParameter(self):
        with self.assertRaises(TypeError):
            def function(): lambda: 1 + 1
            Graph(set(), set()).delarc(function)

    def testDeletionOfNotExistingArc(self):
        graph = Graph(set([1, 2]), set([Arc(1, 2, 10)]))
        graph.delarc(Arc(0, 2, 10))
        self.assertEqual(graph.nodes(), set([1, 2]), "Deletion of not existing arc FAILED")
        self.assertEqual(graph.arcs(), set([Arc(1, 2, 10)]), "Deletion of not existing arc FAILED")

    def testDeletionOfExistingArc(self):
        graph = Graph(set([1, 2]), set([Arc(1, 2, 10)]))
        graph.delarc(Arc(1, 2, 10))
        self.assertEqual(graph.nodes(), set([1, 2]), "Deletion of existing Arc FAILED")
        self.assertEqual(graph.arcs(), set(), "Deletion of existing Arc FAILED")

    # ----------------------------------------------------------------------------------------
    # tests for delnode method
    # ----------------------------------------------------------------------------------------
    def testDeleteNodeWithNodeEqualsNone(self):
        graph = Graph(set([1, 2]), set([Arc(1, 2, 10)]))
        graph.delnode(None)
        self.assertEqual(graph.nodes(), set([1, 2]), "Deletion of node = None FAILED")
        self.assertEqual(graph.arcs(), set([Arc(1, 2, 10)]), "Deletion of node = None FAILED")

    def testDeleteNodeWithWrongTypeOfNodeParameter(self):
        with self.assertRaises(TypeError):
            def function(): lambda: 1 + 1
            Graph(set(), set()).delnode(function)

    def testDeletionOfNotExistingNode(self):
        graph = Graph(set([1, 2]), set([Arc(1, 2, 10)]))
        graph.delnode(3)
        self.assertEqual(graph.nodes(), set([1, 2]), "Deletion of not existing node FAILED")
        self.assertEqual(graph.arcs(), set([Arc(1, 2, 10)]), "Deletion of not existing node FAILED")

    def testDeletionOfExistingNodeWithoutArcs(self):
        graph = Graph(set([1, 2, 3]), set([Arc(1, 2, 10)]))
        graph.delnode(3)
        self.assertEqual(graph.nodes(), set([1, 2]), "Deletion of existing node without arcs FAILED")
        self.assertEqual(graph.arcs(), set([Arc(1, 2, 10)]), "Deletion of existing node without arcs FAILED")

    def testDeletionOfExistingNodeWithArcs(self):
        graph = Graph(set([1, 2, 3]), set([Arc(1, 2, 10)]))
        graph.delnode(1)
        self.assertEqual(graph.nodes(), set([2, 3]), "Deletion of existing node with arcs FAILED")
        self.assertEqual(graph.arcs(), set(), "Deletion of existing node with arcs FAILED")

    # ----------------------------------------------------------------------------------------
    # tests for getarc method
    # ----------------------------------------------------------------------------------------
    def testGetArcsWithNodeEqualsNone(self):
        with self.assertRaises(ValueError):
            Graph(set([1, 2]), set([Arc(1, 2, 10)])).getarcs(None)

    def testGetArcsWithWrongTypeOfNodeParameter(self):
        with self.assertRaises(TypeError):
            def function(): lambda: 1 + 1
            Graph(set(), set()).getarcs(function)

    def testGetArcsByNotExistingNode(self):
        with self.assertRaises(ValueError):
            Graph(set([1, 2]), set([Arc(1, 2, 10)])).getarcs(3)

    def testGetArcsOfExistingNode(self):
        arcs = set([Arc(1, 2, 10)])
        self.assertEqual(Graph(set([1, 2, 3]), arcs).getarcs(1), arcs, "Getting arcs FAILED")


if __name__ == "__main__":
    unittest.main()
