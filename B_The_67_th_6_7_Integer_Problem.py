t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    a.sort()
    print(-1 * (sum(a) - 2 * a[-1]))