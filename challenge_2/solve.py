from itertools import permutations
import numpy as np
from tqdm import tqdm

# Sieve of eratosthenes
N = int(1e6)
l = np.ones(N, dtype=bool)
for i in np.arange(2, N):
    if l[i]:
        l[i*i::i] = False

count = 1
circular_primes = [2]
for i in tqdm(np.arange(3, N, 2)):
    if l[i]:
        strp = str(i)
        if '2' in strp:
            continue
        possibilities = list(map(lambda i: int("".join(i)), permutations(strp)))
        all_primes = True
        for j in possibilities:
            if l[j]:
                l[j] = False
            else:
                all_primes = False
                break
        if all_primes:
            count += len(possibilities)
            circular_primes += possibilities

print(circular_primes)           
print(count)

