t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    accumulator = 0
    prefixSum = [0] * n
    for i in range(n):
        num = a[i]
        accumulator += num
        if accumulator >= num:
            
        prefixSum[i] = num
