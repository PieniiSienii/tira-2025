def check_year(year):
  numbers = list(map(int, str(year)))
  if ((numbers[0]*10 + numbers[1]) + (numbers[2] *10 + numbers[3])) **2 == year:
    return True
  return False

if __name__ == "__main__":
  print(check_year(1995)) # False
  print(check_year(2024)) # False
  print(check_year(2025)) # True
  print(check_year(2026)) # False
  print(check_year(3025)) # True
  print(check_year(5555)) # False