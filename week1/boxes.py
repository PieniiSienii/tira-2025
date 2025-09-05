def min_count(product_count, box_size):
  boxes = 0
  while True:
    if product_count >= box_size:
      product_count -= box_size
      boxes += 1
    else:
      if product_count != 0:
        boxes += 1
      break
  return boxes

if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1