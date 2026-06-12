t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    first = 0
    count = 0
    for second in range(n):
        if a[first] <= b[second]:
            first += 1
        else:
            count += 1
    print(count)