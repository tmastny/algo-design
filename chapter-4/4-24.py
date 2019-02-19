# [5] Let A[1..n] be an array such that the first n − √n
# elements are already sorted (though we know nothing about
# the remaining elements). Give an algorithm that sorts A
# in substantially better than n log n steps.

import random as rnd
from math import sqrt, floor
from collections import deque

def finish_sort(a):
    i = 0
    while i < len(a) - 1 and a[i] <= a[i + 1]:
        i += 1

    merged = a[:i]

    to_merge = a[i:]
    to_merge.sort()

    merged = deque(merged)
    to_merge = deque(to_merge)

    j = 0
    temp = []
    while len(merged) > 0 or len(to_merge) > 0:
        if not len(merged):
            temp.append(to_merge.popleft())
        elif not len(to_merge):
            temp.append(merged.popleft())
        elif merged[0] <= to_merge[0]:
            temp.append(merged.popleft())
        else:
            temp.append(to_merge.popleft())

    return temp


def is_sorted(a):
    return all([a[i] <= a[i + 1] for i in range(len(a) - 1)])

if __name__ == "__main__":
    rnd.seed(38222)

    for i in range(100):
        n = rnd.randint(20, 50)
        sqrtn = floor(sqrt(n))

        a = [rnd.randint(0, 100) for i in range(n - sqrtn)]
        a.sort()

        a += [rnd.randint(0, 100) for i in range(sqrtn)]

        a = finish_sort(a)
        if not is_sorted(a):
            print(a)
            break

        # break
