n = int(input())
a = list(map(int,input().split()))
a.sort()
count = 0
k = 1
for i in range(n):
    if a[i] >= k:
        count += 1
        k += 1
    else:
        continue
print(count)