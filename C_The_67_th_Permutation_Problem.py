t = int(input())
for _ in range(t):
    n = int(input())
    perm = [i for i in range(1,3*n+1)]
    res = []
    i, j = 0, 3*n-1
    while i < j:
        res.append(perm[i])
        res.append(perm[j])
        res.append(perm[j-1])
        i += 1
        j -= 2
    print(*res)