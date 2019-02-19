# 4-14. [5] Give an O(n log k)-time algorithm that merges
# k sorted lists with a total of n elements into one sorted list.
# (Hint: use a heap to speed up the elementary O(kn)- time algorithm).

# Consider worst case:
# [[1, 2, 3, 4], [1], [1]]
# if we start from left to right as in the naive case, we process
# O(2 * 4) times. We have to process all of [1, 2, 3, 4] to add in [1]
# and then process all of [1, 1, 2, 3, 4] to add in the last [1].

# Option 1. Process smallest lists first. We could sort
# the k_list by length of array:
# [[1], [1], [1, 2, 3, 4]]
# Then we will have
# [1, 1] -> [1, 1, 1, 2, 3, 4]
# This is roughly 2 + (4 + 2) comparisons.
#
# As we increase the smaller arrays, this becomes more efficient.
# However, this doesn't help the average case:
#
# Average case:
# [[1, 2], [3, 4], [5, 6]]
# [1, 2, 3, 4] -> [1, 2, 3, 4, 5, 6]

# Option 2: insert each element from the k list into a heap.
# This would take 0(n) steps, by first concatenating all the lists
# at 0(n) and then heapifying at O(n).
# However, extracting out the minimum elements to merge is O(n log n).
# This method doesn't take advantage of the fact that the lists are
# already pre-sorted.

# second,



# Example: suppose we have n = 20 elements in total in k = 10 sorted arrays.
# Then len(array) = 2.
# M(1) = 2 + 2 = 4
# M(2) = 4 + 2 = 6
# M(i) = M(i - 1) + 2
#      = 2 * i + 2
# ...
# M(9) = 9 * 2 + 2
# Sum i = 1 to 9, (2 * i + 2s) ~= 10 * 20 / 2

import random
from collections import deque
import heapq as hq

def merge2(q1, q2):
    temp = deque()
    while len(q1) or len(q2):
        if not len(q2):
            temp.append(q1.popleft())
        elif not len(q1):
            temp.append(q2.popleft())
        elif q1[0] > q2[0]:
            temp.append(q2.popleft())
        else:
            temp.append(q1.popleft())

    return temp

def merge(k_lists):

    merged = deque(k_lists[0])
    n = 1
    while n < len(k_lists):
        to_merge = deque(k_lists[n])
        merged = merge2(to_merge, merged)
        n += 1

    return list(merged)

def set_queue(lists):
    return [deque(ith_list) for ith_list in lists]

def merge_all(k_lists):
    k_lists = set_queue(k_lists)
    hq.heapify(k_lists)

    merged = []
    while len(k_lists) > 0:
        smallest = hq.heappop(k_lists)
        merged.append(smallest.popleft())

        if len(smallest) > 0:
            hq.heappush(k_lists, smallest)

    return merged

if __name__ == "__main__":
    random.seed(94)

    k = 10
    k_lists = []
    for i in range(k):
        random_length = random.randint(1, 10)
        k_lists.append(
            sorted([random.randint(0, random_length) for i in range(random_length)])
        )

    print(k_lists, end='\n\n')

    print(merge(k_lists), end='\n\n')

    print(merge_all(k_lists), end='\n\n')


# import heapq as hq
# a = [
#     (3, [3, 5]),
#     (1, [5, 1000]),
#     (5, [5, 13]),
#     (5, [5, 32]),
#     (1, [1, 1, 2])
# ]
# a = [
#     {3: [3, 5]},
#     {1: [5, 1000]},
#     {5: [5, 13]},
#     {5: [5, 32]},
#     {1: [1, 1, 2]}
# ]
# a = [
#     deque([1, 1]),
#     deque([1, 1])
# ]
# b = a[1:]
# hq.heapify(b)
# hq.heappop(b)
