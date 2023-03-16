N, M = map(int, input().split())

arr = [i+1 for i in range(N)]
for _ in range(M):
    i,j,k = map(int,input().split())
    arr = arr[:i-1]+arr[k-1:j]+arr[i-1:k-1]+arr[j:]
for b in arr:
    print(b,end=' ')