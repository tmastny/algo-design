# [3] Give an efficient algorithm to rearrange an array
# of n keys so that all the negative keys precede all
# the nonnegative keys. Your algorithm must be in-place,
# meaning you cannot allocate another array to temporarily
# hold the items. How fast is your algorithm?

import random as rnd

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partition(a, lo, hi):
    pivot = hi
    first_high = lo
    for i in range(lo, hi):
        if a[i] < a[pivot]:
            swap(a, i, first_high)
            first_high += 1

    swap(a, first_high, pivot)

    return pivot

def partition0(a):
    first_high = 0
    for i in range(len(a)):
        if a[i] < 0:
            swap(a, i, first_high)
            first_high += 1

def part(a):
    partition0(a)

def parted(a):
    i = 0
    while i < len(a) and a[i] < 0:
        i += 1

    while i < len(a) and a[i] >= 0:
        i += 1

    return i == len(a)


if __name__ == "__main__":
    rnd.seed(1111)

    if not parted([-1, 1, 1, 1]) and parted([-1, -1, 1]):
        print("not parted")

    for i in range(100):
        length = 11
        if i % 2 == 0:
            length = 10

        array = [rnd.randint(-100, 100) for i in range(100 * (i + 1) + (i % 2))]

        part(array)

        if not parted(array):
            print(array)
            break
