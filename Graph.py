# -*- coding: utf-8 -*-


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
        pass  # todo: remove edge

    def vertices(self):
        return self.keys()

    def edges(self):
        _edges = []
        for v in self.values():
            for e in v.values():
                if e not in _edges:
                    _edges.append(e)
        return str(_edges)

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

    def add_regular_edges(self, num):  # todo : regular edges and degrees
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
        q = []
        q.append(list(self.vertices())[0])
        marked = dict(zip(self.vertices(), [0 for i in range(len(self.vertices()))]))
        while q:
            vv = q.pop()
            marked[vv] = 1
            for v in self.out_vertices(vv):
                if marked[v] == 0:
                    q.append(v)
        if 0 in marked.values():
            return False
        else:
            return True


class Vertex(object):
    def __init__(self, label=""):
        self.label = label

    def __repr__(self):
        return "Vertex(%s)" % repr(self.label)

    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return "Edge(%s, %s)" % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
