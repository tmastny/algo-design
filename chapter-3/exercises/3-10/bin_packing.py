
import random
import sys

from index_search import Tree

class Bins(Tree):
    def __init__(self, weight = None):
        super().__init__(weight)

    def put_in_smaller_bin(self, weight):
        if self.head.left == None:
            self.head.left = Bins()
        return(self.head.left.best_fit(weight))

    def put_in_this_bin(self, weight):
            self.head.data += weight
            return()

    def best_fit(self, weight):
        # this method currently does not maintain tree order.
        # This method searchs for the right node to bin the weight,
        # but after adding to the bin, the previous tree order could be
        # broken.
        #
        # Therefore, after the right node is found, the node must be deleted
        # and a new node with the new weight must be insert to maintain tree
        # order.
        #
        # This procedure maintans O(log(n)) operations.

        if self.head.data == None:
            self.head.data = weight
            return()

        this_bin_capacity = weight + self.head.data
        if this_bin_capacity > 1:
            return(self.put_in_smaller_bin(weight))

        if self.head.right == None:
            self.put_in_this_bin(weight)
            return()

        next_bin_capacity = weight + self.head.right.data

        if next_bin_capacity > 1:
            self.put_in_this_bin(weight)
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
    #print(pack_bins(weights))

    print(sum(weights))
