
import random
import sys

from index_search import Tree

class Bins(Tree):
    def __init__(self, weight = None):
        super().__init__(weight)

    def best_fit(self, weight):
        if self.head.data == None:
            self.head.data = weight
            return()

        this_bin_capacity = weight + self.head.data
        if this_bin_capacity > 1:
            if self.head.left == None:
                self.head.left = Bins()

            return(self.head.left.best_fit(weight))

        if self.head.right == None:
            self.head.data = this_bin_capacity
            return()

        next_bin_capacity = weight + self.head.right.data

        if next_bin_capacity > 1:
            self.head.data = this_bin_capacity
            return()

        if next_bin_capacity > this_bin_capacity:
            return(self.head.right.best_fit(weight))

    def worst_fit(self, weight):
        return()


def pack_bins(weights, best_fit=True):
    bins = Bins()

    if best_fit:
        method = bins.best_fit
    else:
        method = bins.worst_fit

    for weight in weights:
        method(weight)

    return(bins.length())

if __name__ == '__main__':
    random.seed(1)
    weights = [random.random() for i in range(0, 10)]

    print(' '.join(["{0:0.2f}".format(i) for i in weights]))

    print(pack_bins(weights))
    print(pack_bins(weights))

    print(sum(weights))
