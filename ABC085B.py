import numpy as np

N = int(input())
d = np.array([int(input()) for _ in range(N)])

print(len(np.unique(d)))