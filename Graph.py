# -*- coding: utf-8 -*-
import random

# ch2 graph
class Graph(dict):

    def __init__(self, vs=[], es=[]):
        """create a new graph.
        vs stands for a list of vertices
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
        if there is already an edge connecting these vertices
        the new edge replace it"""
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        try:
            e = self[v1][v2]
            return e
        except KeyError:
            return None

    def remove_edge(self, e):
        v, w = e
        self[v].pop(w)
        self[w].pop(v)

    def vertices(self):
        return self.keys()

    def edges(self):
        _edges = []
        for v in self.values():
            for e in v.values():
                if e not in _edges:
                    _edges.append(e)
        return _edges

    def out_vertices(self, v):
        try:
            return self[v].keys()
        except KeyError:
            return "Invalid vertex"

    def out_edges(self, v):
        try:
            return self[v].values()
        except KeyError:
            return "Invalid vertex"

    def add_all_edges(self):
        for v1 in self.keys():
            for v2 in self.keys():
                if v1 == v2:
                    continue
                else:
                    self.add_edge((v1, v2))

    def add_regular_edges(self, num):  # todo : regular edges and degrees  先证明定理！
        if num == 1:
            if len(self.vertices()) % 2 == 1:
                raise ValueError("unable to create regular graph")
            vertices_list = self.vertices()
            while vertices_list:
                vertex1 = vertices_list.pop()
                vertex2 = vertices_list.pop()
                self.add_edge((vertex1, vertex2))
            return
        if num == 2:
            vertices_list = self.vertices()
            while len(vertices_list) > 1:
                vertex1 = vertices_list.pop()
                if len(vertices_list) == len(self.vertices()) - 1:
                    self.add_edge((vertex1, vertices_list[0]))
                self.add_edge((vertex1, vertices_list[-1]))
            return
        raise ValueError("degree more that 1 not supported")

    def is_connected(self):
        q = list(self.keys())[0]
        marked = {i: 0 for i in self.keys()}
        while q:
            vv = q.pop()
            marked[vv] = 1
            for v in self.out_vertices(vv):
                if marked[v] == 0:
                    q.append(v)
        if 0 in marked.values():
            return False
        return True

    def add_random_edges(self, p):
        def yes_or_no(p):
            p = int(1000 * p)
            rand_int = random.randint(1, 1000)
            if rand_int <= p:
                return True
            else:
                return False

        if p >= 1:
            raise ValueError("Error:possibility above 1")
        vertices_list = list(self.vertices())
        while vertices_list:
            vertex = vertices_list.pop()
            for v in vertices_list:
                if yes_or_no(p):
                    self.add_edge((vertex, v))


class Vertex(object):
    def __init__(self, label=""):
        self.label = label

    def __repr__(self):
        return "Vertex(%s)" % repr(self.label)

    __str__ = __repr__


# todo: check this new method
# since class edge is not used in any test script
class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return "Edge(%s, %s)" % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
