H, M = map(int, list(input().split()))
plus = int(input())

if M + plus < 60:
    M = M + plus
else:
    H += (M + plus) // 60
    if H > 23:
        H = H % 24
    M = (M + plus) % 60

print(H, M)
