def count_sequences(n):
    if n % 2 != 0 or n < 2:
        return 0
    return binom(n, n//2) // ((n//2 +1))

def binom(a, b):
    return factorial(a) // (factorial(b) * factorial(a-b))

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

if __name__ == "__main__":
    print(count_sequences(1)) # 0
    print(count_sequences(2)) # 1
    print(count_sequences(3)) # 0
    print(count_sequences(4)) # 2
    print(count_sequences(5)) # 0
    print(count_sequences(1000)) # 5