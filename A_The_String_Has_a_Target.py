t = int(input())
for _ in range(t):
    n = int(input())
    a = input().lower()
    s = [char for char in a]
    char = a[0]
    idx = 0

    # for i in range(1,n):
    #     if s[i] < s[i-1] and s[i] < char:
    #         char = s[i]
    #         idx = i

    for i in range(1,n):
        if s[i] <= char:
            char = s[i]
            idx = i

    s.pop(idx)
    newS = char + ''.join(s)
    if newS < a:
        print(newS)
    else:
        print(a)