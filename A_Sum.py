f = int(input())
for _ in range(f):
    values = list(map(int,input().split()))
    print('YES' if max(values) == sum(values) - max(values) else 'NO');