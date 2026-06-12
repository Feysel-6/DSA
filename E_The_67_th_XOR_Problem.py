t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    right = n -1

    while n > 1:
        for i in range(right):
            a[i] = a[i] ^ a[right]
        a.pop()
        right -= 1
        n -= 1
    
    print(*a)