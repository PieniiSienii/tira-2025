def create_distribution(string):
  substrings = {}
  seen = set()
  for length in range(1, len(string) + 1):
      for n in range(len(string) - length + 1):
          sub = string[n:n+length]
          if sub not in seen:
            seen.add(sub)
            if length not in substrings:
              substrings[length] = 1
            else:
              substrings[length] += 1
  return substrings

if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}
    
    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}
    
    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}