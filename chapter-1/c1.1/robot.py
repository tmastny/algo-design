# Problem: Robot Tour Optimization
# Input: A set S of n points in the plane.
# Output: What is the shortest cycle tour that visits each point in the set S?

def euclidean_distance:
    return()

def nearest_neighbor(S, index):
    if len(S) == 1:
      return(S[0])

    min_distance = euclidean_distance(index, S[1])
    index_of_min = 1
    for i in range(2, len(S)):
        if i == index:
            continue

        new_distance = euclidean_distance(index, S[i])
        if new_distance < min_distance:
            min_distance = new_distance
            index_of_min += 1

    return(S[index_of_min])

def visit_points(S):
    # need a collection of visited points
    # so I don't return
    return()
