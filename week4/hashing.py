def hash_value(string):
  A = 23
  M = 2**32
  h = 0
  for c in string:
      value = ord(c) - ord("a")
      h = (h * A + value) % M
  return h


if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440