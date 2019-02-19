# [5] Assume that the array A[1..n] only has numbers from {1, . . . , n2 }
# but that at most log log n of these numbers ever appear. Devise an algorithm
# that sorts A in substantially less than O(n log n).

import random as rnd
from math import log2, ceil

def dsort(a):
    num = []
    count = []
    for el in a:
        if el not in num:
            num.append(el)
            count.append(0)

        count[num.index(el)] += 1

    for i in range(1, len(num)):
        j = i
        while j > 0 and num[j - 1] > num[j]:
            swap(num, j, j - 1)
            swap(count, j, j - 1)
            j -= 1

    ai = 0
    for i in range(len(num)):
        for j in range(count[i]):
            a[ai] = num[i]
            ai += 1


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def is_sorted(a):
    return all([a[i] <= a[i + 1] for i in range(len(a) - 1)])

if __name__ == "__main__":
    rnd.seed(32432)
    for i in range(100):
        n = rnd.randint(50, 100)
        k = [rnd.randint(1, n**2) for i in range(ceil(log2(log2(n))))]

        a = [rnd.choice(k) for i in range(n)]

        dsort(a)

        if not is_sorted(a):
            print(a)

        # break
