def count_splits(sequence):
  sequence = [int(n) for n in sequence]
  ones = sequence.count(1)
  zeros = sequence.count(0)
  left_zeros = 0
  left_ones = 0
  ans = 0

  for i in range(len(sequence)-1):
    if sequence[i] == 1:
      left_ones += 1
    else:
      left_zeros += 1
    right_zeros = zeros - left_zeros
    right_ones = ones - left_ones
    if left_ones == left_zeros and right_zeros == right_ones:
      ans += 1
  return ans
if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999