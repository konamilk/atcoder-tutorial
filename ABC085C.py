N, Y = map(int, input().split())

found = False

for x in range(N + 1):
    for y in range(N + 1 - x):
        z = N - x - y
        if x * 10_000 + y * 5_000 + z * 1_000 == Y:
            found = True
            print(f'{x} {y} {z}')
            break
    if found:
        break

if not found:
    print('-1 -1 -1')
