# [3] Suppose you are given an array A of n sorted numbers
# that has been circularly shifted k positions to the right.
# For example, {35, 42, 5, 15, 27, 29} is a sorted array that
# has been circularly shifted k = 2 positions, while
# {27, 29, 35, 42, 5, 15} has been shifted k = 4 positions.
# • Suppose you know what k is. Give an O(1) algorithm to find
#   the largest number in A.
# • Suppose you do not know what k is. Give an O(lgn) algorithm
#   to find the largest number in A. For partial credit, you may give
#   an O(n) algorithm.

import random as rnd

def max_shift(a, k=None):
    maxi = len(a) - 1
    return a[(maxi + k) % len(a)]

def max_search(a):
    """
    If k > 0, then we have the following shift invariant:
    a[0] >= a[len(a) - 1]
    """
    if a[0] < a[len(a) - 1]:
        return a[len(a) - 1]

    return left_binary(a, 0, len(a) - 1)

def left_binary(a, lo, hi):
    n = (hi + lo) // 2
    if lo == n:
        return a[n]

    if a[lo] > a[n]:
        return left_binary(a, lo, n)
    else:
        return left_binary(a, n, hi)

if __name__ == "__main__":
    rnd.seed(3243)

    test_case1 = [35, 42, 5, 15, 27, 29]
    k1 = 2

    assert max_shift(test_case1, k1) == max(test_case1)
    assert max_search(test_case1) == max(test_case1)

    test_case2 = [27, 29, 35, 42, 5, 15]
    k2 = 4
    assert max_shift(test_case2, k2) == max(test_case2)
    assert max_search(test_case2) == max(test_case2)

    for i in range(100):
        max_k = 10
        a = [rnd.randint(0, 50) for i in range(max_k)]
        k = rnd.randint(0, max_k)

        a.sort()

        break
