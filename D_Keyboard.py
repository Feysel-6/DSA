from collections import Counter
from collections import defaultdict
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if n == 1:
        print(s[0])
        continue
    count = Counter(s)
    sCount = defaultdict(int)
    working = []
    l,r = 0,1
    while r < n:
        if s[l] != s[r]:
            sCount[s[l]] += 1
            l += 1
            r += 1
        else:
            sCount[s[l]] += 1
            l = r + 1
            if l == n - 1:
                sCount[s[l]] += 1
            r += 2

    for val,freq in enumerate(count):
        if sCount[freq] == val:
            working.append(freq)
    working.sort()
    print(''.join(working))