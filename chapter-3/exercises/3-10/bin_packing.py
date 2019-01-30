
import random
import sys

sys.path.append('../3-8')

from index_search import Tree

class Bins(Tree):
    def __init__(self, weight = None):
        super().__init__(weight)

    def best_fit(self, weight):
        if self.head == None:
            self.head = Bins(weight)

        this_bin_capacity = weight + self.head.data
        if this_bin_capacity > 1:
            if self.head.left == None:
                self.head.left = Bins()

            return(self.head.left.best_fit(weight))

        if self.head.right == None:
            return()

        next_bin_capacity = weight + self.head.right.data

        if next_bin_capacity > 1:
            return()

        if next_bin_capacity > this_bin_capacity:
            return(self.head.right.best_fit(weight))

    def length(self):
        return(
            self.head.n_left + self.head.n_right + 1
        )

def pack_bins(weights, best_fit = True):
    bins = Bins()

    if best_fit:
        method = bins.best_fit

    for weight in weights:
        method(weight)

    return(bins.length())

if __name__ == '__main__':
    random.seed(1)
    weights = [random.random() for i in range(0, 10)]

    print(' '.join(["{0:0.2f}".format(i) for i in weights]))

    pack_bins(weights)

    print()
