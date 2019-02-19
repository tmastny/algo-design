# given an array of n integers, find the k largest
# http://forums.codeguru.com/showthread.php?508246-Find-largest-integers-in-array

import heapq as hq
import random as rd

def k_max(a, k):
    heap = a[:k]
    hq.heapify(heap)

    for i in range(k + 1, len(a)):
        if a[i] > heap[0]:
            hq.heapreplace(heap, a[i])

    return heap

if __name__ == "__main__":
    for i in range(100):
        rd.seed(4832)

        n = rd.randint(10, 20)
        a = [rd.randint(1, 20) for i in range(n)]

        k = rd.randint(1, n // 2)
        k_largest = k_max(a, k)

        a.sort()
        k_largest.sort()
        a_k = a[len(a) - k:]
        if a_k != k_largest:
            print("a: {}".format(a_k))
            print("k: {}".format(k_largest))

        break
