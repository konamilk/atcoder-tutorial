import numpy as np

N, A, B = map(int, input().split())

a = np.arange(N) + 1

def Sum_Digits(x):
    s = str(100000 + x)
    return (int(s[1]) + int(s[2]) + int(s[3]) + int(s[4]) + int(s[5]))

b = np.array(list(map(Sum_Digits, a)))

c = a[(b >= A) & (b <= B)]

print(c.sum())
