t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if not s:
        print('NO')
        continue

    meow = 'meow'
    cat = s.lower()
    t = cat[0]
    for i in range(1,n):
        if cat[i] != cat[i-1]:
            t += cat[i]
    print('YES' if t == meow else 'NO')