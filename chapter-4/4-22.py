# [3] Show that n positive integers in the range 1 to k
# can be sorted in O(nlogk) time. The interesting case is when k << n.

import random as rnd

def dsort(a):
    nums = dict()
    for el in a:
        nums[el] = nums.get(el, 0) + 1

    i = 0
    for key, value in nums.items():
        for v in range(value):
            a[i] = key
            i += 1

def count_sort(a, k = None):
    if k:
        count = [0] * (k + 1)
    else:
        count = [0] * (max(a) + 1)


    for el in a:
        count[el] += 1

    i = 0
    for j in range(len(count)):
        for p in range(count[j]):
            a[i] = j
            i += 1

def is_sorted(a):
    return all([a[i] <= a[i + 1] for i in range(len(a) - 1)])

if __name__ == "__main__":
    rnd.seed(47888)
    for i in range(100):
        n = rnd.randint(20, 100)
        k = rnd.randint(n // 4, n // 2)
        a = [rnd.randint(0, k) for i in range(n)]

        count_sort(a, k)


        if not is_sorted(a):
            print(a)
            break
