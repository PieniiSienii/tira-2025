def find_segments(data):
  result = []
  letters = 0
  last_num = data[0]
  for mark in data:
    if mark == last_num:
      letters += 1
    else: 
      result.append((letters, last_num))
      last_num = mark
      letters = 1
  result.append((letters, last_num))
  return result



if __name__ == "__main__":
    print(find_segments("aabbcc"))
    # # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    # print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]