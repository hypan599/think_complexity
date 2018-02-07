from GraphWorld import *
from Graph import *
import string
from BFS_Graph import bfs
from Itertool import alphabet_num_cycle
import timeit
import matplotlib.pyplot as plt


def erdos(n):
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    for p in range(20, 40, 1):
        p /= 100
        connection_list = []
        connection_count = 0
        for i in range(n):
            g = Graph(vs)
            g.add_random_edges(p)
            connection_list.append(g.is_connected())
            if g.is_connected():
                connection_count += 1
        print("p = {0:.2f} and connection rate are:{1:.2f}".format(p, connection_count / 10))


def draw_graph(g):
    # draw the graph
    layout = CircleLayout(g)
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()


if __name__ == '__main__':
    xs = list(range(100, 800, 100))
    gs = [Graph([Vertex(c) for c in alphabet_num_cycle(x)]) for x in xs]
    for g in gs:
        g.add_random_edges(0.1)
    ys = [timeit.timeit(lambda: bfs(g, next(iter(g.vertices()))), number=1) for g in gs]
    plt.plot(xs, ys, "*--")
    plt.plot(xs, [i / 6000 for i in xs])
    # plt.xscale("log")
    # plt.yscale("log")
    plt.title("bfs performance")
    plt.xlabel("n")
    plt.ylabel("run time")
    plt.show()
