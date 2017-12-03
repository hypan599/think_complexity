from Graph import *
import random

def yes_or_no(p):
	p = int(1000 * p)
	rand_int = random.randint(1, 1000)
	if rand_int <= p:
		return True
	else:	
		return False

class RandomGraph(Graph):
	
	def add_random_edges(self, p):	
		if p >= 1:
			raise ValueError("Error:possibility above 1")
		vertices_list = self.vertices()
		while vertices_list:
			vertex = vertices_list.pop()
			for v in vertices_list:
				if yes_or_no(p):
					self.add_edge((vertex, v))