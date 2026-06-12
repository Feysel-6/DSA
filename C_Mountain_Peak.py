t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    l,r,m = 0,1,2
    indices = [0] * 3
    possible = False
    while r < n:  
        if a[l] < a[r] and a[l] < a[m]:
            indices[0] = l + 1
            indices[1] = r + 1
            indices[2] = m + 1
        elif a[l] < a[r]:
            indices[0] = l + 1
            indices[1] = r + 1
            m += 1
        else:
            r += 1
            m += 1
        if len(indices) == 2:
            possible = True
            break
        if r == n - 1:
            l += 1
            r = l + 1
    if possible:
        print('YES')
        print(*indices)
    else: 
        print('NO')