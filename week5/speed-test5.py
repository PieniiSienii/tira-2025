import random
import time
def find_mode(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    return mode

def sort_mode(numbers):
    first_idx = {}
    for i, x in enumerate(numbers):
        if x not in first_idx:
            first_idx[x] = i

    nums = sorted(numbers)
    cur_val = nums[0]; cur_len = 1
    best_val = cur_val; best_len = 1

    for x in nums[1:]:
        if x == cur_val:
            cur_len += 1
        else:
            if (cur_len > best_len or
               (cur_len == best_len and first_idx[cur_val] < first_idx[best_val])):
                best_len = cur_len
                best_val = cur_val
            cur_val = x; cur_len = 1

    if (cur_len > best_len or
       (cur_len == best_len and first_idx[cur_val] < first_idx[best_val])):
        best_val = cur_val
    return best_val

n = 1000
print("n:", n)
random.seed(1337)
numbers = [random.randint(1, 10**7) for _ in range(n)]

start_time = time.time()
result = find_mode(numbers)
end_time = time.time()

print("result:", result)
print("time:", round(end_time - start_time, 4), "s")

start_time = time.time()
result = sort_mode(numbers)
end_time = time.time()

print("SORTED result:", result)
print("time:", round(end_time - start_time, 4), "s")
