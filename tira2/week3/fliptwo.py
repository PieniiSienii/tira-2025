import collections
def find_first(size, steps):
    items = collections.deque(range(1, size +1))
    for i in range(steps):
        num = items.popleft()
        num2 = items.popleft()
        items.append(num2)
        items.append(num)
    return items[0]
if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295 