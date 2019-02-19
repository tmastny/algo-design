import heapq
import random

def k_smallest(array, k):
    heapq.heapify(array)

    k_smallest = []
    for i in range(k):
        k_smallest.append(heapq.heappop(array))

    return k_smallest

if __name__ == "__main__":
    random.seed(48)
    array = [random.randint(0, 20) for i in range(0, 20)]
    print(array)
    print(k_smallest(array, 5))
