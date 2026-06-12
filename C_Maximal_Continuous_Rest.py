from collections import defaultdict

n = int(input())
hours = list(map(int,input().split()))

if not 1 in hours:
    print(0)
    exit()

trace = defaultdict(int)

left = 0
maxRest = 0

for right in range(2*n):
    trace[hours[right % n]] += 1
    while left < 2 * n and 0 in trace:
        trace[hours[left % n]] -= 1
        if trace[hours[left % n]] == 0:
            del trace[hours[left % n]]
        left += 1
    maxRest = max(maxRest, right - left + 1)

print(maxRest)