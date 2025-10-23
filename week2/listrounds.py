def find_rounds(numbers):
    indexes = {number: ind for ind, number in enumerate(numbers)}
    result = []
    a = 1

    for i in range(len(numbers)):
      round = []

      while True:
        round.append(a)
        numbers.remove(a)

        if not numbers: 
          result.append(round)
          return result
        
        if indexes[a+1] > indexes[a]:
          a += 1

        else:
          a += 1
          break

      result.append(round)
    return result

if __name__ == "__main__":
    # print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]