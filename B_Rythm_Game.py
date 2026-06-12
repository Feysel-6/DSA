t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    lastOne = -1
    ans = 0
    for i in range(n):
        if s[i] == '1':
            if lastOne == -1 or i - lastOne >= k:
                ans += 1
            lastOne = i

    print(ans)