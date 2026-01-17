def count_steps(x):
    results = {0: 0, 1: 1}


    for n in range(2,x+1):
        if n == 2:
            results[n] = 1
            continue
        results[n] = 0
        if 1 <= n - 3 and results[n-3] != -1:
            results[n] += results[n-3]
        if   n % 2 == 0 and results[n // 2] != -1:
            results[n] += results[n // 2]
    return results[x]

if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311