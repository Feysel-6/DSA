n, n2 = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
p1 = 0
tracker = []
for second in range(n2):
    while p1 < n and a[p1] < b[second]:
        p1+=1
    tracker.append(p1)
print(*tracker)
