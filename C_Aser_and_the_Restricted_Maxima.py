t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    cnt = 0

    for ch in s:
        if ch == '1':
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            print('NO')
            break
    else:
        l = 1
        r = n
        ans = [0] * n
        for i in range(n):
            if s[i] == '1':
                ans[i] = l
                l += 1
            else:
                ans[i] = r
                r -= 1
        print('YES')
        print(*ans)