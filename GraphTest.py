from GraphWorld import *
# from Graph import *
from RandomGraph import *
import string


def main():
    # generate vertices a,b,c...
    # n is number of vertices
    n = 10
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = RandomGraph(vs)
    g.add_random_edges(0.1)
    # g.add_all_edges()
    layout = CircleLayout(g)
    print(g.is_connected())

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()


def erdos(n):
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    for p in range(20, 40, 1):
        p /= 100
        connection_list = []
        connection_count = 0
        for i in range(n):
            g = RandomGraph(vs)
            g.add_random_edges(p)
            connection_list.append(g.is_connected())
            if g.is_connected():
                connection_count += 1
        print("p = {0:.2f} and connection rate are:{1:.2f}".format(p, connection_count / 10))


if __name__ == '__main__':
    erdos(10)
