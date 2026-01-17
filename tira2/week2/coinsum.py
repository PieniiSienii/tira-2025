def can_create(coins, target):
    results = [False]* (target + 1)
    results[0] = True
    for c in coins:
        for s in range(c, target +1):
            if results[s-c]:
                results[s] = True
        if results[target]:
            return True
    return False

if __name__ == "__main__":
    # print(can_create([1, 2, 5], 13)) # True
    print(can_create([2, 4, 6], 13)) # False
    # print(can_create([1], 42)) # True
    print(can_create([2, 4, 6], 42)) # True
    print(can_create([3], 1337)) # False
    print(can_create([3, 4], 1337)) # True