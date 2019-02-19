# [3] A company database consists of 10,000 sorted names,
# 40% of whom are known as good customers and who together
# account for 60% of the accesses to the database. There are
# two data structure options to consider for representing the database:
# • Put all the names in a single array and use binary search.
# • Put the good customers in one array and the rest of them in a second array.
#   Only if we do not find the query name on a binary search of the first array
#   do we do a binary search of the second array.
#
# Demonstrate which option gives better expected performance.
# Does this change if linear search on an unsorted array is used
# instead of binary search for both options?

# Good customers = 40% * 10,000 = 4000
# Represent 60% of accesses

from math import log2, floor

def log2_2(n):
    return floor(log2(n))

if __name__ == "__main__":
    total_names = 10000
    good_customers = 0.4 * total_names

    print("Search for a particular name: {}".format(log2_2(10000)))
    print(
        """
***
Failed search: log2(4000) = {}
Search through secondary names: log2(6000) = {}
Total: {}
        """.format(
            log2_2(good_customers),
            log2_2(total_names - good_customers),
            log2_2(good_customers) + log2_2(total_names - good_customers)
        )
    )
    print("Expected cost: 60% of first search is successful, therefore:")
    print("log2(4000) + 40% log2(6000) =")
    print("{} + {} * {} = {}".format(
        log2_2(4000), 0.4, log2_2(6000), log2_2(4000) + 0.4 * log2_2(6000)
    ))

    print("\nTherefore, everytime it is better simply to search through the entire array")
    print("\n****************\n")
    print("Next, consider we do linear search on two unsorted arrays")
    print("First, the expected cost is n / 2 = 10000 / 2 = {}".format(10000 // 2))
    print()
    print("Then, in the second case:")
    print("4000 / 2 + 0.4 * 6000 / 2 = {}".format(4000 // 2 + 0.4 * 6000 // 2))
    print("Therefore, the second method is more performant.")
