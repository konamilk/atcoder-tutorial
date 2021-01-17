import numpy as np

N = int(input())
a = np.array(list(map(int, input().split())))

Ans = 0
flg = False

while True:
    for _, num in enumerate(a):
        if num % 2 == 1:
            flg = True
            break
    if flg:
        break
    a = a / 2
    Ans += 1

print(Ans)
