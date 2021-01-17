S = input()

words = ['dream', 'dreamer', 'erase', 'eraser']

dp = [False] * (len(S) + 10)
dp[0] = True

for i in range(len(S)):
    if not dp[i]:
        continue

    for word in words:
        slice = S[i:i+len(word)]
        # print(f'[{i}]{slice} {"/OK" if slice == word else ""}')

        if slice == word:
            dp[i + len(word)] = True

# print(dp)
print('YES' if dp[len(S)] else 'NO')
