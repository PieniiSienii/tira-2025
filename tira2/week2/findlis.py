def find_sequence(numbers):
    result = {}

    subsequence = []
    for i in range(len(numbers)):
        result[i] = [numbers[i]]
        for j in range(i):
            if numbers[j] < numbers[i] and len(result[i]) < len(result[j])+1:
                result[i] = result[j].copy()
                result[i].append(numbers[i])
        if len(result[i]) > len(subsequence):
            subsequence = result[i]

    
    return subsequence


if __name__ == "__main__":
    print(find_sequence([1, 2, 3])) # [1, 2, 3]
    print(find_sequence([3, 2, 1])) # [1]
    print(find_sequence([1, 1, 1, 1, 1])) # [1]

    print(find_sequence([1, 8, 2, 7, 3, 6])) # [1, 2, 3, 6]
    print(find_sequence([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find_sequence([4, 1, 5, 6, 3, 4, 3, 8])) # [1, 3, 4, 8] 