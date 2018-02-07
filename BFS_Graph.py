# from Graph import Graph
from collections import deque


def default_visit(node):
    print("visiting node: %s" % node.label)


def bfs(g, top_node, visit=default_visit):
    visited = set()
    visited.add(top_node)
    queue = deque()
    queue.append(top_node)
    while len(queue):
        curr_node = queue.pop()
        visit(curr_node)
        visited.add(curr_node)

        for c in g.out_vertices(curr_node):
            if c not in visited and c not in queue:
                queue.append(c)
