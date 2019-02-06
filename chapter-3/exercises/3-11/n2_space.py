import random
from binary_search_tree import BinarySearchTree

class QuickDictMin:
    def __init__(self, a):
        self._dict = self._init_dict(a)


    def _init_dict(self, a):
        d = {}
        for i in range(len(a)):
            d[(i, i)] = a[i]

            min = a[i]
            for j in range(i + 1, len(a)):
                if min > a[j]:
                    min = a[j]
                d[(i, j)] = min

        return d

    def find_min(self, i, j):
        return self._dict[(i, j)]

class QuickTreeMin:
    def __init__(self, a):
        self._tree = self._init_tree(a)
        # what if we had two trees
        # one for indices
        # one for values

        # two trees with key, value pairs:
        # value is index for other tree

        # find_min
        #   while left.value >= i or left.value <= j

    def _init_tree(self, a):
        tree = BinarySearchTree()
        for i in range(len(a)):
            tree.put(i, a[i])

        return tree

    def find_min(self, i, j):
        # let's start small
        # suppose we are trying to find (1, 1) or index 1

        # then we could build an index_tree and find value
        # associated at key == 1

        # adjacent keys: (1, 2)
        # look up both keys and find the min

        # range keys: (0, 2)
        # example: [0.75, 0.25, 0.9]

        # what if we build out the normal tree
        #   0.75                0
        #   /   \       ->     / \
        #  0.25  0.9          1   2
        # and then replaced the keys with the indices.
        # or equivalently, the value is the key and the
        # index is the value. But then you want to do a
        # search/find_min on the value.

        #  [0.9, 0.75, 0.25, 0.91]
        #   0.75                1             2
        #   /   \       ->     / \      ->   / \
        #  0.25  0.9          2   0         1   4
        #         \                \       /   / \
        #         0.91              3     0   3   5

        # use index_tree
        #   tree.add(i, a[i])
        #
        # Find j index: log(n)
        #   go up to root*, maintaining min pointer to value: log(n)
        #   go down to i index, maintaining min pointer to value: log(n)
        # return min
        #
        # *may find i on way up to root, end early
        # *may not go up to root: only go up until i < "root"

        return self._find_min_root(self, tree.root)


if __name__ == "__main__":
    random.seed(1)
    rand = [random.random() for i in range(0, 10)]
    print(rand)

    seq = QuickDictMin(rand)

    min = seq.find_min(1, 4)

    print()
    print(seq._dict)
    print()
    print(min)
