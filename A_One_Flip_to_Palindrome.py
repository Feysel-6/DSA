t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l,r = 0,n-1
    possible = True
    if not n % 2:
        while l < r:
            if s[l] != s[r]:
                possible = False
                break
            l += 1
            r -= 1
    else:
        

    print('Yes' if possible else 'No')