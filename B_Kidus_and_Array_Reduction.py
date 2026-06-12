t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    maxVal = -1
    
    for i in range(n):
        if a[i] >= maxVal:
            maxVal = a[i]
            count += 1
    
    print(count)