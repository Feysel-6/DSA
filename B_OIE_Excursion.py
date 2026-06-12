t = int(input())

for _ in range(t):
    n,m  = map(int,input().split())
    a = list(map(int,input().split()))

    if a[0] == m:
        print('NO')
        continue

    forbidden = []
    for i in range(n):
        k = (-a[i] - i) // m
