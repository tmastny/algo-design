import random
from binary_search_tree import BinarySearchTree, TreeNode
import numpy as np

class Bins(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def put(self, key, value):
        """ add a new mapping between key and value to the BST """
        if self.root:
            self.root.put(key, value)
        else:
            self.root = Bin(key, value)

    def fit(self, weight, best=True):
        if not self.root:
            self.put(weight, True)
            return()

        if best:
            method = self.root.find_best_fit
        else:
            method = self.root.find_worst_fit

        bin = method(weight)
        if bin:
            self.delete(bin)
            self.put(bin + weight, True)
        else:
            self.put(weight, True)


class Bin(TreeNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find_best_fit(self, weight):
        this_capacity = self.key + weight
        if this_capacity > 1:
            return(self._fit_over_capacity(weight))

        larger_bin = self.right
        if larger_bin:
            larger_capacity = larger_bin.key + weight
            if larger_capacity < 1:
                return(larger_bin.find_best_fit(weight))

        return(self.key)

    def find_worst_fit(self, weight):
        this_capacity = self.key + weight
        if this_capacity > 1:
            return(self._fit_over_capacity(weight))

        min_bin = self._findMin(self)[0]
        return(min_bin.key)

    def _fit_over_capacity(self, weight):
        smaller_bin = self.left
        if smaller_bin:
            return(smaller_bin.find_best_fit(weight))


        return(self.put(weight, True))

def pack_bins(weights, best_fit=True):
    bins = Bins()

    for weight in weights:
        bins.fit(weight, best_fit)

    count = 0
    for bin in bins:
        count += 1

    return(count)

def naive_best_fit(weights, best_fit=True):
    bins = []
    for weight in weights:
        if len(bins) == 0:
            bins.append(weight)
            continue

        max = -1
        max_index = 0
        for i in range(len(bins)):
            new_capacity = bins[i] + weight
            if new_capacity > max and new_capacity < 1:
                max = new_capacity
                max_index = i


        if max == -1:
            bins.append(weight)
        else:
            bins[max_index] += weight

    return(len(bins))


def pack_mean(best_fit=True, naive=False, no_method=False):
    method = pack_bins
    if naive:
        method = naive_best_fit

    if no_method:
        method = lambda x, y: sum(x)

    number_of_bins = []
    for i in range(0, 100):
        number_of_bins.append(
            method([random.random() for i in range(0, 100)], best_fit)
        )

    return(sum(number_of_bins) / len(number_of_bins))


if __name__ == "__main__":
    random.seed(1)
    weights = [random.random() for i in range(0, 10)]

    print(' '.join(["{0:0.2f}".format(i) for i in weights]))

    print("Tree Best fit: {}".format(pack_bins(weights)))
    print("Array Best fit: {}".format(naive_best_fit(weights)))
    print("Tree Worst fit: {}".format(pack_bins(weights, False)))

    print("Lower Bound: {0:0.1f}".format(sum(weights)))
    print()
    print()

    print('Average tree best fit: {}'.format(pack_mean()))
    print('Average array best fit: {}'.format(pack_mean(True, True)))
    print('Average tree worst fit: {}'.format(pack_mean(False)))
    print('Lower bound: {}'.format(pack_mean(True, True, True)))
