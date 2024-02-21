def count(n):
    return n * (n - 1) // 2 if 2 <= n <= 10000 else "Invalid input. n should be between 2 and 10000 (inclusive)."
print(count(10))