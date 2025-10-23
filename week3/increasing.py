def count_sublists(numbers):
  total = 0
  sublist = 1

  for i in range(1, len(numbers)):
      if numbers[i] > numbers[i - 1]:
          sublist += 1
      else:
          total += sublist * (sublist + 1) // 2
          sublist = 1

  total += sublist * (sublist + 1) // 2
  return total


if __name__ == "__main__":
  print(count_sublists([2, 1, 3, 4]))  # 7
  print(count_sublists([1, 2, 3, 4]))  # 10
  print(count_sublists([4, 3, 2, 1]))  # 4
  print(count_sublists([1, 1, 1, 1]))  # 4
  print(count_sublists([1, 2, 1, 2]))  # 6

  numbers = list(range(1, 10**5 + 1))
  print(count_sublists(numbers))  # 5000050000