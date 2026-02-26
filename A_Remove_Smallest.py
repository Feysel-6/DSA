t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    if all(x == array[0] for x in array):
        print('YES')
        continue
    array.sort()
    for i in range(1, n):
        if not abs(array[i] - array[i-1]) <= 1:
            print('NO')
            break
    else:
        print('YES')