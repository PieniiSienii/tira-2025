def count_steps(numbers):
  nums = {n: i for i, n in enumerate(numbers)}

  sorted_nums = sorted(nums.items(), key=lambda x: x[0])

  counter = abs(sorted_nums[0][1])
  for n in range(len(sorted_nums)-1):
    counter += abs(sorted_nums[n][1]- sorted_nums[n+1][1])

  return counter


if __name__ == "__main__":
    print(count_steps([1])) # 0
    print(count_steps([1, 2, 3])) # 2
    print(count_steps([3, 2, 1])) # 4
    print(count_steps([42, 1337, 1, 10**9])) # 7
    print(count_steps([1, 3, 5, 7, 8, 6, 4, 2])) # 28
    print(count_steps([10**6, 10**8, 10**7, 10**9])) # 5

    numbers = [(x * 999983) % 10**9 + 1 for x in range(10**5)]
    print(count_steps(numbers)) # 4871908997