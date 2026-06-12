t = int(input())

for _ in range(t):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    # I can also use diffrence logic
    if x1 >= y1 and y2 >= x2:
        print('NO')
    elif x1 <= y1 and x2 >= y2:
        print('NO')
    else: 
        print('YES')
