t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    mx = 0
    for i in range(n):
        if a[i] >= mx:
            count += 1
            mx = a[i]
    print(count)