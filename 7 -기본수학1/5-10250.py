T = int(input())

for i in range(T):  # 몇 번 돌릴건지
    H, W, N = map(int, list(input().split()))  # 호텔 층 수, 각 층의 방 수, 몇 번째 손님
    num = N // H + 1  # 방 번호(뒷자리)
    floor = N % H  # 층 수 (앞자리)
    if N % H == 0:
        num = N // H
        floor = H
    print(f'{floor*100+num}')
