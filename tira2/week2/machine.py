def min_steps(x):
    results = [-1, 0]


    for n in range(2,x+1):
        results.append(-1)
        if 1 <= n - 3 and results[n-3] != -1:
            results[n] = results[n-3] + 1
        if   n % 2 == 0 and results[n // 2] != -1:
            if results[n] != -1:
                results[n] = min(results[n // 2] + 1, results[n])
            else:
                results[n] = results[n // 2] + 1
    return results[x]

if __name__ == "__main__":
    print(min_steps(1)) # 0
    print(min_steps(2)) # 1
    print(min_steps(3)) # -1
    print(min_steps(4)) # 1
    print(min_steps(5)) # 2
    print(min_steps(17)) # 4
    # print(min_steps(42)) # -1
    # print(min_steps(100)) # 7
    # print(min_steps(1000)) # 13