cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


print(sum([fibonacci(n) for n in range(1,300) if fibonacci(n) <= 4e6 and fibonacci(n) % 2 == 0]))