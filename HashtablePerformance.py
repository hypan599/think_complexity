# -*- coding: utf-8 -*-
from hashtable import LinearMap, BetterMap, HashMap, TreeMap
import matplotlib.pyplot as plt
import timeit
import math
from Itertool import alphabet_num_cycle


def add_items(map, magnitude):
    for i in alphabet_num_cycle(magnitude):
        map.add(i, 1)


if __name__ == "__main__":
    # test_and_draw(BetterMap())
    # test_and_draw(HashMap())
    my_hash_map = HashMap()
    my_linear_map = LinearMap()
    my_better_map = BetterMap()

    xs = range(10000, 100001, 30000)
    hash_ys = [timeit.timeit(lambda: add_items(my_hash_map, x), number=2) for x in xs]
    linear_ys = [timeit.timeit(lambda: add_items(my_linear_map, x), number=2) for x in xs]
    better_ys = [timeit.timeit(lambda: add_items(my_better_map, x), number=2) for x in xs]

    plt.plot(xs, hash_ys, label=str(type(my_hash_map)))
    plt.plot(xs, linear_ys, label=str(type(my_linear_map)))
    plt.plot(xs, better_ys, label=str(type(my_better_map)))

    plt.xscale("log")
    plt.yscale("log")
    plt.title("hash performance")
    plt.xlabel("n")
    plt.ylabel("run time")
    plt.legend()
    plt.show()
    print("all finish")
