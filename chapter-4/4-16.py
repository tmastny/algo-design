


import random as rnd
from statistics import median


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def quicksort(array, lo, hi):
    if hi - lo > 0:
        p = partition(array, lo, hi)
        qselect(array, lo, p - 1)
        qselect(array, p + 1, hi)

def qselect(array, lo, hi):
    n = len(array)
    mid = (n - 1) // 2

    if hi - lo <= 0:
        if n % 2 == 1:
            return array[mid]
        else:
            return (array[mid] + array[mid + 1]) / 2


    p = partition(array, lo, hi)
    if p <= mid:
        return qselect(array, p + 1, hi)
    else:
        return qselect(array, lo, p - 1)


def partition(array, lo, hi):
    pivot = array[hi]
    first_high = lo
    for i in range(lo, hi):
        if array[i] < pivot:
            swap(array, i, first_high)
            first_high += 1

    swap(array, first_high, hi)

    return first_high

def qmedian(array):
    if len(array) == 1:
        return array[0]

    rnd.shuffle(array)

    return qselect(array, 0, len(array) - 1)

if __name__ == "__main__":
    rnd.seed(843)
    for i in range(100):
        length = 11
        if i % 2 == 0:
            length = 10

        array = [rnd.randint(0, 100) for i in range(100 * (i + 1) + (i % 2))]

        m1 = median(array)
        m2 = qmedian(array)

        if m1 != m2:
            print(i)
            print(array)
            print(m1, m2, m3)
            print(median(array), qmedian(array))
            break
