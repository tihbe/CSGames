from itertools import product, chain, islice
from functools import reduce
import numpy as np
from scipy import optimize
from tqdm import tqdm
import multiprocessing

# A B C D
# E F G H
# I J K L
# M N O P

# A+B+C+D = VAL
# E+F+G+H = VAL
# I+J+K+L = VAL
# M+N+O+P = VAL
# A+E+I+M = VAL
# B+F+J+N = VAL
# C+G+K+O = VAL
# D+H+L+P = VAL
# A+F+K+P = VAL
# D+G+J+M = VAL

# 10 equations for 17 variables => 9? variables to bruteforce

def is_valid(values):
    A, F, K, P, C, G, E, D, M = values
    val = A+F+K+P
    J = val-M-G-D
    if J<0:
        return False
    B = val-A-C-D
    if B < 0:
        return False
    N = val-B-F-J
    if N < 0:
        return False
    O = val-C-G-K
    if O < 0:
        return False
    H = val-E-F-G
    if H < 0:
        return False
    L = val-D-H-P
    if L < 0:
        return False
    I = val-A-E-M
    if I < 0:
        return False

    return A+B+C+D == E+F+G+H == I+J+K+L == M+N+O+P == \
        A+E+I+M == B+F+J+N == C+G+K+O == D+H+L+P == \
            A+F+K+P == D+G+J+M

    # g = np.array(((A, B, C, D), (E, F, G, H), (I, J, K, L), (M, N, O, P)))

    # return np.all(g.sum(axis=0) == val) and \
    #     np.all(g.sum(axis=1) == val) and \
    #         g.diagonal().sum() == val and \
    #             np.fliplr(g).diagonal().sum() == val

total_count = multiprocessing.Value('i', 0)

def worker_subfunc(q, count):
    while True:
        batch = q.get(True)
        batch_result = sum(map(is_valid, batch))
        with count.get_lock():
            count.value += batch_result

queue = multiprocessing.Queue(100)
pool = multiprocessing.Pool(multiprocessing.cpu_count()-1, worker_subfunc, (queue,total_count,))
batch_size = int(1e5)
gen = np.ndindex(*[10]*9)

for v in tqdm(gen, total=1e9 // batch_size):
    batch = list(chain([v], islice(gen, batch_size-1)))
    queue.put(batch)

print(total_count.value) # 17 248 798
