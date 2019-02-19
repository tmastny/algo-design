import random
from collections import deque

def doc():
    """
    [3]
    Given two sets S1 and S2 (each of size n), and a number x,
    describe an O(n log n) algorithm for finding whether
    there exists a pair of elements, one from S1 and one from S2,
    that add up to x. (For partial credit, give a Θ(n2) algorithm for this problem.)
    """
    return

def pair_sum_pos(x, s1, s2):
    """
    Edge case: negative numbers
    """
    n = len(s1)
    assert n == len(s2)

    s1.sort()
    s2.sort()

    # s3 = [7, 100, 200, 300, 400, 500]
    # s4 = [1, 2, 2, 2, 2, 3]
    # x = 10

    # s1 = [0, 9, 10]
    # s2 = [5, 7, 9]

    # s1 = [0, 9, 10]
    # s2 = [0, 6, 7]
    # x = 15

    # what if we merged the lists?
    # s1, s2 -> [0, 0, 6, 7, 9, 10]
    #        -> [1, 2, 2, 2, 1, 1]
    # the problem is the pair must come
    # from both s1 and s2

    # during the merge we work with every element
    # of both arrays. We could test equality during the merge
    # portion of the algorithm


    i = 0
    j = 0
    while True:
        if i >= n - 1 and j >= n - 1:
            return False

        i = min(n - 1, i)
        j = min(n - 1, j)

        # infinite loop around i -> n - 1 -> n
        if s1[i] + s2[j] == x:
            return True

        if i <= j and i + 1 <= n - 1 and s1[i + 1] + s2[j] <= x:
            i += 1
        elif j + 1 <= n - 1 and s1[i] + s2[j + 1] <= x:
            j += 1
        else:
            i += 1


# s1 = [0, 9, 10]
# s2 = [5, 7, 9]
# [0, 5, 7, 9, 9, 10]
# [1, 2, 2, 1, 2, 1]
# this example demostrates the problem of just using the merge step.
# not every element is compared, which means it can skip over the
# correct implementation. I think I need to write mergesort from stratch and
# test the pair_sum during every comparison.

# s1 = [0, 9, 10]
# s2 = [0, 6, 7]
# x = 15

def merge_pair_sum(x, s1, s2):
    s1.sort()
    s2.sort()

    s1 = deque(s1)
    s2 = deque(s2)

    last1 = s1.popleft()
    last2 = s2.popleft()
    while len(s1) > 0 or len(s2) > 0:
        if last1 + last2 == x:
            return True

        if last1 > last2 and len(s2) > 0:
            last2 = s2.popleft()
        elif len(s1) > 0:
            last1 = s1.popleft()

    return False

def brute_pair_sum(x, s1, s2):
    for el1 in s1:
        for el2 in s2:
            if el1 + el2 == x:
                return True

    return False

if __name__ == "__main__":
    random.seed(48)
    s1 = [random.randint(0, 10) for i in range(0, 10)]
    s2 = [random.randint(0, 10) for i in range(0, 10)]
    print(sorted(s1))
    print(sorted(s2))

    x = random.randint(0, 20)



    print()
    print()
    print(x, pair_sum_pos(x, s1, s2), brute_pair_sum(x, s1, s2))
    print(17, pair_sum_pos(17, s1, s2), brute_pair_sum(17, s1, s2))
    print(10, pair_sum_pos(10, [7, 9], [2, 3]), brute_pair_sum(10, [7, 9], [2, 3]))

    s3 = [7, 100, 200, 300, 400, 500]
    s4 = [1, 2, 2, 2, 2, 3]
    print(10, pair_sum_pos(10, s3, s4), brute_pair_sum(10, s3, s4))


    # test case:
    # can't just iterate through s1 checking first element of s2
    # it will skip over intermediate s2[1] and s1[1]
    s1 = [0, 9, 10]
    s2 = [0, 6, 7]
    x = 15
    print(x, pair_sum_pos(x, s1, s2), brute_pair_sum(x, s1, s2))

    print()
    print()
    for i in range(0, 100):
        s1 = [random.randint(0, 10) for i in range(0, 10)]
        s2 = [random.randint(0, 10) for i in range(0, 10)]
        x = random.randint(0, 20)

        smart = pair_sum_pos(x, s1, s2)
        naive = brute_pair_sum(x, s1, s2)
        if smart != naive:
            print("iteration: {}. x: {}".format(i, x))
            print("brute: {}. pos: {}".format(smart, naive))
            print(sorted(s1))
            print(sorted(s1))
            break
