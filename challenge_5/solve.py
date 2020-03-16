import numpy as np

multiplicators = [2, 3, 4, 5, 6]

for i in range(1, 0xffffffffff):
    i_digits = sorted(str(i))
    is_valid = True
    for j in multiplicators:
        if i_digits != sorted(str(j*i)):
            is_valid = False
            break
    if is_valid:
        print(i)
        break
