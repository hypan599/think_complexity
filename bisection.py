import os
import timeit


def etime():
    user, sys, chuser, chsys, real = os.times()
    return user + sys


def bisection(_list, target):
    start = 0
    end = len(_list) - 1
    if end < 0:
        return "empty list"
    while True:
        if end - start + 1 % 2 == 0:  # even number
            if target <= _list[(start + end - 1) / 2]:
                end = (start + end - 1) // 2
            elif target >= _list[(start + end + 1) / 2]:
                start = (start + end + 1) // 2
            else:
                return "no"
        else:
            if _list[(start + end) // 2] == target:
                return "yes"
            elif end - start == 0:
                return "no"
            elif _list[(start + end) // 2] > target:
                end = (start + end) // 2 - 1
            else:
                start = (start + end) // 2 + 1


#  much more effective version
# seems faster
def bisection2(list, target):
    start = 0
    end = len(list)
    while start < end:
        mid = (start + end) // 2
        if list[mid] == target:
            return "yes"
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid
    return "no"


def time_search(func, my_list, target):
    smtp = "%s(%s, %s)" % (func.__name__, my_list.__repr__(), target.__repr__())
    setup = "from __main__ import %s" % func.__name__
    print(timeit.timeit(smtp, setup=setup, number=10000))


if __name__ == '__main__':
    time_search(bisection2, range(0, 10 ** 8, 2), 100007)
