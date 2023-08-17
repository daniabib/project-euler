def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def largest_factor(n: int, prime_factors = []) -> int:
    if n > 0:
        for prime in primes(200000):
            if n % prime == 0:
                print(prime)
                prime_factors.append(prime)
                return largest_factor(n/prime, prime_factors)
    return prime_factors[-1]
        
# print(largest_factor(13195))
print(largest_factor(600851475143))