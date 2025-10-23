def count_rounds(numbers):
  indexes = {number: ind for ind, number in enumerate(numbers)}
  result = 1
  a = 1

  for i in range(2,len(numbers)+1):
    if indexes[i] < indexes[i-1]:
      result += 1
  return result
if __name__ == "__main__":
    print(count_rounds([2,1])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000