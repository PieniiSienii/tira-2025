def create_string(pages):
  all_pages = []
  pages = sorted(pages)
  first_p = pages[0]
  for i in range(len(pages)):
    if i == len(pages)-1:
      all_pages.append((first_p, pages[i]))
      continue
    if pages[i] +1 < pages[i+1]:
      all_pages.append((first_p, pages[i]))
      first_p = pages[i+1]
  string = ""
  for pair in all_pages:
    if pair[0] == pair[1]:
      string += f"{pair[0]},"
    else:
      string += f"{pair[0]}-{pair[1]},"
  return string[:-1]
if __name__ == "__main__":
#  print(create_string([1])) # 1
  print(create_string([1, 2, 3])) # 1-3
  print(create_string([1, 1, 1])) # 1
  print(create_string([1, 2, 1, 2])) # 1-2
  print(create_string([1, 6, 2, 5])) # 1-2,5-6
  print(create_string([1, 3, 5, 7])) # 1,3,5,7
  print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
  print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

  pages = [3, 2, 1, 3, 2, 1]
  print(create_string(pages)) # 1-3
  print(pages) # [3, 2, 1, 3, 2, 1]