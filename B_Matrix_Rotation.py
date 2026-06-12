t = int(input())
for _ in range(t):
    a = [list(map(int,input().split())) for _ in range(2)]
    x = ((a[0][0] + a[1][1]) - (a[0][1] + a[1][0]))
    count = 0
    possible = False
    while count < 4:
        if a[0][0] < a[0][1] and a[0][0] < a[1][0] and a[0][1] < a[1][1] and a[1][0] < a [1][1]:
            possible = True
            break
        temp = a[0][0] 
        a[0][0] = a[1][0]
        temp2 = a[0][1]
        a[0][1] = temp
        temp = a[1][1]
        a[1][1] = temp2
        a[1][0] = temp
        count += 1
    
    print('NO' if not possible else 'YES')