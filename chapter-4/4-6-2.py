import random

def pair_sum_brute(x, s1, s2):
    for el1 in s1:
        for el2 in s2:
            if el1 + el2 == x:
                return True

    return False

def pair_sum2(x, s1, s2):
    s1.sort()
    s2.sort()

    n = len(s1)

    i = 0
    j = n - 1
    while i < n and j >= 0:
        if s1[i] + s2[j] > x:
            j -= 1
        elif s1[i] + s2[j] < x:
            i += 1
        else:
            return True
    return False


def binary_search(x, s):
    n = len(s)
    if n == 0:
        return False

    if x == s[n // 2]:
        return True
    elif x > s[n // 2]:
        return binary_search(x, s[n // 2 + 1:])
    else:
        return binary_search(x, s[:n // 2])

def pair_sum3(x, s1, s2):
    s1.sort()
    for el in s2:
        if binary_search(x - el, s1):
            return True

    return False

def pair_sum4(x, s1, s2):
    n = len(s1)
    assert n == len(s2)

    seen_numbers = set()
    for i in range(n):
        if x - s1[i] in seen_numbers:
            return True
        else:
            seen_numbers.add(s1[i])

        if x - s2[i] in seen_numbers:
            return True
        else:
            seen_numbers.add(s2[i])

    return False

if __name__ == "__main__":
    random.seed(358)

    fns = [pair_sum_brute, pair_sum2, pair_sum3, pair_sum4]

    pairs = [
        (10, [7, 100, 200, 300, 400, 500] ,[1, 2, 2, 2, 2, 3]),
        (15, [0, 9, 10], [0, 6, 7]),
        (15, [0, 9, 10], [5, 7, 9])
    ]

    for fn in fns:
        for pair in pairs:
            print(fn(*pair), end='')

        print()

    number_of_pairs = 0
    for fn in fns:
        for i in range(0, 100):
            pairs = (
                random.randint(-200, 200),
                [random.randint(-100, 100) for i in range(0, 100)],
                [random.randint(-100, 100) for i in range(0, 100)]
            )
            if not fn(*pair):
                print("error")
            else:
                number_of_pairs += 1

    print(number_of_pairs)
