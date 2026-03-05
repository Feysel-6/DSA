n, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p1 = 0
p2 = 0
merged = []

while p1 < n and p2 < n2:
    if a[p1] < b[p2]:
        merged.append(a[p1])
        p1 += 1
    else:
        merged.append(b[p2])
        p2 += 1
while p1 < n:
    merged.append(a[p1])
    p1 += 1

while p2 < n2:
    merged.append(b[p2])
    p2 += 1

print(*merged)
