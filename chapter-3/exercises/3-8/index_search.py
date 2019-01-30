from random import shuffle

class Node:
    def __init__(self, data=None):
        self.data = data

        self.parent = None
        self.right = None
        self.n_right = 0

        self.left = None
        self.n_left = 0

class Tree:
    def __init__(self, data=None):
        self.head = Node()

    def insert(self, data):
        if self.head.data == None:
            self.head.data = data
            return()

        if self.head.data > data:
            self.head.n_left += 1

            if self.head.left is None:
                self.head.left = Tree()
            self.head.left.insert(data)
        else:
            self.head.n_right += 1

            if self.head.right is None:
                self.head.right = Tree()
            self.head.right.insert(data)

    def kth_smallest(self, k):
        #        3
        #       /  \
        #      2    4
        #     /     / \
        #    1     6   5
        #
        # Find 4th smallest
        # 3.n_left = 2
        # 3.n_right = 3
        # => 3 is the third smallest
        # => we need to go bigger, so
        # recurse into 3.right

        if self.head == None:
            return()

        n_smaller = self.head.n_left
        count_of_head = 1

        assert k > 0
        assert k <= n_smaller + count_of_head + self.head.n_right

        if k == n_smaller + count_of_head:
            return(self.head.data)

        if k > n_smaller + count_of_head:
            return(
                self.head.right.kth_smallest(k - (n_smaller + count_of_head))
            )
        else:
            return(
                self.head.left.kth_smallest(k)
            )

    def traverse(self, print_nodes=True, array = None):
        if self.head is not None:
            left = self.head.left
            if left is not None:
                self.head.left.traverse(print_nodes=print_nodes, array=array)

            if array is not None:
                array.append(self.head.data)

            if print_nodes:
                print(self.head.data)

            right = self.head.right
            if right is not None:
                self.head.right.traverse(print_nodes=print_nodes, array=array)

    def length(self):
        a = []
        self.traverse(print_nodes=False, array = a)
        return(len(a))


if __name__ == '__main__':
    tree = Tree()
    elements = list(range(0,9))
    shuffle(elements)

    for el in elements:
        print(el)
        tree.insert(el)

    print()
    tree.traverse()
    print()

    kth = tree.kth_smallest(8)
    print(kth)
