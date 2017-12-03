from GraphWorld import *
from Graph import *
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
    print g.is_connected()
    
    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()
	
def erdos(n):
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]
	
    for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        connection_list = []
        for i in range(10):
            g = RandomGraph(vs)
            g.add_random_edges(p)
            connection_list.append(g.is_connected())
        print "p = {0} and 10 graphs are:{1}".format(p, connection_list)
		
	

if __name__ == '__main__':
	erdos(10)