N, K = map(int,input().split())
list1 = []
for i in range(1, N+1):
    if N % i  == 0 :
        list1.append(i)

        