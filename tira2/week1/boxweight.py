import itertools
def min_count(weights, max_weight):
    if len(weights) == 0:
        return 0
    if max(weights) > max_weight:
        return -1
    min_boxes = float("inf")
    for permutation in itertools.permutations(weights):
        curr_weight = 0
        counter = 1
        for weight in permutation:
            if curr_weight + weight <= max_weight:
                curr_weight += weight
            else:
                counter += 1
                curr_weight = weight
        if counter <= min_boxes:
            min_boxes = counter
    return min_boxes
if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3