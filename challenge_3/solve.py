import numpy as np

# Sieve of eratosthenes
N = int(1e6)
l = np.ones(N, dtype=bool)
for i in range(2, N):
    if l[i]:
        l[i*i::i] = False

# Remove 0 from primes
l[0] = False
prime_numbers = np.flatnonzero(l)
sum_of_primes = np.cumsum(prime_numbers)

for length in range(len(prime_numbers), 1, -1):
    m = len(prime_numbers) - length - 1
    if length % 2 == 0:
        m = min(m, 2)
    for i in range(1, m):
        curr_sum = sum_of_primes[i+length-1] - sum_of_primes[i-1]
        if curr_sum >= N:
            break
        if l[curr_sum]:
            print("Prime numbers:", prime_numbers[i:i+length])
            print("Length:", length)
            print("Sum (prime):", curr_sum)
            exit(0)
