def check_number(number):
  check_num = [3,7,1,3,7,1,3,7]
  counter = 0
  sum = 0

  if len(number) != 9 or int(number[0]) != 0:
     return False

  for num in number:
    if counter == 8:
      continue
    sum += int(num) * check_num[counter]
    counter += 1

  last_num = int(str(sum)[-1]) 

  if last_num == 0 and int(number[-1]) == 0:
     return True
  if 10 - last_num == int(number[-1]):
     return True
  return False

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False