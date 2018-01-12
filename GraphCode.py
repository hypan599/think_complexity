# -*- coding: utf-8 -*-


# ch2 graph
class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """create a new graph.
        vs stands for a list of verticles
        es stands for a list of edges"""
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """ add v to graph """
        self[v] = {}

    def add_edge(self, e):
        """add edge to graph by adding an entry to both directions.
        if there is already an edge connecting these vesicles
        the new edge replace it"""
        v, w = e
        self[v][w] = e
        self[w][v] = e


class Vertex(object):
    def __init__(self, label=""):
        self.label = label

    def __repr__(self):
        return "Vertex(%s) " % repr(self.label)

    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return "Edge(%s, %s) " % (repr(self[0]), repr(self[1]))

    __str__ = __repr__


v = Vertex('v')
w = Vertex('w')
e = Edge(v, w)
print(e)
g = Graph([v, w], [e])
print(g)
