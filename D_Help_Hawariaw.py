import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    
    b.sort()
    a11 = b[0]
    
    expected = []
    
    for i in range(n):
        for j in range(n):
            expected.append(a11 + i * c + j * d)
    
    expected.sort()
    
    if expected == b:
        print("YES")
    else:
        print("NO")