A, B, C = map(int, list(input().split()))

if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+1))
