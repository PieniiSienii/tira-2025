import random
import time
# toteutus 1
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

n = 10**7
random.seed(1337)
numbers = [random.randint(1, 10**7) for _ in range(n)]

start_time = time.time()
result = count_even(numbers)
end_time = time.time()

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")

start_time = time.time()
result = count_even2(numbers)
end_time = time.time()

print("result 2:", result)
print("time 2:", round(end_time - start_time, 2), "s")