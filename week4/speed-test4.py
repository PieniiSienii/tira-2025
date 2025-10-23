import random
import time

def count_rounds(numbers):
    n = len(numbers)

    rounds = 1
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1

    return rounds

def count_rounds_dict(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

n = 1000
print("n:", n)
random.seed(1337)
numbers = list(range(1, n + 1))
random.shuffle(numbers)

start_time = time.time()
result = count_rounds(numbers)
end_time = time.time()

print("result list:", result)
print("time list:", round(end_time - start_time, 4), "s")

start_time = time.time()
result = count_rounds_dict(numbers)
end_time = time.time()

print("result dict:", result)
print("time dict:", round(end_time - start_time, 4), "s")