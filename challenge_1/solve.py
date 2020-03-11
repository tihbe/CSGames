import numpy as np
grid = np.loadtxt("grid.txt", dtype=int)
max_val = 0
max_info = {}
for i, j in np.ndindex(*grid.shape):
    combinations = [
        grid[i:i+4,j],
        grid[i,j:j+4],
        grid[i:i+4,j:j+4].diagonal(),
        np.fliplr(grid[i:i+4,j:j+4]).diagonal()
    ]
    iter_result = [np.prod(comb) for comb in combinations]
    best = np.argmax(iter_result)
    if iter_result[best] > max_val:
        max_val = iter_result[best]
        max_info = {
            'value': iter_result[best],
            'indices': (i, j),
            'type': best,
            'elements': combinations[best],
        }
print(max_info)
