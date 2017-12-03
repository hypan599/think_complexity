""" this file definess a hashtable object"""

class LinearMap(object):
	
	def __init__(self):
		self.items = []
	
	def add(self, k, v):
		self.items.append((k, v))
		
	def get(self,k):
		for key, val in self.items:
			if k == key:
				return val
		raise KeyError
	
class BetterMap(object):
	
	def __init__(self, n=100):
		self.maps = []
		for i in range(n):
			self.maps.append(LinearMap())
	
	def __len__(self):
		count = 0
		for linear_map in self.maps:
			count += len(linear_map)
		return count
	
	def find_map(self, k):
		index = hask(k) % lem(self.maps)
		return self.maps[index]
		
	def add(self, k, v):
		m = self.find_map(k)
		m.add(k, v)
		
	def get(self,k):
		m = self.find_map(k)
		return m.get(k)
		
	def iteritems(self):
		for linear_map in self.maps:
			for (k, v) in linear_map:
				yield k, v

class HashMap(object):
	
	def __init__(self):
		self.maps = BetterMap(2)
		self.num = 0
	
	def get(self, k):
		return self.maps.get(k)
	
	def add(self, k, v):
		if len(self.maps.maps) == self.num:
			self.resize()
		
		self.maps.add(k, v)
		self.num += 1
	
	def resize(self):
		new_maps = BetterMap(self.num * 2)
		
		for m in self.maps.maps:
			for k, v in m.items:
				new_maps.add(k, v)
		self.maps = new_maps
		