""" this file defines a hashtable object"""


class LinearMap:
    """
    basic class of hashtable
    """
    def __init__(self):
        self.items = []
        self.num = 0

    def __len__(self):
        return self.num

    def add(self, k, v):
        self.items.append((k, v))
        self.num += 1

    def get(self, k):
        for key, val in self.items:
            if k == key:
                return val
        raise KeyError


class BetterMap:
    """
    an advanced hashtable
    """
    def __init__(self, n=100):
        self.maps = []
        self.num = 0
        for i in range(n):
            self.maps.append(LinearMap())

    def __len__(self):
        return self.num

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)
        self.num += 1

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)

    def iteritems(self):
        for linear_map in self.maps:
            for i in linear_map.items:
                yield i[0], i[1]


class HashMap:

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

        for k, v in self.maps.iteritems():
            new_maps.add(k, v)
        self.maps = new_maps


class TreeMapNode:

    def __init__(self, key, value):
        self.id = None
        self.left_child = None
        self.right_child = None
        self.key = key
        self.value = value
        self.color = "Black"

    def _paint(self, color):
        if color not in ["red", "black"]:
            raise ValueError("invalid color")
        self.color = color


# todo: use red black tree in map
class TreeMap:

    def __init__(self):
        self.root = None
        self.num = 0

    def _left_rotate(self, node):
        pass

    def _right_rotate(self, node):
        pass

    def add(self, k, v):
        pass

    def get(self, k):
        pass

    def remove(self, k):
        pass
