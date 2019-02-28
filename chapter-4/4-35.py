# [5]Suppose that you are given a sorted sequence of distinct
# integers {a1, a2, ..., an}. Give an O(lgn) algorithm to
# determine whether there exists an indexi such as ai = i.
# For example, in {−10,−3,3,5,7}, a3 = 3. In {2,3,4,5,6,7},
# there is no such i.

def matching_i(a):
    return

if __name__ == "__main__":
    test1 = [-10, -3, 2, 5, 7]
    assert matching_i(test1) == 2

    test2 = [2,3,4,5,6,7]
    assert matching_i(test2) == -1
