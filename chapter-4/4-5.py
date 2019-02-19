

def mode_sort(array):
    array.sort()

    run_index = 0
    max_run = 0
    run = 0
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            run += 1
        elif run > max_run:
            max_run = run
            run_index = i - 1

    return array[run_index]

def mode(array):
    count = {}
    for el in array:
        count[el] = count.get(el, 0) + 1

    max = 0
    max_element = None
    for key, value in count.items():
        if value > max:
            max = value
            max_element = key

    return max_element

if __name__ == "__main__":
    test_array = [4, 6, 2, 4, 3, 1]
    print(mode(test_array))
