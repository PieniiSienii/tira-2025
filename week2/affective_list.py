import time

def add_remove(n):
  numbers = []
  start_time_add = time.time()
  for i in range(1,n+1):
    numbers.append(i)
  end_time_add = time.time()
  add_time = end_time_add - start_time_add

  start_time_pop = time.time()
  while numbers:
    numbers.pop(0)
  end_time_pop = time.time()
  pop_time = end_time_pop - start_time_pop
  print("Time for add: ", round(add_time, 4), "s")
  print("Time for remove: ", round(pop_time, 4), "s")

n = 10**5
add_remove(n)

