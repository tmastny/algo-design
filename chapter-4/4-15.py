# [5]
# (a) Give an efficient algorithm to find the second-largest key
#     among n keys. You can do better than 2n − 3 comparisons.
# (b) Then, give an efficient algorithm to find the third-largest
#     key among n keys. How many key comparisons does your algorithm
#     do in the worst case? Must your algorithm determine which key
#     is largest and second-largest in the process?

import random as rnd
from math import inf, log2, floor, ceil, inf
import heapq as hq

# heap construction is 2n - 2 * s(n) - 2 * e(n)
# where s(x) is sum of binary digits of x and e(x)
# is exponent of 2 in prime factorization of n

class MaxHeap():
    def __init__(self, array):
        max_array = [-1 * x for x in array]
        hq.heapify(max_array)
        self._heap = max_array

    def pop(self):
        return -1 * hq.heappop(self._heap)

    def push(self, item):
        return hq.heappush(self._heap, -1 * item)

    def __getitem__(self, key):
        return -1 * self._heap[key]

def max2_heap(array):
    heap = MaxHeap(array)

    if heap[1] > heap[2]:
        return heap[1]

    return heap[2]

def max3_heap(array):
    heap = MaxHeap(array)

    max3 = heap[3]
    for i in range(4, 7):
        if heap[i] > max3:
            max3 = heap[i]

    return max3

class Tournament:
    def __init__(self, s):
        self._results = self.play(s)

    def play(self, s):
        n = len(s)
        assert n % 2 == 0

        first_match = 2 ** ceil(log2(n) + 1)
        tourney = [-inf] * first_match
        for i in range(first_match - 1, n):
            tourney.append(s[i])

        match = first_match - 1
        while match > 0:
            for i in range(match // 2, match, 2):
                if s[i] > s[i + 1]:
                    swap(s, i, i // 2)
                else:
                    swap(s, i + 1, i // 2)

            match = match // 2

        max2_index = 1
        max2 = s[1]
        if s[0] == s[1]:
            max2 = s[2]
            max2_index = 2

        while max2_index < n:
            child = 2 * max2_index + 1
            if s[child] == s[0]:
                child += 1

            if s[child] > s[max2_index]:
                max2 = s[child]
                max2_index = child
            else:
                break

        return max2

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp



def max2_tournament(s):
    n = len(s)

    first_match = 2 ** ceil(log2(n) + 1)
    t = [-inf] * first_match
    match = first_match - 1
    for i in range(match // 2, match // 2 + n):
        t[i] = s[i - match // 2]

    while match > 0:
        for i in range(match // 2, match, 2):
            if t[i] > t[i + 1]:
                t[i // 2] = t[i]
            else:
                t[i // 2] = t[i + 1]

        match = match // 2

    max2 = -inf
    winner = 1
    while winner < len(t):
        opponent = winner + 1
        if t[winner] != t[0]:
            winner += 1
            opponent -= 1

        if t[opponent] > max2:
            max2 = t[opponent]

        winner = 2 * winner + 1

    return max2

def max2(array):
    max_el = max2_el = array[0]
    max_index = max2_index = 0

    for i in range(1, len(array)):
        if array[i] > max2_el:
            if array[i] > max_el:
                max2_index, max2_el = (max_index, max_el)
                max_index, max_el = (i, array[i])
            else:
                max2_index, max2_el = (i, array[i])

    return (max2_index, max2_el)

def max2_2(array):
    max_el = array[0]
    max_index = max2_index = 0

    for i in range(1, len(array)):
        if array[i] > max_el:
            max2_index, max2_el = (max_index, max_el)
            max_index, max_el = (i, array[i])

    max2_el_2 = max2_el
    max2_index_2 = max2_index
    for i in range(max_index + 1, len(array)):
        if array[i] > max2_el_2:
            max2_index_2, max2_el_2 = (i, array[i])

    if max2_el > max2_el_2:
        return (max2_index, max2_el)

    return (max2_index_2, max2_el_2)


if __name__ == "__main__":
    rnd.seed(666)

    array = [rnd.randint(0, 100) for i in range(0, 10)]

    print(array, end='\n\n')

    print("2n compare: {}".format(max2(array)), end='\n\n')

    print("2n compare better: {}".format(max2_2(array)), end='\n\n')

    print("heap2: {}".format(max2_heap(array)), end='\n\n')

    print("heap3: {}".format(max3_heap(array)), end='\n\n')

    print("tourney2: {}".format(max2_tournament(array)), end='\n\n')

    print("tourney2 redux: {}".format(max2_tournament(array)), end='\n\n')

    print("tourney3: {}".format(""), end='\n\n')
