import numpy as np

N = input()
a = list(map(int, input().split()))

sorts = sorted(a, reverse=True)

Alice = np.array(sorts)[::2].sum()
Bob = np.array(sorts)[1::2].sum()

print(Alice - Bob)