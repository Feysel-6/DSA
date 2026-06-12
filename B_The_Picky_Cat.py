t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    x = abs(a[0])
    count = 0
    a.sort()
    for num in a:
        if x < abs(num):
            count += 1
    if not n % 2:
        print('YES' if count >= (n//2) - 1 else 'NO')
    else:
        print('YES' if count >= (n//2) else 'NO')